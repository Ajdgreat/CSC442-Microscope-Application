from .db import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS measurements (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            microscope_size FLOAT,
            actual_size FLOAT
        );
    """)
    
    conn.commit()
    cur.close()
    conn.close()

def insert_measurement(username, microscope_size, actual_size):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
        INSERT INTO measurements (username, microscope_size, actual_size)
        VALUES (%s, %s, %s);
    """, (username, microscope_size, actual_size))
    
    conn.commit()
    cur.close()
    conn.close()
