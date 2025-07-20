
# 🧾 Receipt Summarizer App

An intelligent full-stack application for automatically parsing and analyzing receipts or bills using OCR, native algorithms, and lightweight infrastructure. Built for automation, insights, and extensibility — this project delivers real-world utility with clean architecture and deep algorithmic thought.

---

## 🚀 What It Does

Upload a receipt (JPG, PNG, or PDF) and instantly:
- 🔍 Extracts **vendor name**, **billing date**, and **amount**
- 📊 Aggregates data for:
  - Total spend
  - Vendor frequency
  - Monthly spending trends
- 💾 Stores all parsed data in a relational database
- 📈 Visualizes stats on an interactive dashboard

Powered by **FastAPI**, **Tesseract OCR**, and **Streamlit**, it applies real algorithmic thinking to real-world data extraction.

---

## 🎯 Why This Project Stands Out

| Feature                        | Implementation                                         |
|-------------------------------|--------------------------------------------------------|
| 🔎 High-quality OCR            | Tesseract OCR with preprocessing (OpenCV + PIL)       |
| 🧠 Smart Parsing               | Rule-based date/amount/vendor extraction with fallback|
| 🧮 Algorithmic Thinking        | Native searching, sorting (Timsort, Regex), Aggregation|
| 💡 Insightful Visualizations   | Bar charts, line plots, and categorical analysis      |
| 🛠️ Fully Modular Architecture | Streamlit frontend + FastAPI backend + SQLite DB      |
| 📦 Portable & Lightweight      | No external services, deploy anywhere with Python     |



## 🧱 System Architecture


     ┌──────────────┐        ┌──────────────┐
     │   Streamlit  │ ─────▶ │   FastAPI    │
     │   Frontend   │        │   Backend    │
     └──────┬───────┘        └──────┬───────┘
            │                       │
            ▼                       ▼
     Receipt Uploads           Tesseract OCR
    User Search Queries     Rule-Based Parsers
            │                       │
            ▼                       ▼
       📊 Dashboard             📂 SQLite DB




## 📂 Folder Structure


receipt_app/
├── backend/
│   ├── api.py           # FastAPI routes
│   ├── crud.py          # DB logic
│   ├── database.py      # SQLAlchemy setup
│   ├── models.py        # Pydantic & ORM models
│   └── ocr_utils.py     # OCR + text parsing
│
├── frontend/
│   └── dashboard.py     # Streamlit interface
│
├── .env                 # Tesseract path
├── requirements.txt     # All Python dependencies
├── README.md            # You’re reading this!
└── .gitignore
```

---

## 🛠️ Installation & Run Instructions

### 1. 🔧 Clone the Repo

```bash
git clone https://github.com/Abhay-gk/receipt_app.git
cd receipt_app
```

### 2. 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### 3. 🧠 Install Tesseract OCR

* Download from: [Tesseract for Windows (UB Mannheim)](https://github.com/UB-Mannheim/tesseract/wiki)
* Save path (e.g. `C:\Users\abhay\Desktop\Tesseract-OCR\tesseract.exe`) to `.env`:

```env
TESSERACT_PATH=C:\Users\abhay\Desktop\Tesseract-OCR\tesseract.exe
```

### 4. 🚀 Run the App

Start backend (FastAPI):

```bash
uvicorn backend.api:app --reload
```

Start frontend (Streamlit):

```bash
streamlit run frontend/dashboard.py
```

---

## 📊 Features & Algorithms

### ✅ Core Capabilities

* 🔍 OCR from images or PDFs using Tesseract
* 📤 Upload interface for receipts
* 💾 Data stored using SQLite (via SQLAlchemy ORM)
* 🔎 Search by vendor, date, or amount
* 📈 Aggregations: total spend, average, histogram
* 📅 Time-series spend trend analysis

### 🧠 Algorithms Implemented

| Type         | Logic Used                                |
| ------------ | ----------------------------------------- |
| Search       | Linear + keyword match (case-insensitive) |
| Sort         | Timsort (via Pandas)                      |
| Aggregation  | Native Python + Pandas stats              |
| Parsing      | Regex, rule-based inference               |
| OCR Boosting | Grayscale + EXIF correction               |

---

## 🙋‍♂️ User Journey

1. User launches app via Streamlit
2. Uploads receipt (image or PDF)
3. Backend extracts and parses info using OCR
4. Data saved and visualized instantly
5. User filters/searches + downloads summary

---

## ❗ Limitations

* OCR accuracy depends on image quality
* No support for multi-page PDF receipts
* No login/auth system (single-user mode)
* No multilingual support yet

---

## 🔮 Future Work

* 🈳 Multilingual parsing (e.g., Hindi, Kannada)
* 👤 User-level authentication
* 📤 Export as Excel or JSON
* 📸 Webcam scanning mode
* ☁️ Deployment on Railway/Render

---

## 📃 License

This project is open-sourced under the [MIT License](LICENSE).

---

## 👋 About the Author

Made with ❤️ by **Abhay G K**
A full-stack enthusiast, data wrangler, and algorithmic thinker.

🔗 [GitHub](https://github.com/Abhay-gk)

---

> *"Turning messy receipts into structured insights, one scan at a time."*



