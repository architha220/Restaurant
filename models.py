from database import Base
from sqlalchemy import Column, Integer, String


class customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, nullable=False, primary_key=True)


class order(Base):
    __tablename__ = "orders"

    order_item = Column(Integer, nullable=False, primary_key=True)
    customer_id = Column(Integer, nullable=False,primary_key=True)
    item = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    bill = Column(Integer, nullable=False)