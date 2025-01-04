from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Ship(Base):
    __tablename__ = "ships"

    id = Column(Integer, primary_key=True, index=True)
    manufacturing_date = Column(Date)
    model_number = Column(String(255))
    software_version = Column(String(255))
    network_interface_info = Column(String(255)) 