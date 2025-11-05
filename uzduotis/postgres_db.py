from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from db_connection import get_db_settings

db_conn = get_db_settings()
db_url = db_conn.get_database_url()

database = Database(db_url)
metadata = MetaData()


events = Table (
  "events",
  metadata,
  Column("id", Integer, primary_key=True, index=True),
  Column("event_type", String, index=True),
  Column("event_payload", String, index=True),
)

engine = create_engine(db_url)
metadata.create_all(engine)