from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app.core.security import create_access_token, verify_password, get_password_hash
from app.models import User
from app.schemas.auth import Token, UserLogin
from app.api.deps import get_db

router = APIRouter()

@router.post("/login", response_model=Token)
def login_for_access_token(form_data: UserLogin, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == form_data.email).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.email, "id": user.id, "email": user.email, "view_users": user.can_view_all_users, "view_data": user.can_view_all_data,"send_commands": user.can_send_commands }, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=Token)
def register_user(user: UserLogin, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": new_user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
