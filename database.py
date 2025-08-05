import sqlite3
import pandas as pd
import streamlit as st
from config import DB_FILE, TABLE_NAME

@st.cache_resource
def get_db_connection():
    """Establishes a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        return conn
    except sqlite3.Error as e:
        st.error(f"Database connection error: {e}")
        return None

@st.cache_data
def get_table_schema():
    """Retrieves the schema of the specified table."""
    try:
        _conn = get_db_connection()
        query = f"PRAGMA table_info({TABLE_NAME});"
        schema_df = pd.read_sql_query(query, _conn)
        return tuple(schema_df['name'].tolist()) # Return as tuple for hashing
    except Exception as e:
        st.error(f"Error fetching schema: {e}")
        return ()

@st.cache_data
def execute_query(sql_query):
    """Executes a SQL query and returns the results."""
    if not sql_query.strip().upper().startswith("SELECT"):
        st.error("Security Alert: Only SELECT queries are allowed.")
        return None, None

    try:
        _conn = get_db_connection()
        cursor = _conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        return column_names, rows
    except sqlite3.Error as e:
        st.error(f"SQL Error: {e}")
        return None, None
