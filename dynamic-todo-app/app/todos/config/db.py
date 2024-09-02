# creating connection with database
from sqlmodel import create_engine,SQLModel #type: ignore
import os
connection_string=os.getenv("DB_URL")
engine=create_engine(connection_string)

def create_tables():
    SQLModel.metadata.create_all(engine)