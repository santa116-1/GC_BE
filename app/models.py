from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
class Ship(Base):
    __tablename__ = "ships"

    id = Column(Integer, primary_key=True, index=True)
    manufacturing_date = Column(Date)
    model_number = Column(String(255))
    software_version = Column(String(255))
    network_interface_info = Column(String(255)) 

class Propulsion(Base):
    __tablename__ = 'propulsoins'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ship_id = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    speed = Column(Float, nullable=False)
    direction = Column(Float, nullable=False)
    roll = Column(Float, nullable=False)
    pitch = Column(Float, nullable=False)
    yaw = Column(Float, nullable=False)
    rudder_output = Column(Float, nullable=False)
    rudder_angle = Column(Float, nullable=False)

class Commnication(Base):
    __tablename__ = 'communications'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ship_id = Column(Integer, nullable=False)
    wifi_status = Column(Boolean, nullable=False)
    wifi_rssi = Column(Integer, nullable=False)
    gps_status = Column(Boolean, nullable=False)
    gps_quality = Column(Integer, nullable=False)

class Telemetry(Base):
    __tablename__ = "telemetries"
    
    id = Column(Integer, primary_key=True, index=True)
    ship_id = Column(Integer, nullable=False)
    thruster_output = Column(Integer, nullable=False)
    thruster_rotation_speed = Column(Integer, nullable=False)
    thruster_voltage = Column(Float, nullable=False)
    thruster_current = Column(Float, nullable=False)
    battery_1_remaining = Column(Integer, nullable=False)
    battery_1_voltage = Column(Float, nullable=False)
    battery_1_charging_status = Column(Integer, nullable=False)
    battery_2_remaining = Column(Integer, nullable=False)
    battery_2_voltage = Column(Float, nullable=False)
    battery_2_charging_status = Column(Integer, nullable=False)
    battery_3_remaining = Column(Integer, nullable=False)
    battery_3_voltage = Column(Float, nullable=False)
    battery_3_charging_status = Column(Integer, nullable=False)
    pcu_voltage = Column(Float, nullable=False)
    pcu_current = Column(Float, nullable=False)
    solar_voltage = Column(Float, nullable=False)
    solar_current = Column(Float, nullable=False)
    body_temperature = Column(Float, nullable=False)

class ShipSystem(Base):
    __tablename__ = 'ship_system'

    id = Column(Integer, primary_key=True, index=True)
    ship_id = Column(Integer, nullable=False)
    system_status = Column(Integer, nullable=False)
    total_operating_time = Column(Integer, nullable=False)
    current_operating_time = Column(Integer, nullable=False)
    cpu_usage = Column(Float, nullable=False)
    memory_usage = Column(Float, nullable=False)
    disk_usage = Column(Float, nullable=False)

class ShipMission(Base):
    __tablename__ = 'ship_missions'
    
    id = Column(Integer, primary_key=True, index=True)
    ship_id = Column(Integer, nullable=False)
    mission_area = Column(Integer, nullable=False)
    current_mode = Column(Integer, nullable=False)
    destination_latitude = Column(Float, nullable=False)
    destination_longitude = Column(Float, nullable=False)