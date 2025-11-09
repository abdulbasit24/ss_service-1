from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas import VenueCreate, VenueResponse
from crud import create_venue, get_venues, get_venue, update_venue, delete_venue

router = APIRouter()

@router.post("/venues", response_model=VenueResponse)
def create_venue_endpoint(venue: VenueCreate, db: Session = Depends(get_db)):
    return create_venue(db, venue)

@router.get("/venues", response_model=List[VenueResponse])
def read_venues_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_venues(db, skip, limit)

@router.get("/venues/{venue_id}", response_model=VenueResponse)
def read_venue_endpoint(venue_id: int, db: Session = Depends(get_db)):
    venue = get_venue(db, venue_id)
    if venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue

@router.put("/venues/{venue_id}", response_model=VenueResponse)
def update_venue_endpoint(venue_id: int, venue: VenueCreate, db: Session = Depends(get_db)):
    updated_venue = update_venue(db, venue_id, venue)
    if updated_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return updated_venue

@router.delete("/venues/{venue_id}")
def delete_venue_endpoint(venue_id: int, db: Session = Depends(get_db)):
    deleted_venue = delete_venue(db, venue_id)
    if deleted_venue is None:
        raise HTTPException(status_code=404, detail="Venue not found")
    return {"detail": "Venue deleted"}