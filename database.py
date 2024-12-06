import psycopg2
from psycopg2.extras import RealDictCursor

# Function to get a database connection
def get_connection():
    return psycopg2.connect(
        dbname="premiert",
        user="postgres",
        password="kundwa",
        host="localhost",  # Or your database host
        port="5432",       # Default PostgreSQL port
        cursor_factory=RealDictCursor
    )

# Function to initialize the tables
def initialize_db():
    connection = get_connection()
    cursor = connection.cursor()

    # Create the tables if they don't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS owners (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );
    CREATE TABLE IF NOT EXISTS buses (
        id SERIAL PRIMARY KEY,
        plate_number VARCHAR(20) NOT NULL UNIQUE,
        owner_id INTEGER REFERENCES owners(id) ON DELETE CASCADE
    );
    """)
    connection.commit()
    cursor.close()
    connection.close()
