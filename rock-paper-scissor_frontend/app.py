import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Rock Paper Scissors Classifier", page_icon="✌️")
st.title("🪨📄✂️ Rock Paper Scissors Classifier")

st.write("Upload an image of a hand gesture and let the model predict what it is!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):
        with st.spinner("Sending image to backend..."):
            # Convert image to bytes
            buf = io.BytesIO()
            image.save(buf, format="PNG")
            buf.seek(0)

            files = {"file": ("image.png", buf, "image/png")}
            try:
                response = requests.post("http://localhost:8000/predict", files=files)
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"**Prediction:** {result['label']} ({result['confidence']:.2%})")
                    st.json(result["probabilities"])
                else:
                    st.error(f"Backend error: {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
