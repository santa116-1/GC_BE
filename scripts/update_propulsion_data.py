import random
import time
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Propulsion

def update_propulsion_data(session: Session, num_entries: int = 100):
    """Update propulsion data with small changes."""
    for i in range(1, num_entries + 1):
        propulsion = session.query(Propulsion).filter(Propulsion.ship_id == i).first()
        
        if propulsion:
            # Apply small variations to each value to simulate realistic changes
            propulsion.latitude += round(random.uniform(-0.001, 0.001), 5)
            propulsion.longitude += round(random.uniform(-0.001, 0.001), 5)
            propulsion.speed += round(random.uniform(-0.05, 0.05), 2)
            propulsion.direction += round(random.uniform(-0.05, 0.05), 2)
            propulsion.roll += round(random.uniform(-0.05, 0.05), 2)
            propulsion.pitch += round(random.uniform(-0.05, 0.05), 2)
            propulsion.yaw += round(random.uniform(-0.05, 0.05), 2)
            propulsion.rudder_output += round(random.uniform(-0.05, 0.05), 2)
            propulsion.rudder_angle += round(random.uniform(-0.05, 0.05), 2)
            
            # Ensure values remain within a realistic range
            propulsion.speed = max(0, min(1, propulsion.speed))
            propulsion.direction = max(0, min(1, propulsion.direction))
            propulsion.roll = max(0, min(1, propulsion.roll))
            propulsion.pitch = max(0, min(1, propulsion.pitch))
            propulsion.yaw = max(0, min(1, propulsion.yaw))
            propulsion.rudder_output = max(0, min(1, propulsion.rudder_output))
            propulsion.rudder_angle = max(0, min(1, propulsion.rudder_angle))
        
        session.commit()
    print(f"✅ Updated {num_entries} propulsion records successfully!")

if __name__ == "__main__":
    while True:
        with SessionLocal() as session:
            update_propulsion_data(session, num_entries=100)
        time.sleep(10)
