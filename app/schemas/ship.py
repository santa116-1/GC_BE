from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ShipBase(BaseModel):
    manufacturing_date: date
    model_number: str
    software_version: str
    network_interface_info: str

class Ship(ShipBase):
    id: int

    class Config:
        from_attributes = True 

# Telemetry Data Schema
class TelemetryDataBase(BaseModel):
    ship_id: int
    thruster_output: float
    thruster_rotation_speed: float
    thruster_voltage: float
    thruster_current: float
    battery_1_remaining: int
    battery_1_voltage: float
    battery_1_charging_status: int
    battery_2_remaining: int
    battery_2_voltage: float
    battery_2_charging_status: int
    battery_3_remaining: int
    battery_3_voltage: float
    battery_3_charging_status: int
    pcu_voltage: float
    pcu_current: float
    solar_voltage: float
    solar_current: float
    body_temperature: float

class TelemetryDataCreate(TelemetryDataBase):
    pass

class TelemetryDataResponse(TelemetryDataBase):
    id: int

    class Config:
        orm_mode = True

# Systems Data Schema
class SystemDataBase(BaseModel):
    ship_id: int = Field(..., example=1)
    system_status: int = Field(..., example=1)
    total_operating_time: int = Field(..., example=695)
    current_operating_time: int = Field(..., example=578)
    cpu_usage: float = Field(..., example=58.0)
    memory_usage: float = Field(..., example=39.0)
    disk_usage: float = Field(..., example=48.0)

class SystemDataCreate(SystemDataBase):
    pass

class SystemDataUpdate(BaseModel):
    ship_id: Optional[int] = Field(None, example=1)
    system_status: Optional[int] = Field(None, example=1)
    total_operating_time: Optional[int] = Field(None, example=695)
    current_operating_time: Optional[int] = Field(None, example=578)
    cpu_usage: Optional[float] = Field(None, example=58.0)
    memory_usage: Optional[float] = Field(None, example=39.0)
    disk_usage: Optional[float] = Field(None, example=48.0)

class SystemDataRead(SystemDataBase):
    id: int

    class Config:
        orm_mode = True

# Ship Mission Data Schema
class ShipMissionBase(BaseModel):
    ship_id: int = Field(..., example=1)
    mission_area: int = Field(..., example=2)
    current_mode: int = Field(..., example=3)
    destination_latitude: float = Field(..., example=35.288)
    destination_longitude: float = Field(..., example=139.507)


class ShipMissionCreate(ShipMissionBase):
    pass


class ShipMissionUpdate(BaseModel):
    ship_id: Optional[int] = Field(None, example=1)
    mission_area: Optional[int] = Field(None, example=2)
    current_mode: Optional[int] = Field(None, example=3)
    destination_latitude: Optional[float] = Field(None, example=35.288)
    destination_longitude: Optional[float] = Field(None, example=139.507)


class ShipMissionRead(ShipMissionBase):
    id: int

    class Config:
        orm_mode = True