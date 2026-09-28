from fastapi import FastAPI
from pydantic import BaseModel
from mysql.connector import connect
from models import customer,order
from database import Base,engine,LocalSession

app = FastAPI()

Base.metadata.create_all(bind=engine)


class CustomerRequest(BaseModel):
    customer_id: int


class OrderRequest(BaseModel):
    order_item: int
    customer_id: int
    item: str
    price: int
    quantity: int


@app.get("/")
def home():
    return "This is home page"


@app.post("/add_customer")
def add_customer(request: CustomerRequest):

    customer_id = request.customer_id

    customer_details = customer(
        customer_id=customer_id
    )

    db = LocalSession()

    db.add(customer_details)
    db.commit()
    db.close()

    return "Customer added Successfully"


@app.post("/take_order")
def take_order(request: OrderRequest):

    order_item = request.order_item
    customer_id = request.customer_id
    item = request.item
    price = request.price
    quantity = request.quantity

    bill = price * quantity

    db = LocalSession()

    new_order = order(
        order_item=order_item,
        customer_id=customer_id,
        item=item,
        price=price,
        quantity=quantity,
        bill=bill
    )

    db.add(new_order)
    db.commit()
    db.close()

    return "Order taken successfully"


@app.get("/get_orders")
def get_orders():

    db = LocalSession()

    orders = db.query(order).all()

    db.close()

    return orders


@app.get("/calculate_bill")
def calculate_bill(customer_id: int):

    db = LocalSession()

    orders = db.query(order).filter(
        order.customer_id == customer_id
    ).all()

    total_bill = 0

    for item in orders:
        total_bill = total_bill + item.bill

    db.close()

    return {
        "customer_id": customer_id,
        "total_bill": total_bill
    }