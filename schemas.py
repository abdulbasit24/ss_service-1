from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class VenueBase(BaseModel):
    name: str
    city: str
    capacity: int

class VenueCreate(VenueBase):
    pass

class VenueResponse(VenueBase):
    venue_id: int

    class Config:
        from_attributes = True

class EventBase(BaseModel):
    venue_id: int
    title: str
    event_type: str
    event_date: datetime
    base_price: float
    status: str

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    event_id: int

    class Config:
        from_attributes = True