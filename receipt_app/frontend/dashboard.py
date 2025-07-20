import streamlit as st
import pandas as pd
import requests

BASE = "http://localhost:8000"

st.set_page_config("📥 Receipt Analyzer", layout="wide")

st.title("📄 Receipt Analyzer with OCR & Stats")

tab1, tab2 = st.tabs(["📤 Upload & View", "📊 Analytics"])

with tab1:
    uploaded = st.file_uploader("Upload receipt (.jpg/.png/.pdf)", type=["jpg", "jpeg", "png", "pdf"])
    if uploaded:
        files = {"file": uploaded}
        r = requests.post(f"{BASE}/upload/", files=files)
        if r.ok:
            st.success("✅ Uploaded!")
            st.json(r.json())
        else:
            st.error("❌ " + r.json().get("detail", "Unknown error"))

    st.divider()
    if st.button("🔁 Refresh Records"):
        df = pd.DataFrame(requests.get(f"{BASE}/receipts/").json())
        if df.empty:
            st.warning("No data yet.")
        else:
            st.subheader("🧾 All Parsed Receipts")
            st.dataframe(df, use_container_width=True)
            if st.download_button("⬇️ Export CSV", df.to_csv(index=False), file_name="receipts.csv"):
                st.success("Exported!")

with tab2:
    df = pd.DataFrame(requests.get(f"{BASE}/receipts/").json())
    if df.empty:
        st.info("No data to analyze yet.")
    else:
        df['date'] = pd.to_datetime(df['date'])

        col1, col2, col3 = st.columns(3)
        col1.metric("💰 Total Spent", f"₹{df['amount'].sum():,.2f}")
        col2.metric("📈 Average", f"₹{df['amount'].mean():,.2f}")
        col3.metric("🔢 Median", f"₹{df['amount'].median():,.2f}")

        st.subheader("🛍️ Top Vendors")
        st.bar_chart(df['vendor'].value_counts())

        st.subheader("📅 Monthly Trend")
        monthly = df.set_index('date').resample("M")['amount'].sum()
        st.line_chart(monthly)

res = requests.get(f"{BASE}/receipts/")
if res.ok:
    data = res.json()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.warning("No receipts found.")
else:
    st.error("Backend error!")
    st.write("Response Code:", res.status_code)
    st.write("Message:", res.text)
