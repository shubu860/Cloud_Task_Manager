# import create_engine
from sqlalchemy import create_engine
import os
# import sessionmaker
from sqlalchemy.orm import sessionmaker

# import declarative_base
from sqlalchemy.orm import declarative_base

# copy this from neon and replace the username , password , and host with your own credentials 
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
# here , we are connecting to a PostgreSQL database hosted on the cloud(neon)

# note : click , "Show Password" and copy the complete connection string

# create SQLAlchemy engine
# the engine is responsible for connecting FastAPI with the cloud PostgreSQL database
engine = create_engine(DATABASE_URL)

# create sessions as every database operation will use this session
SessionLocal = sessionmaker(bind= engine)

# base class as all database tables will inherit from this class
Base = declarative_base()

# dependency injection , this function provides a database 

def get_db():

    db = SessionLocal()

    try :

        yield db

    finally:

        db.close()
