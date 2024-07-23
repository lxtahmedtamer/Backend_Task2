from sqlalchemy.orm import Session
from models import User

# Read user by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Create a new user
def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Read all users
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# Update user by ID
def update_user(db: Session, user_id: int, user_update: dict):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in user_update.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user
    return None

# Delete user by ID
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None
