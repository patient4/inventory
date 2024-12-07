from sqlalchemy import Column, Integer, String, Float
from db.connection import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
