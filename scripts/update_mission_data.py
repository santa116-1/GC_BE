import random
import time
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ShipMission

def update_ship_mission_data(session: Session, num_entries: int = 100):
    """Update ShipMission data with small realistic variations."""
    ship_missions = (
        session.query(ShipMission)
        .filter(ShipMission.ship_id <= num_entries)
        .all()
    )

    for ship_mission in ship_missions:
        # Update mission area and mode randomly
        ship_mission.mission_area = random.randint(0, 5)
        ship_mission.current_mode = random.randint(0, 5)

        # Slightly adjust destination coordinates
        ship_mission.destination_latitude = round(
            max(35.396308, min(38.551483, ship_mission.destination_latitude + random.uniform(-0.01, 0.01))), 6
        )
        ship_mission.destination_longitude = round(
            max(138.111111, min(139.986411, ship_mission.destination_longitude + random.uniform(-0.01, 0.01))), 6
        )

    try:
        session.commit()
        print(f"✅ Updated {len(ship_missions)} ship mission records successfully!")
    except Exception as e:
        session.rollback()
        print(f"❌ Error updating ship mission records: {e}")

if __name__ == "__main__":
    while True:
        with SessionLocal() as session:
            update_ship_mission_data(session, num_entries=100)  # Adjust the number of entries to update
        time.sleep(10)
