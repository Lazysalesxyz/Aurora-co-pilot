import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the connection string from environment variables
conn_string = os.getenv("POSTGRESML_CONNECTION_STRING")

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    
    # Execute the query
    cursor.execute("SELECT * FROM conversation_memory ORDER BY created_at DESC LIMIT 10;")
    
    # Fetch all results
    rows = cursor.fetchall()
    
    # Get column names
    colnames = [desc[0] for desc in cursor.description]
    print("\nColumn names:", colnames)
    
    # Print the results
    print("\nQuery Results:")
    print("=" * 100)
    
    for row in rows:
        print(row)
    
    print("=" * 100)
    print(f"Total rows: {len(rows)}")
    
    # Close cursor and connection
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}") 