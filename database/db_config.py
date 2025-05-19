import sqlite3

def create_connection():
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect("user_history.db")  # Database file
    return conn

def create_table():
    """Create a table to store user history."""
    conn = create_connection()
    cursor = conn.cursor()
    
    # Creating a table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_history (
        user_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        predicted_disease TEXT NOT NULL,
        precautions TEXT NOT NULL,
        prediction_date TEXT NOT NULL
    );
    ''')
    
    conn.commit()
    conn.close()
    
def create_login_history_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS login_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        login_time TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
