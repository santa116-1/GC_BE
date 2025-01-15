from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Ship
import random
import string
from datetime import datetime, timedelta

def random_date(start_year=2024, end_year=2025):
    """Generate a random date within the specified range."""
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def random_network_interface():
    """Generate a MAC address in the format 00-00-00-XX"""
    return '00-00-00-{:02d}'.format(random.randint(0, 99))

def random_model_number():
    """Generate a random model number based on a pattern with a 3-letter prefix."""
    prefix = ''.join(random.choices(string.ascii_lowercase, k=3))  # 3 random lowercase letters
    suffix = random.randint(100, 999)  # Random number between 100 and 999
    return f"{prefix}-{suffix}"

def random_software_version():
    """Generate a random software version following the pattern 'X.Y.Z'."""
    major = random.randint(1, 2)  # Version major number 1 or 2
    minor = random.randint(0, 9)  # Version minor number between 0 and 9
    patch = random.randint(0, 9)  # Version patch number between 0 and 9
    return f"{major}.{minor}.{patch}"

def seed_device_data(session: Session, num_entries: int = 100):
    """Populate the Device table with realistic/randomized data based on patterns."""
    for i in range(1, num_entries + 1):
        device = Ship(
            id=i,
            manufacturing_date=random_date(),
            model_number=random_model_number(),
            software_version=random_software_version(),
            network_interface_info=random_network_interface()
        )
        session.add(device)
    session.commit()
    print(f"✅ Seeded {num_entries} device records successfully!")

if __name__ == "__main__":
    with SessionLocal() as session:
        seed_device_data(session, num_entries=100)  # Adjust for the number of records you want to generate
