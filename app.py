import os
import random
import requests
import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

from rock_paper_scissor.model import predict_image


# -----------------------------
# APP TITLE
# -----------------------------
st.set_page_config(page_title="Rock Paper Scissors Classifier", page_icon="✌️")

st.markdown("<h2 style='text-align: left; font-size: 40px;'>✊🖐️✌️ Rock-Paper-Scissor App</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: left; font-size: 25px;'>An AI Hand Gesture classifier</h3>", unsafe_allow_html=True)

st.write("🎮 Upload a photo of your hand (Rock, Paper, or Scissors) and challenge the computer to a quick match!")



# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
EMOJI_MAP = {"rock": "✊", "paper": "🖐️", "scissor": "✌️"}

def get_emoji(label: str) -> str:
    """Return the emoji for a given label."""
    return EMOJI_MAP.get(label.lower(), "❓")

def get_computer_choice():
    """Return random computer choice."""
    return random.choice(list(EMOJI_MAP.keys()))

def determine_winner(user, computer):
    """Decide who wins the game."""
    if user == computer:
        return "🤝 It's a tie!"
    if (
        (user == "rock" and computer == "scissor")
        or (user == "paper" and computer == "rock")
        or (user == "scissor" and computer == "paper")
        ):
        return f"🎉 YOU WIN! {get_emoji(user)} beats {get_emoji(computer)}"
    else:
        return f"💻 COMPUTER WINS! {get_emoji(computer)} beats {get_emoji(user)}"


# -----------------------------
# SIDEBY-SIDE LAYOUT
# -----------------------------
col_left, col_right = st.columns([1, 2])

with col_left:
    uploaded = st.file_uploader("", type=["jpg", "jpeg", "png"])
    run_prediction = False

    if uploaded:
        st.image(uploaded, caption="Preview", use_container_width=True)
        if st.button("▶️ Play!"):
            run_prediction = True

with col_right:
    if uploaded and run_prediction:
        with st.spinner("🤖 Analyzing your image..."):
            try:
                image = Image.open(uploaded)
                data = predict_image(image)

                label = data.get("label", "Unknown").lower()
                probs = data.get("probabilities", {})
                confidence = data.get("confidence", 0.0)

            except Exception as e:
                st.error(f"⚠️ Prediction failed: {e}")
                data, label, probs = None, None, None

        if data:
            st.markdown("---")
            st.markdown("<h4 style='text-align:center'>🧑‍💻 USER vs. COMPUTER 💻</h3>", unsafe_allow_html=True)
            #st.markdown("---")

            # Prepare result layout
            col_user, col_comp = st.columns(2)

            # USER SIDE
            with col_user:
                if label in EMOJI_MAP:
                    st.markdown("<h4 style='text-align:center;'>You</h4>", unsafe_allow_html=True)
                    st.markdown(f"<h3 style='text-align:center; color:green;'>{get_emoji(label)} {label.upper()}</h2>", unsafe_allow_html=True)
                    st.markdown(f"<h7 style='text-align:center; color:gray;'>(Confidence: {confidence:.1%})</h3>", unsafe_allow_html=True )

            # COMPUTER SIDE
            with col_comp:
                comp_choice = get_computer_choice()
                st.markdown("<h4 style='text-align:center;'>Computer</h4>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='text-align:center; color:red;'>{get_emoji(comp_choice)} {comp_choice.upper()}</h2>", unsafe_allow_html=True)
                st.markdown(f"<h7 style='text-align:center; color:gray;'>(Randomly chosen)</h3>", unsafe_allow_html=True )

            # FINAL RESULT
            st.markdown("---")
            result = determine_winner(label, comp_choice)
            st.markdown(
                f"""
                <div style="
                    border: 2px solid #333;
                    border-radius: 10px;
                    background-color: #1E1E1E;
                    padding: 15px;
                    text-align: center;
                ">
                    <h4 style='color:white;'>{result}</h3>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown("---")
