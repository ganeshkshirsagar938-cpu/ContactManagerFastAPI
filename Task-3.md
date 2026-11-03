# Create Database Configuration File
1. create new file inside core folder with the name database.py

```python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os

database_url = os.getenv("DATABASE_URL","mysql+pymysql://root:root@localhost:3306/contactManagerDB")
engine = create_engine(database_url)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def getDatabase():

    db = LocalSession()

    try:
        yield db
        
    finally:
        db.close()


Base = declarative_base()
```

2. Create the contact model (Represent Database Table)
inside model folder, create one file with name contact.py

```python
from sqlalchemy import Column, Integer, String
from ..core.database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(30), nullable=True)
    address = Column(String(255), nullable=True)

```