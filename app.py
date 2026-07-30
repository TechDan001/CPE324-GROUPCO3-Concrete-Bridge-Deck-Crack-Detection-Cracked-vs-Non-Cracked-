import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image


st.set_page_config(
    page_title="Concrete Crack Detector",
    page_icon="🔧",
    layout="centered",
)


st.title("Concrete Surface Crack Detector")
st.subheader("Concrete Bridge Deck Crack Detection (Cracked vs Non-Cracked)")
st.caption("Upload an image of a concrete surface to analyze it for structural cracks.")
st.divider()


@st.cache_resource
def load_model():
    return tf.keras.models.load_model("mobilenetv3_transfer.keras")

model = load_model()


def predict(model, pil_image):
    img = pil_image.convert("RGB").resize((128, 128))
    arr = np.expand_dims(np.array(img, dtype=np.float32), axis=0)
    preds = model.predict(arr, verbose=0)[0]
    
    # Class mapping based on alphabetical folder order:
    # Index 0: 'Negative' (No Crack)
    # Index 1: 'Positive' (Crack)
    prob_negative = float(preds[0])
    prob_positive = float(preds[1])
    

    if prob_positive >= prob_negative:
        label = "Crack Detected"
    else:
        label = "No Crack (Clean)"
        
    return label, prob_positive, prob_negative


uploaded_file = st.file_uploader("Choose a concrete image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    

    st.image(img, caption="Uploaded Surface", width=350)
    
    if st.button("Analyze Surface", type="primary"):
        with st.spinner("Scanning for anomalies..."):
            label, prob_positive, prob_negative = predict(model, img)
            

        if label == "Crack Detected":
            st.error(f"Result: **{label}**")
        else:
            st.success(f"Result: **{label}**")
        
        st.divider()
        

        st.write("### Analysis Breakdown")
        col1, col2 = st.columns(2)
        

        with col1:
            st.metric(label="Cracked (Positive)", value=f"{prob_positive * 100:.2f}%")
            st.progress(prob_positive)
            
        with col2:
            st.metric(label="Clean (Negative)", value=f"{prob_negative * 100:.2f}%")
            st.progress(prob_negative)
