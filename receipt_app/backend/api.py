from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from .database import SessionLocal
from .crud import create_receipt, get_all
from .models import ReceiptCreate
from .ocr_utils import load_image, preprocess_image, extract_text, parse_amount, parse_date, parse_vendor
from sqlalchemy.orm import Session
import os

app = FastAPI()

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Upload receipt (image/pdf) endpoint
@app.post("/upload/")
async def upload(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # ✅ Validate file by extension, not MIME type
        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in [".jpg", ".jpeg", ".png", ".pdf"]:
            raise HTTPException(status_code=400, detail=f"Unsupported file extension: {ext}")

        # Process the file (image or first page of PDF)
        image = load_image(await file.read(), file.content_type)
        image = preprocess_image(image)
        text = extract_text(image)

        # Extract data
        vendor = parse_vendor(text)
        amount = parse_amount(text)
        date = parse_date(text)

        # Validate amount
        if amount is None:
            raise HTTPException(status_code=400, detail="Amount not found in receipt")

        # Save to DB
        rc = ReceiptCreate(vendor=vendor, date=date, amount=amount)
        receipt = create_receipt(db, rc.vendor, rc.date, rc.amount, rc.category)

        return {
            "id": receipt.id,
            "vendor": receipt.vendor,
            "amount": receipt.amount,
            "date": str(receipt.date)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get all receipts
@app.get("/receipts/")
def list_receipts(db: Session = Depends(get_db)):
    data = get_all(db)
    return jsonable_encoder(data)
