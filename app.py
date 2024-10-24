from dotenv import load_dotenv
load_dotenv()

import pandas as pd
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure API Key
genai.configure(api_key=os.getenv("GENERATIVEAI_API_KEY"))

# Function to load Google Gemini Model and Provide SQL Query as Response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text.strip()

# Function to retrieve data from the database
def get_data(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    column_names = [description[0] for description in cur.description]  # Get column names
    conn.commit()
    conn.close()
    return column_names, rows  # Return both column names and rows

# Define your Prompt
prompt = ["""
You are an expert in converting English questions to SQL query!
The SQL database has the name retail_data and has the following columns - PRODUCT_ID, PRODUCT_NAME, CATEGORY, PRICE, QUANTITY_SOLD, CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_AGE, SALE_DATE, STORE_LOCATION
For example, Example 1 - What are the details of all products in the "Apparel" category?, the SQL command will be something like this SELECT * FROM RETAIL_DATA WHERE CATEGORY = 'Apparel';
Example 2 - How many products are available in each category?, the SQL command will be something like this SELECT CATEGORY, COUNT(*) AS PRODUCT_COUNT FROM RETAIL_DATA GROUP BY CATEGORY;
Example 3 - Give me first 5 rows of the table?, the SQL command will be something like this SELECT * FROM RETAIL_DATA LIMIT 5;
also the sql code should not have ``` in beginning or end and sql word in the output
Also, if user greets you should also greet the user and if any question asked outside of the database it should return "Sorry, I don't understand, I am a bot for answering questions about retail data and can not answer your question."
"""]

# Streamlit app
st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini App To Retrieve SQL Query")

question = st.text_input("Input", key='input')
submit = st.button("Ask Your Question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    
    st.subheader("The Response Is")
    
    if response.lower().startswith("select"):  # Check if response is a SQL command
        column_names, data = get_data(response, "retail_data.db")
        
        if data:
            # Convert data to a DataFrame for better visualization
            df = pd.DataFrame(data, columns=column_names)  # Set column names
            st.dataframe(df)
        else:
            st.write("No data found.")
    else:
        st.write(response)  # Display as plain text if not a SQL command
