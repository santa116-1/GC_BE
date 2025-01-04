from pydantic import BaseModel
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