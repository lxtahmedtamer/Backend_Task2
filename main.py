from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import crud, models, schemas
from database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return crud.create_user(db=db, user=user)

@app.get("/user/{user_id}", response_model=schemas.User)
def read_user(user_id: int,
    greeting: Optional[str] = None,
    age: Optional[int] = None,
    db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if greeting:
        return {"message": f"Greeting Activated: {user.greeting}"}
    if age is not None:
        return {"message": f"Age Activated: {user.age}"}
    return user

@app.get("/details/{user_id}")
def read_details(user_id: int, include_greeting: Optional[bool] = False, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    details = {"user_id": user.id}
    if include_greeting:
        details["greeting"] = f"Hello from FastAPI! Greeting Activated: {user.greeting}"
    return details
