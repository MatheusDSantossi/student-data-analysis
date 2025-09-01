import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_connection():

    try:
        
        conn = psycopg2.connect(
            database="testqueries",
            user="postgres",
            password=os.getenv("POSTGRES_PASSWORD"),
            host="localhost",  # e.g., 'localhost' or an IP address
            port="5432"   
        )
        
        db_connection_str = f'postgresql+psycopg2://postgres:{os.getenv("POSTGRES_PASSWORD")}@localhost:5432/testqueries'
        
        
        engine = create_engine(db_connection_str)
    except psycopg2.OperationalError as err:
        print(f"Error conecting to the database: {err}")


    return conn, engine
