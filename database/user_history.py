from database.db_config import create_connection
from datetime import datetime

def save_user_history(username, email, predicted_disease, precautions):
    """Save user's prediction history to the database."""
    conn = create_connection()
    cursor = conn.cursor()
    
    # Insert user history into the database
    cursor.execute('''
    INSERT INTO user_history (username, email, predicted_disease, precautions, prediction_date)
    VALUES (?, ?, ?, ?, ?)
    ''', (username, email, predicted_disease, precautions, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    conn.commit()
    conn.close()
    
def get_user_history(user_id):
    """Get a user's history from the database."""
    conn = create_connection()
    cursor = conn.cursor()
    
    # Fetch user history
    cursor.execute("SELECT * FROM user_history WHERE user_id = ?", (user_id,))
    history = cursor.fetchall()
    
    conn.close()
    return history

def save_login_event(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO login_history (user_id, login_time)
    VALUES (?, ?)
    ''', (user_id, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()
    conn.close()

def get_login_history(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT login_time FROM login_history WHERE user_id = ? ORDER BY login_time DESC
    ''', (user_id,))
    history = cursor.fetchall()
    conn.close()
    return history

if __name__ == "__main__":
    # Example usage: save a user history record
    save_user_history('JohnDoe', 'john.doe@example.com', 'Flu', 'Rest and stay hydrated')
