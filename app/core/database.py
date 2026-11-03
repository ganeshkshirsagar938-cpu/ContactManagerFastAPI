from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os

database_url = os.getenv("DATABASE_URL","mysql+pymysql://root:root@localhost:3306/ContactManagerDB")


engine = create_engine(database_url)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def getDatabase():

    db = LocalSession()

    try:
        yield db

    finally:
        db.close()


Base = declarative_base()