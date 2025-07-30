import streamlit as st
import requests

st.title("🧠 Fake Job Ad Detection")

# Input box for job ad text
job_text = st.text_area("Paste the full job advertisement text below:", height=200)

# Button to submit
if st.button("Check if Fake"):
    if job_text.strip() == "":
        st.warning("Please enter some job text.")
    else:
        # Send to FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={"text": job_text}
        )
        if response.status_code == 200:
            result = response.json()["prediction"]
            if result == "Fake":
                st.error("🚨 This job ad looks FAKE!")
            else:
                st.success("✅ This job ad looks REAL.")
        else:
            st.error("⚠️ Error: Could not connect to prediction server.")

