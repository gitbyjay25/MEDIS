import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from sqlalchemy import create_engine, text
from werkzeug.security import generate_password_hash
import sqlite3

def migrate_users_table():
    """
    Migration script to update users table:
    1. Rename password column to hashed_password
    2. Add is_active column
    3. Re-hash existing passwords
    """
    # Get the absolute path to the database file
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(current_dir, 'medis.db')
    
    # Create SQLite connection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if password column exists
        cursor.execute("PRAGMA table_info(users)")
        columns = cursor.fetchall()
        has_password = any(col[1] == 'password' for col in columns)
        has_hashed_password = any(col[1] == 'hashed_password' for col in columns)
        
        if has_password and not has_hashed_password:
            # Create new hashed_password column
            cursor.execute("ALTER TABLE users ADD COLUMN hashed_password TEXT")
            
            # Copy and hash existing passwords
            cursor.execute("SELECT id, password FROM users")
            users = cursor.fetchall()
            for user_id, password in users:
                hashed = generate_password_hash(password)
                cursor.execute("UPDATE users SET hashed_password = ? WHERE id = ?", (hashed, user_id))
            
            # Drop old password column
            cursor.execute("ALTER TABLE users DROP COLUMN password")
        
        # Add is_active column if it doesn't exist
        cursor.execute("PRAGMA table_info(users)")
        columns = cursor.fetchall()
        if not any(col[1] == 'is_active' for col in columns):
            cursor.execute("ALTER TABLE users ADD COLUMN is_active BOOLEAN DEFAULT TRUE")
        
        # Commit all changes
        conn.commit()
        print("Migration completed successfully!")
        
    except Exception as e:
        print(f"Error during migration: {str(e)}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_users_table() 