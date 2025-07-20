from sqlalchemy.orm import Session
from . import models

def create_receipt(db: Session, vendor, date, amount, category):
    rec = models.Receipt(vendor=vendor, date=date, amount=amount, category=category)
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return rec

def get_all(db: Session):
    return db.query(models.Receipt).all()

def search_receipts(db: Session, vendor=None, date_from=None, date_to=None, amount_min=None, amount_max=None):
    q = db.query(models.Receipt)
    if vendor: q = q.filter(models.Receipt.vendor.contains(vendor))
    if date_from: q = q.filter(models.Receipt.date >= date_from)
    if date_to: q = q.filter(models.Receipt.date <= date_to)
    if amount_min is not None: q = q.filter(models.Receipt.amount >= amount_min)
    if amount_max is not None: q = q.filter(models.Receipt.amount <= amount_max)
    return q.all()
