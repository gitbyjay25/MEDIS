from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)  # Changed from password to hashed_password
    gender = Column(String(20))
    date_of_birth = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    login_history = relationship("LoginHistory", back_populates="user")

class LoginHistory(Base):
    __tablename__ = 'login_history'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    login_time = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(45))  # IPv6 can be up to 45 characters

    user = relationship("User", back_populates="login_history")

# Get the absolute path to the database file
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'medis.db')

# Create database directory if it doesn't exist
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Create database engine with absolute path
engine = create_engine(f'sqlite:///{db_path}')

# Create all tables
Base.metadata.create_all(engine)

# Create session factory
Session = sessionmaker(bind=engine)

# Function to get a new session
def get_session():
    return Session() 