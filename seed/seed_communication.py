# seed_communications.py
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Commnication  # Make sure this is your correct model import
from faker import Faker
import random

fake = Faker()

def seed_communications(session: Session, num_entries: int = 10):
    """Seed Communication data with random values."""
    
    for i in range(1, num_entries + 1):
        communication = Commnication(
            ship_id=i,
            wifi_status=random.choice([True, False]),  # Random boolean for wifi_status
            wifi_rssi=random.randint(0, 100),  # Random wifi RSSI value between -100 and 100
            gps_status=random.choice([True, False]),  # Random boolean for gps_status
            gps_quality=random.randint(1, 100)  # Random GPS quality between 1 and 100
        )
        session.add(communication)
    
    session.commit()
    print(f"✅ Seeded {num_entries} communication records successfully!")

if __name__ == "__main__":
    with SessionLocal() as session:
        seed_communications(session, num_entries=100)
