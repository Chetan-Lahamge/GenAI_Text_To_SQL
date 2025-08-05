import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from database import get_db_connection, get_table_schema, execute_query
from llm import configure_llm, get_sql_from_llm

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Retail AI Analyst",
    page_icon="🤖",
    layout="centered",
)

# --- LOAD ENVIRONMENT VARIABLES ---
load_dotenv()

# --- INITIALIZATION ---
def initialize_app():
    """Initialize database, LLM, and session state."""
    conn = get_db_connection()
    if conn is None:
        st.stop()

    model = configure_llm()
    if model is None:
        st.stop()

    if 'history' not in st.session_state:
        st.session_state.history = []

    return conn, model

# --- UI COMPONENTS ---
def display_header():
    """Display the main header and introduction."""
    st.title("🤖 Retail AI Analyst")
    st.markdown("Ask questions about your retail data in plain English and get answers instantly.")

def display_example_questions():
    """Display clickable example questions."""
    st.markdown("**Try these examples:**")
    examples = [
        "What are the top 5 most sold products?",
        "How many customers are in each age group?",
        "What is the total revenue from the 'Electronics' category?",
        "Show me all sales from 'New York' in the last week."
    ]
    for example in examples:
        if st.button(example):
            st.session_state.user_question = example

def display_chat_history():
    """Display the conversation history."""
    for entry in st.session_state.history:
        with st.chat_message(entry["role"]):
            st.markdown(entry["content"])

# --- MAIN LOGIC ---
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import re

from database import get_db_connection, get_table_schema, execute_query
from llm import configure_llm, get_sql_from_llm, get_insights_from_llm

# --- HELPER FUNCTIONS ---
def extract_sql_query(text):
    """Extracts the first SQL query from a text block using a more robust regex."""
    # This regex looks for a non-greedy block starting with SELECT
    # and ending with a semicolon or the end of the string.
    match = re.search(r"(SELECT[\s\S]*?)(?:;|$)", text, re.IGNORECASE)
    if match:
        # Return the first captured group, which is the SQL statement itself
        return match.group(1).strip()
    return None

def display_intelligent_chart(df, sql_query):
    """Analyzes the DataFrame and displays the most appropriate chart."""
    if df.empty or len(df.columns) < 2:
        return

    # Attempt to convert date/time columns
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_datetime(df[col])
            except (ValueError, TypeError):
                pass # Ignore columns that can't be converted

    # Identify column types
    date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]
    numeric_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
    categorical_cols = [col for col in df.columns if col not in date_cols and col not in numeric_cols]

    st.write("### Chart")
    try:
        # Time series line chart
        if date_cols and numeric_cols:
            st.line_chart(df.set_index(date_cols[0])[numeric_cols[0]])
            st.caption(f"Line chart showing {numeric_cols[0]} over time.")
        # Bar chart for grouped data
        elif categorical_cols and numeric_cols and "group by" in sql_query.lower():
            st.bar_chart(df.set_index(categorical_cols[0])[numeric_cols[0]])
            st.caption(f"Bar chart showing {numeric_cols[0]} by {categorical_cols[0]}.")
        # Scatter plot for two numeric columns
        elif len(numeric_cols) >= 2:
            st.scatter_chart(df, x=numeric_cols[0], y=numeric_cols[1])
            st.caption(f"Scatter plot showing the relationship between {numeric_cols[0]} and {numeric_cols[1]}.")
        else:
            st.write("Could not determine a suitable chart for this data.")
    except Exception as e:
        st.warning(f"Could not generate chart: {e}")

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Retail AI Analyst",
    page_icon="🤖",
    layout="centered",
)

# --- INITIALIZATION ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- UI COMPONENTS ---
st.title("🤖 Retail AI Analyst")

# Display chat history
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "data" in message:
            st.dataframe(message["data"], use_container_width=True)
            display_intelligent_chart(message["data"].copy(), message.get("sql", ""))
        if "sql" in message and "data" not in message: # Only show SQL if there was no data
            with st.expander("View Generated SQL"):
                st.code(message["sql"], language="sql")
        if "insights" in message:
            st.info(message["insights"])

# --- MAIN LOGIC ---
if prompt := st.chat_input("Ask your question about the retail data..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            schema = get_table_schema()
            if not schema:
                st.error("Could not retrieve database schema.")
                st.stop()

            llm_response = get_sql_from_llm(prompt, schema)
            sql_query = extract_sql_query(llm_response)

            if not sql_query:
                response_text = llm_response or "Sorry, I couldn't understand that."
                st.markdown(response_text)
                st.session_state.history.append({"role": "assistant", "content": response_text})
            else:
                column_names, data = execute_query(sql_query)

                if not data:
                    st.warning("Your query returned no results.")
                    with st.expander("View Generated SQL"):
                        st.code(sql_query, language="sql")
                    st.session_state.history.append({"role": "assistant", "content": "I ran the query, but it returned no data.", "sql": sql_query})
                else:
                    df = pd.DataFrame(data, columns=column_names)
                    st.markdown(f"Here is the data for your query: *'{prompt}'*")
                    st.dataframe(df, use_container_width=True)
                    
                    display_intelligent_chart(df.copy(), sql_query)

                    with st.spinner("Generating insights..."):
                        insights = get_insights_from_llm(prompt, df.to_json(orient="records"))
                    
                    if insights:
                        st.info(insights)
                    
                    st.session_state.history.append({
                        "role": "assistant",
                        "content": f"Here is the data for your query: *'{prompt}'*",
                        "sql": sql_query,
                        "data": df,
                        "insights": insights
                    })
