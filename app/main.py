from fastapi import FastAPI, Depends, HTTPException
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

@app.get("/api/shipData/{ship_id}", response_model=schemas.Ship)
def get_ship_data_by_id(ship_id: int, db: Session = Depends(get_db)):
    ship = db.query(models.Ship).filter(models.Ship.id == ship_id).first()
    if ship is None:
        raise HTTPException(status_code=404, detail="Ship not found")
    return ship

# Propulsion Action
# @app.get("api/propulsion/")
# def read_ships(db: Session = Depends(get_db)):
#     ships = db.query(models.Propulsion).all()
#     return ships

# @app.post("api/propulsion/")
# def create_ship(ship: models.Propulsion, db: Session = Depends(get_db)):
#     db.add(ship)
#     db.commit()
#     db.refresh(ship)
#     return ship

# @app.get("/api/propulsion/{ship_id}")
# def get_ship_data_by_id(ship_id: int, db: Session = Depends(get_db)):
#     ship = db.query(models.Propulsion).filter(models.Propulsion.id == ship_id).first()
#     if ship is None:
#         raise HTTPException(status_code=404, detail="Ship Propulsion Data not found")
#     return ship