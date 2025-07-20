import os
import re
import io
import datetime
from pathlib import Path
from dotenv import load_dotenv
import pytesseract
from PIL import Image, ImageOps
import fitz  # PyMuPDF

# ✅ Load environment variables (robust absolute path)
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

# ✅ Set tesseract path from .env or fallback to hardcoded path
tess_path = os.getenv("TESSERACT_PATH") or r'C:\Users\abhay\Desktop\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tess_path

# ✅ Load image (from bytes) with PDF and image support
def load_image(file_bytes: bytes, content_type: str) -> Image.Image:
    if content_type == "application/pdf":
        doc = fitz.open("pdf", file_bytes)
        pix = doc[0].get_pixmap()
        return Image.open(io.BytesIO(pix.tobytes("png")))
    return Image.open(io.BytesIO(file_bytes))

# ✅ Preprocess image (grayscale + orientation fix)
def preprocess_image(image: Image.Image) -> Image.Image:
    image = ImageOps.exif_transpose(image)
    return image.convert("L")

# ✅ OCR text extraction
def extract_text(image: Image.Image) -> str:
    return pytesseract.image_to_string(image)

# ✅ Vendor parsing logic
def parse_vendor(text: str) -> str:
    for line in text.splitlines():
        if len(line.strip()) > 3:
            return line.strip().title()
    return "Unknown Vendor"

# ✅ Amount parsing logic
def parse_amount(text: str) -> float | None:
    lines = text.lower().splitlines()
    for line in reversed(lines):
        if any(key in line for key in ["total", "amount", "paid", "balance"]):
            match = re.search(r"(\d+[.,]\d{2})", line)
            if match:
                return float(match.group(1).replace(",", ""))
    all_nums = re.findall(r"(\d+[.,]\d{2})", text)
    if all_nums:
        return float(all_nums[-1].replace(",", ""))
    return None

# ✅ Date parsing logic
def parse_date(text: str) -> datetime.date:
    for pattern in [r"\d{2}/\d{2}/\d{4}", r"\d{4}-\d{2}-\d{2}"]:
        match = re.search(pattern, text)
        if match:
            try:
                return datetime.datetime.strptime(match.group(), "%d/%m/%Y").date()
            except:
                try:
                    return datetime.datetime.strptime(match.group(), "%Y-%m-%d").date()
                except:
                    pass
    return datetime.date.today()
