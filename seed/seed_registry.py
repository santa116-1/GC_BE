from seed.seed_users import seed_users
from seed.seed_communication import seed_communications
from seed.seed_mission import seed_ship_mission
from seed.seed_propulsion import seed_propulsion_data
from seed.seed_system import seed_ship_system
from seed.seed_telemetry import seed_telemetry

SEED_FUNCTIONS = [
    seed_users,
    seed_communications,
    seed_ship_mission,
    seed_propulsion_data,
    seed_ship_system,
    seed_telemetry
]
