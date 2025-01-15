# seed_telemetry.py
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Telemetry
from faker import Faker
import random

fake = Faker()

def seed_telemetry(session: Session, num_entries: int = 100):
    """Seed Telemetry data with random values."""
    
    for i in range(1, num_entries + 1):
        telemetry = Telemetry(
            ship_id=i,
            thruster_output=random.randint(0, 100),
            thruster_rotation_speed=random.randint(0, 100),
            thruster_voltage=round(random.uniform(1.0, 5.0), 2),
            thruster_current=round(random.uniform(0.1, 12.0), 2),
            battery_1_remaining=random.randint(1, 100),
            battery_1_voltage=round(random.uniform(0.5, 5.5), 2),
            battery_1_charging_status=random.choice([0, 1, -1]),
            battery_2_remaining=random.randint(1, 100),
            battery_2_voltage=round(random.uniform(0.5, 5.5), 2),
            battery_2_charging_status=random.choice([0, 1, -1]),
            battery_3_remaining=random.randint(1, 100),
            battery_3_voltage=round(random.uniform(0.5, 5.5), 2),
            battery_3_charging_status=random.choice([0, 1, -1]),
            pcu_voltage=round(random.uniform(1.0, 10.0), 2),
            pcu_current=round(random.uniform(0.1, 5.0), 2),
            solar_voltage=round(random.uniform(0.5, 5.5), 2),
            solar_current=round(random.uniform(0.1, 10.0), 2),
            body_temperature=round(random.uniform(15.0, 40.0), 2),
        )
        session.add(telemetry)
    
    session.commit()
    print(f"✅ Seeded {num_entries} telemetry records successfully!")

if __name__ == "__main__":
    with SessionLocal() as session:
        seed_telemetry(session, num_entries=100)  # Set the number of entries to seed (adjust as needed)
