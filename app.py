import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="DentalMate",
    page_icon="🦷",
    layout="wide"
)

# Title
st.title("🦷 DentalMate")
st.write("Dental Condition Detection & Instance Segmentation")

# Load model
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

st.success("✅ DentalMate model loaded successfully")

# Upload image
uploaded_file = st.file_uploader(
    "Upload a Dental X-ray image",
    type=["jpg", "jpeg", "png"]
)

# Confidence threshold
confidence = st.slider(
    "Confidence Threshold",
    0.05,
    0.95,
    0.25,
    0.05
)

# Prediction
if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Original Image")
    st.image(image, use_container_width=True)

    with st.spinner("🔍 Analyzing image..."):

        results = model.predict(
            image,
            conf=confidence,
            verbose=False
        )

    result = results[0]

    # Annotated image
    annotated_image = result.plot()

    st.subheader("🔬 DentalMate Prediction")

    st.image(
        annotated_image,
        caption="Detection + Segmentation",
        use_container_width=True
    )

    # Results
    st.subheader("📊 Detected Conditions")

    if result.boxes is None or len(result.boxes) == 0:

        st.warning("⚠️ No condition detected.")

    else:

        for i in range(len(result.boxes)):

            class_id = int(result.boxes.cls[i])
            conf = float(result.boxes.conf[i])

            class_name = model.names[class_id]

            st.write(
                f"🦷 **{class_name}** — "
                f"Confidence: **{conf:.1%}**"
            )