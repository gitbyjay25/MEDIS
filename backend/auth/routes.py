from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random
import string
from typing import Optional

from ..database.db_config import get_db
from ..database.models import User
from .utils import (
    verify_password,
    get_password_hash,
    create_access_token,
    verify_token,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Email service (placeholder - implement actual email service)
def send_reset_email(email: str, token: str):
    """Send password reset email"""
    # TODO: Implement actual email service
    print(f"Reset link sent to {email}: {token}")
    return True

@router.post("/register")
async def register(
    username: str,
    email: str,
    name: str,
    gender: str,
    date_of_birth: str,
    password: str,
    confirm_password: str,
    db: Session = Depends(get_db)
):
    # Validate passwords match
    if password != confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match"
        )

    # Check if username or email already exists
    if db.query(User).filter(User.username == username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Validate gender
    if gender not in ["male", "female", "other"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid gender selection"
        )

    # Convert date_of_birth string to Date object
    try:
        dob = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid date format"
        )

    # Create new user
    hashed_password = get_password_hash(password)
    user = User(
        username=username,
        email=email,
        name=name,
        gender=gender,
        date_of_birth=dob,
        hashed_password=hashed_password
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"status": "success", "message": "User registered successfully"}

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # Find user
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {
        "status": "success",
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.post("/forgot-password")
async def forgot_password(
    email: str,
    db: Session = Depends(get_db)
):
    # Find user by email
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email not found"
        )

    # Generate reset token
    reset_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    reset_token_expires = datetime.utcnow() + timedelta(hours=1)

    # Update user with reset token
    user.reset_token = reset_token
    user.reset_token_expires = reset_token_expires
    db.commit()

    # Send reset email
    send_reset_email(email, reset_token)

    return {
        "status": "success",
        "message": "Password reset link sent to your email"
    }

@router.post("/reset-password")
async def reset_password(
    token: str,
    new_password: str,
    confirm_new_password: str,
    db: Session = Depends(get_db)
):
    # Validate passwords match
    if new_password != confirm_new_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match"
        )

    # Find user by reset token
    user = db.query(User).filter(
        User.reset_token == token,
        User.reset_token_expires > datetime.utcnow()
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired reset token"
        )

    # Update password and clear reset token
    user.hashed_password = get_password_hash(new_password)
    user.reset_token = None
    user.reset_token_expires = None
    db.commit()

    return {
        "status": "success",
        "message": "Password updated successfully"
    } 