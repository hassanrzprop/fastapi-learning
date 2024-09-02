# creating connection with database
from sqlmodel import create_engine,SQLModel #type: ignore
import os
connection_string=os.getenv("DB_URL") # this is used to create connection with database using connection string
engine=create_engine(connection_string)

def create_tables(): # this function is used actually to create tables in database which we run in start functiojn in main.py file in start function
    SQLModel.metadata.create_all(engine)