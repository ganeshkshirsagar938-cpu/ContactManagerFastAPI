from sqlalchemy import Column, Integer, String
from ..core.database import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=True)
    phone = Column(String(30), Nullable=True)
    address = Column(String(255), nullable=True)

