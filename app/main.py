from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import ship
from . import models
from .database import engine
from app.api.deps import get_db
from app.api.v1 import auth, users
from app.core.security import verify_token

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/api/ships/", response_model=list[ship.Ship])
def get_ships(db: Session = Depends(get_db), user_email: str = Depends(verify_token)):
    ships = db.query(models.Ship).all()
    return ships

@app.get("/api/shipData/{ship_id}", response_model=ship.Ship)
def get_ship_data_by_id(ship_id: int, db: Session = Depends(get_db), user_email: str = Depends(verify_token)):
    ship = db.query(models.Ship).filter(models.Ship.id == ship_id).first()
    if ship is None:
        raise HTTPException(status_code=404, detail="Ship not found")
    return ship