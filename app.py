import os
import requests
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# APPP TITLE
# -----------------------------
st.set_page_config(page_title="Rock Paper Scissors Classifier", page_icon="✌️")

st.markdown("<h2 style='text-align: left; font-size: 40px;'>✊🖐️✌️ Rock-Paper-Scissor App</h2>",unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; font-size: 25px;'>An AI Hand Gesture classifier</h3>",unsafe_allow_html=True)

st.write("ℹ️ Machine learning powered app to recognizes and predicts hand gestures in images.")

st.write("💡 Upload below an image of a hand gesture and let the model predict what it is:")

# -----------------------------
# API SETUP
# -----------------------------
PRED_ENDPOINT = "http://localhost:8000/predict"  # FastAPI running in Docker

# -----------------------------
# SIDEBY-SIDE LAYOUT
# -----------------------------
col_left, col_right = st.columns([1, 2])

with col_left:
    uploaded = st.file_uploader("", type=["jpg", "jpeg", "png"])
    run_prediction = False

    if uploaded:
        st.image(uploaded, caption="Preview", use_container_width=True)
        if st.button("🎯 Predict"):
            run_prediction = True

with col_right:
    if uploaded and run_prediction:
        with st.spinner("🤖 Analyzing your image..."):
            try:
                img_bytes = uploaded.getvalue()
                content_type = uploaded.type or "image/jpeg"
                files = {"file": (uploaded.name, img_bytes, content_type)}

                response = requests.post(PRED_ENDPOINT, files=files, timeout=20)
                response.raise_for_status()
                data = response.json()

                label = data.get("label", "Unknown")
                confidence = data.get("confidence", None)
                probs = data.get("probabilities", {})

            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ API call failed: {e}")
                data, label, confidence, probs = None, None, None, None

        # -----------------------------
        # SHOW RESULT + PIE CHART
        # -----------------------------

        if data:
            st.markdown("---")
            st.markdown("<h3 style='text-align:center'> 🎯 Prediction Result 🎯</h3>", unsafe_allow_html=True)
            st.markdown("---")

        if isinstance(probs, dict) and probs:
            series = pd.Series(probs)
            top_label = series.idxmax()
            top_conf = series.max()

            st.markdown(f"<h2 style='text-align:center; color:green; font-size:40px;'>{top_label.upper()}</h2>", unsafe_allow_html=True )

            st.markdown(f"<h3 style='text-align:center; color:gray;'>Confidence: {top_conf:.1%}</h3>", unsafe_allow_html=True )

        else:
            st.write("⚠️ No probability data returned.")
