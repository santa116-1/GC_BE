from seed.seed_registry import SEED_FUNCTIONS
from app.database import SessionLocal

def run_all_seeds():
    """Run all seed functions."""
    with SessionLocal() as session:
        for seed_func in SEED_FUNCTIONS:
            print(f"Seeding {seed_func.__name__}...")
            seed_func(session)
            print(f"✅ {seed_func.__name__} completed!")

if __name__ == "__main__":
    run_all_seeds()
