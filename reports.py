from database import SessionLocal
from models import Order, Payment
import csv, json
from openpyxl import Workbook

def export_csv(filename):
    db = SessionLocal()
    orders = db.query(Order).all()
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "client_id", "project_name", "status"])
        for o in orders:
            writer.writerow([o.id, o.client_id, o.project_name, o.status])
    db.close()

def export_json(filename):
    db = SessionLocal()
    payments = db.query(Payment).all()
    data = [{"id": p.id, "order_id": p.order_id, "amount": p.amount} for p in payments]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    db.close()

def export_excel(filename):
    db = SessionLocal()

    payments = db.query(Payment).all()

    wb = Workbook()
    ws_payments = wb.active
    ws_payments.title = "Payments"
    ws_payments.append(["id", "order_id", "amount"])

    for payment in payments:
        ws_payments.append([payment.id, payment.order_id, payment.amount])

    wb.save(filename)
    db.close()
