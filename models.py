from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Venue(Base):
    __tablename__ = "venues"
    venue_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    city = Column(String(255))
    capacity = Column(Integer)
    events = relationship("Event", back_populates="venue")

class Event(Base):
    __tablename__ = "events"
    event_id = Column(Integer, primary_key=True, index=True)
    venue_id = Column(Integer, ForeignKey("venues.venue_id"))
    title = Column(String(255))
    event_type = Column(String(255))
    event_date = Column(DateTime)
    base_price = Column(Float)
    status = Column(String(255))
    venue = relationship("Venue", back_populates="events")