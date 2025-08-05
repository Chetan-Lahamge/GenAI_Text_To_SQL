DB_FILE = "retail_data.db"
TABLE_NAME = "retail_data"
CSV_FILE = "retail_data.csv"
API_KEY_ENV_VAR = "GENERATIVEAI_API_KEY"

PROMPT_TEMPLATE = """
You are an expert in converting English questions to SQL query!
The SQL database has the name {table_name} and has the following columns - {columns}
For example, Example 1 - What are the details of all products in the "Apparel" category?, the SQL command will be something like this SELECT * FROM {table_name} WHERE CATEGORY = 'Apparel';
Example 2 - How many products are available in each category?, the SQL command will be something like this SELECT CATEGORY, COUNT(*) AS PRODUCT_COUNT FROM {table_name} GROUP BY CATEGORY;
Example 3 - Give me first 5 rows of the table?, the SQL command will be something like this SELECT * FROM {table_name} LIMIT 5;
also the sql code should not have ``` in beginning or end and sql word in the output
Also, if user greets you should also greet the user and if any question asked outside of the database it should return "Sorry, I don't understand, I am a bot for answering questions about retail data and can not answer your question."
"""

INSIGHTS_PROMPT_TEMPLATE = """
As a data analyst, you are presented with the following data, which was retrieved based on the user's question: '{user_question}'.

Data:
```json
{data_json}
```

Please provide a brief, insightful summary based on this data. Focus on the key takeaways a business user would find valuable. Avoid simply restating the data; instead, interpret what it means.
"""
