# create_db.py
from sqlalchemy import create_engine
from database import DATABASE_URL, Base
from models import *

def create_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_database()
