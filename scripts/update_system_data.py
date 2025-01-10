import random
import time
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ShipSystem

def update_ship_system_data(session: Session, num_entries: int = 100):
    """Update ShipSystem data with small realistic variations."""
    ship_systems = (
        session.query(ShipSystem)
        .filter(ShipSystem.ship_id <= num_entries)
        .all()
    )

    for ship_system in ship_systems:
        # Apply small random variations to ship system fields
        ship_system.system_status = random.randint(1, 2)
        ship_system.total_operating_time += random.randint(1, 10)  # Increment total operating time
        ship_system.current_operating_time = max(0, ship_system.current_operating_time + random.randint(-5, 10))

        ship_system.cpu_usage = max(0.0, min(100.0, ship_system.cpu_usage + round(random.uniform(-5.0, 5.0), 2)))
        ship_system.memory_usage = max(0.0, min(100.0, ship_system.memory_usage + round(random.uniform(-5.0, 5.0), 2)))
        ship_system.disk_usage = max(0.0, min(100.0, ship_system.disk_usage + round(random.uniform(-5.0, 5.0), 2)))

    try:
        session.commit()
        print(f"✅ Updated {len(ship_systems)} ship system records successfully!")
    except Exception as e:
        session.rollback()
        print(f"❌ Error updating ship system records: {e}")

if __name__ == "__main__":
    while True:
        with SessionLocal() as session:
            update_ship_system_data(session, num_entries=100)  # Adjust the number of entries to update
        time.sleep(10)