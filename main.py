from fastapi import FastAPI
from routers import venues, events
from database import engine
from models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Catalog Service")

app.include_router(venues.router, prefix="/v1")
app.include_router(events.router, prefix="/v1")

