import os
import google.generativeai as genai
import streamlit as st
from config import API_KEY_ENV_VAR, PROMPT_TEMPLATE, TABLE_NAME, INSIGHTS_PROMPT_TEMPLATE

@st.cache_resource
def configure_llm():
    """Configures the Generative AI model."""
    try:
        api_key = os.getenv(API_KEY_ENV_VAR)
        if not api_key:
            st.error("API key not found. Please set the GENERATIVEAI_API_KEY environment variable.")
            return None
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        st.error(f"LLM configuration error: {e}")
        return None

@st.cache_data
def get_sql_from_llm(question, schema):
    """Generates a SQL query from a natural language question."""
    _model = configure_llm()
    if not _model:
        return None

    try:
        columns = ", ".join(schema)
        prompt = PROMPT_TEMPLATE.format(table_name=TABLE_NAME, columns=columns)
        response = _model.generate_content([prompt, question])
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating SQL: {e}")
        return None

@st.cache_data
def get_insights_from_llm(user_question, data_json):
    """Generates data insights from a query result."""
    _model = configure_llm()
    if not _model:
        return None
    
    try:
        prompt = INSIGHTS_PROMPT_TEMPLATE.format(user_question=user_question, data_json=data_json)
        response = _model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating insights: {e}")
        return None
