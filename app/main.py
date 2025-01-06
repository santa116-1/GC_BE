from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/ships/", response_model=list[schemas.Ship])
def get_ships(db: Session = Depends(get_db)):
    ships = db.query(models.Ship).all()
    return ships