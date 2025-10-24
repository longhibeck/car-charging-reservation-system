from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True)
    license_plate = Column(String, unique=True)
    model = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="cars")
