import pandas as pd
from sqlalchemy import create_engine

# ✅ Database connection (Kubernetes service name)
engine = create_engine("mysql+pymysql://root:admin@catalog-db:3306/catelog_db")

# ✅ Read CSV files directly from /app/
venues_df = pd.read_csv("etsr_venues.csv")
events_df = pd.read_csv("etsr_events.csv")

# ✅ Insert into MySQL tables
venues_df.to_sql("venues", con=engine, if_exists="append", index=False)
events_df.to_sql("events", con=engine, if_exists="append", index=False)

print(f"✅ Inserted {len(venues_df)} venues and {len(events_df)} events successfully!")
