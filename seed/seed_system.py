# seed_ship_system.py
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ShipSystem
import random

def seed_ship_system(session: Session, num_entries: int = 100):
    """Seed ShipSystem data with random values."""
    
    for i in range(1, num_entries + 1):
        ship_system = ShipSystem(
            ship_id=i,
            system_status=random.randint(1, 2),
            total_operating_time=random.randint(100, 1000),
            current_operating_time=random.randint(50, 1000),
            cpu_usage=random.randint(0, 100),  
            memory_usage=random.randint(0, 100),
            disk_usage=random.randint(0, 100)
        )
        session.add(ship_system)
    session.commit()
    print(f"✅ Seeded {num_entries} ship system records successfully!")

if __name__ == "__main__":
    with SessionLocal() as session:
        seed_ship_system(session, num_entries=100)
