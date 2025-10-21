import pandas as pd
from sqlalchemy import create_engine
from catalog_service.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

# Import CSV data
venues_df = pd.read_csv("C:/Users/abdul/Desktop/BITS/Scalable Services_SEZG583/Assignments/Ass-1_PS-5/Datasets/etsr_venues.csv")
events_df = pd.read_csv("C:/Users/abdul/Desktop/BITS/Scalable Services_SEZG583/Assignments/Ass-1_PS-5/Datasets/etsr_events.csv")
venues_df.to_sql("venues", engine, if_exists="append", index=False)
events_df.to_sql("events", engine, if_exists="append", index=False)

print("Seed data imported successfully!")