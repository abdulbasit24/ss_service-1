from fastapi import FastAPI
from catalog_service.routers import venues, events
from catalog_service.database import engine
from catalog_service.models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Catalog Service")

app.include_router(venues.router, prefix="/v1")
app.include_router(events.router, prefix="/v1")

