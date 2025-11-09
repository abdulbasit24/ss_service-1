import requests
from typing import Optional, List
from sqlalchemy.orm import Session
from models import Venue, Event
from schemas import VenueCreate, EventCreate
from fastapi import HTTPException
from sqlalchemy import func
import models


def create_venue(db: Session, venue: VenueCreate):
    db_venue = Venue(**venue.dict())
    db.add(db_venue)
    db.commit()
    db.refresh(db_venue)
    return db_venue

def get_venues(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Venue).offset(skip).limit(limit).all()

def get_venue(db: Session, venue_id: int):
    return db.query(Venue).filter(Venue.venue_id == venue_id).first()

def update_venue(db: Session, venue_id: int, venue: VenueCreate):
    db_venue = get_venue(db, venue_id)
    if db_venue:
        for key, value in venue.dict().items():
            setattr(db_venue, key, value)
        db.commit()
        db.refresh(db_venue)
    return db_venue

def delete_venue(db: Session, venue_id: int):
    db_venue = get_venue(db, venue_id)
    if db_venue:
        db.delete(db_venue)
        db.commit()
    return db_venue

def create_event(db, event):
    db_event = models.Event(
        venue_id=event.venue_id,
        title=event.title,
        event_type=event.event_type,
        event_date=event.event_date,
        base_price=event.base_price,
        status=event.status
    )
    db.add(db_event)
    db.commit()          # ✅ commit before refresh
    db.refresh(db_event) # ✅ will now have event_id assigned
    return db_event



def get_events(db: Session, city: Optional[str] = None, 
               event_type: Optional[str] = None,
               status: Optional[str] = None,
               skip: int = 0, limit: int = 100):

    query = db.query(Event)

    if city:
        query = query.join(Venue).filter(Venue.city.ilike(f"%{city}%"))

    if event_type:
        query = query.filter(Event.event_type.ilike(f"%{event_type}%"))

    if status:
        query = query.filter(Event.status == status)

    return query.offset(skip).limit(limit).all()


def get_event(db: Session, event_id: int):
    return db.query(Event).filter(Event.event_id == event_id).first()

def update_event(db: Session, event_id: int, event: EventCreate):
    db_event = get_event(db, event_id)
    if db_event:
        for key, value in event.dict().items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
    return db_event

def delete_event(db: Session, event_id: int):
    db_event = get_event(db, event_id)
    if db_event:
        db.delete(db_event)
        db.commit()
    return db_event

# In-Future Service
'''
def create_order(db: Session, order: OrderCreate):
    # Verify event from Catalog
    catalog_url = "http://catalog-service:8000/v1/events/{event_id}"  # Use service name in Docker
    response = requests.get(catalog_url.format(event_id=order.event_id))
    if response.status_code != 200 or response.json()["status"] != "ON_SALE":
        raise HTTPException(status_code=400, detail="Event not available")
    # Proceed with order creation...
'''