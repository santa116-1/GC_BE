# seed_ship_mission.py
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ShipMission  # Ensure this is the correct import for your model
import random

def seed_ship_mission(session: Session, num_entries: int = 10):
    """Seed ShipMission data with random values."""
    
    for i in range(1, num_entries + 1):
        ship_mission = ShipMission(
            ship_id=i,
            mission_area=random.randint(0, 5),
            current_mode=random.randint(0, 5),
            destination_latitude=round(random.uniform(35.396308, 38.551483), 6),
            destination_longitude=round(random.uniform(138.111111, 139.986411), 6)
        )
        session.add(ship_mission)
    
    session.commit()
    print(f"✅ Seeded {num_entries} ship mission records successfully!")

if __name__ == "__main__":
    with SessionLocal() as session:
        seed_ship_mission(session, num_entries=100)
