from database.models import Base, engine, User, LoginHistory
import os

def init_database():
    # Create database directory if it doesn't exist
    db_dir = os.path.dirname(os.path.abspath('user_history.db'))
    os.makedirs(db_dir, exist_ok=True)
    
    # Create all tables
    Base.metadata.create_all(engine)
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_database() 