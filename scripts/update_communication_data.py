import random
import time
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Commnication

def update_communication_data(session: Session, num_entries: int = 100):
    """Update communication data with small changes."""
    for i in range(1, num_entries + 1):
        communication = session.query(Commnication).filter(Commnication.ship_id == i).first()
        
        if communication:
            # Apply small variations to each value
            communication.wifi_status = random.choice([True, False])
            communication.wifi_rssi = max(1, communication.wifi_rssi + random.randint(-20, 20))
            communication.gps_status = random.choice([True, False])
            communication.gps_quality = max(1, communication.gps_quality + random.randint(-20, 20))
        
        session.commit()
    print(f"✅ Updated {num_entries} communication records successfully!")

if __name__ == "__main__":
    while True:
        with SessionLocal() as session:
            update_communication_data(session, num_entries=100)
        time.sleep(10)
