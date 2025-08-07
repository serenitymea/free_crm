from models import Client, Order, Payment
from database import SessionLocal

def add_client(name, email, phone):
    db = SessionLocal()
    client = Client(name=name, email=email, phone=phone)
    db.add(client)
    db.commit()
    db.close()

def add_order(client_id, project_name, status, deadline):
    db = SessionLocal()
    order = Order(client_id=client_id, project_name=project_name, status=status, deadline=deadline)
    db.add(order)
    db.commit()
    db.close()

def add_payment(order_id, amount):
    db = SessionLocal()
    payment = Payment(order_id=order_id, amount=amount, paid=True)
    db.add(payment)
    db.commit()
    db.close()