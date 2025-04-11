import psycopg2
import os

# Connect to PostgreSQL using environment variable
def get_connection():
    return psycopg2.connect(os.environ("DATABASE"))
