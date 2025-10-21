from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from catalog_service.database import get_db
from catalog_service.schemas import EventCreate, EventResponse
from catalog_service.crud import create_event, get_events, get_event, update_event, delete_event

router = APIRouter()

@router.post("/events", response_model=EventResponse)
def create_event_endpoint(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event)

@router.get("/events", response_model=List[EventResponse])
def read_events_endpoint(
    city: Optional[str] = Query(None, description="Filter by city"),
    type: Optional[str] = Query(None, description="Filter by event_type"),
    status: Optional[List[str]] = Query(None, description="Filter by status (ON_SALE, SOLD_OUT, CANCELLED)"),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_events(db, city, type, status, skip, limit)

@router.get("/events/{event_id}", response_model=EventResponse)
def read_event_endpoint(event_id: int, db: Session = Depends(get_db)):
    event = get_event(db, event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.put("/events/{event_id}", response_model=EventResponse)
def update_event_endpoint(event_id: int, event: EventCreate, db: Session = Depends(get_db)):
    updated_event = update_event(db, event_id, event)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event

@router.delete("/events/{event_id}")
def delete_event_endpoint(event_id: int, db: Session = Depends(get_db)):
    deleted_event = delete_event(db, event_id)
    if deleted_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"detail": "Event deleted"}