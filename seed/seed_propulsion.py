from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Propulsion
import random

def seed_propulsion_data(session: Session, num_entries: int = 100):
    """Populate the Propulsion table with realistic/randomized data."""
    for i in range(1, num_entries + 1):
        propulsion = Propulsion(
            ship_id=i,
            latitude=round(random.uniform(35.2, 35.3), 6),
            longitude=round(random.uniform(139.5, 139.6), 6),
            speed=round(random.uniform(0, 1), 2),
            direction=round(random.uniform(0, 1), 2),
            roll=round(random.uniform(0, 1), 2),
            pitch=round(random.uniform(0, 1), 2),
            yaw=round(random.uniform(0, 1), 2),
            rudder_output=round(random.uniform(0, 1), 2),
            rudder_angle=round(random.uniform(0, 1), 2)
        )
        session.add(propulsion)
    session.commit()
    print(f"✅ Seeded {num_entries} propulsion records successfully!")

if __name__ == "__main__":
    with SessionLocal() as session:
        seed_propulsion_data(session, num_entries=100)  # Adjust for the number of records you want to generate
