import random
import time
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Telemetry

def update_telemetry_data(session: Session, num_entries: int = 100):
    """Update telemetry data with small realistic variations."""
    telemetries = (
        session.query(Telemetry)
        .filter(Telemetry.ship_id <= num_entries)
        .all()
    )

    for telemetry in telemetries:
        # Apply small random variations to telemetry fields
        telemetry.thruster_output = max(0, min(100, telemetry.thruster_output + random.randint(-10, 10)))
        telemetry.thruster_rotation_speed = max(0, min(100, telemetry.thruster_rotation_speed + random.randint(-10, 10)))
        telemetry.thruster_voltage = max(0.0, telemetry.thruster_voltage + round(random.uniform(-0.5, 0.5), 2))
        telemetry.thruster_current = max(0.0, telemetry.thruster_current + round(random.uniform(-0.5, 0.5), 2))

        telemetry.battery_1_remaining = max(0, min(100, telemetry.battery_1_remaining + random.randint(-10, 10)))
        telemetry.battery_1_voltage = max(0.0, telemetry.battery_1_voltage + round(random.uniform(-0.5, 0.5), 2))
        telemetry.battery_1_charging_status = random.choice([0, 1, -1])

        telemetry.battery_2_remaining = max(0, min(100, telemetry.battery_2_remaining + random.randint(-10, 10)))
        telemetry.battery_2_voltage = max(0.0, telemetry.battery_2_voltage + round(random.uniform(-0.5, 0.5), 2))
        telemetry.battery_2_charging_status = random.choice([0, 1, -1])

        telemetry.battery_3_remaining = max(0, min(100, telemetry.battery_3_remaining + random.randint(-10, 10)))
        telemetry.battery_3_voltage = max(0.0, telemetry.battery_3_voltage + round(random.uniform(-0.5, 0.5), 2))
        telemetry.battery_3_charging_status = random.choice([0, 1, -1])

        telemetry.pcu_voltage = max(0.0, telemetry.pcu_voltage + round(random.uniform(-0.5, 0.5), 2))
        telemetry.pcu_current = max(0.0, telemetry.pcu_current + round(random.uniform(-0.5, 0.5), 2))

        telemetry.solar_voltage = max(0.0, telemetry.solar_voltage + round(random.uniform(-0.5, 0.5), 2))
        telemetry.solar_current = max(0.0, telemetry.solar_current + round(random.uniform(-0.5, 0.5), 2))

        telemetry.body_temperature = max(15.0, min(40.0, telemetry.body_temperature + round(random.uniform(-0.5, 0.5), 2)))

    try:
        session.commit()
        print(f"✅ Updated {len(telemetries)} telemetry records successfully!")
    except Exception as e:
        session.rollback()
        print(f"❌ Error updating telemetry records: {e}")

if __name__ == "__main__":
    while True:
        with SessionLocal() as session:
            update_telemetry_data(session, num_entries=100)  # Adjust the number of entries to update
        time.sleep(10)