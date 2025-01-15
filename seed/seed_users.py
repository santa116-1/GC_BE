# Seed data
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import UserRole, User
from passlib.hash import bcrypt

def seed_users(session: Session):
    roles_permissions = {
        UserRole.Administrator: {
            "can_view_all_users": True,
            "can_view_all_data": True,
            "can_send_commands": True,
        },
        UserRole.Operator: {
            "can_view_all_users": False,
            "can_view_all_data": True,
            "can_send_commands": True,
        },
        UserRole.Viewer: {
            "can_view_all_users": False,
            "can_view_all_data": True,
            "can_send_commands": False,
        },
    }

    users = [
        {
            "email": "admin@example.com",
            "password": "password",
            "role": UserRole.Administrator,
        },
        {
            "email": "ope@example.com",
            "password": "password",
            "role": UserRole.Operator,
        },
        {
            "email": "view@example.com",
            "password": "password",
            "role": UserRole.Viewer,
        },
    ]

    for user_data in users:
        hashed_password = bcrypt.hash(user_data["password"])
        role_permissions = roles_permissions[user_data["role"]]

        user = User(
            email=user_data["email"],
            hashed_password=hashed_password,
            role=user_data["role"],
            **role_permissions
        )

        # Check if user already exists
        existing_user = session.query(User).filter_by(email=user.email).first()
        if not existing_user:
            session.add(user)

    session.commit()
    print(f"✅ Seeded User records successfully!")

if __name__ == "__main__":

    with SessionLocal() as session:
        seed_users(session)
    print("Seeding completed.")
