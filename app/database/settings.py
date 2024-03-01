from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USERNAME = None
PASSWORD = None
HOST = None
DBNAME = None

DATABASE_URL = "mysql+mysqlconnector://{}:{}@{}/{}".format(USERNAME, PASSWORD, HOST, DBNAME)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()