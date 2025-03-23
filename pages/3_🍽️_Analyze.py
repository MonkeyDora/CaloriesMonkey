import streamlit as st
from utils import configuration_page, get_ai_response, get_image_caption

st.set_page_config(
    page_title="Analyze",
    page_icon="🍽️"
)

configuration_page()

st.title("🎯 SnapMetrix Image Analysis")

# ✅ Initialize Session State Variables
if "caption" not in st.session_state:
    st.session_state.caption = None
if "image_data" not in st.session_state:
    st.session_state.image_data = None
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# 📸 Choose Image Source
option = st.radio("Choose an Image:", ["Upload Image", "Take a Picture"])

# 📂 Get Image Input
image_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"]) if option == "Upload Image" else st.camera_input("Take a Picture")

# ✅ Store Image in Session State (Persist Between Pages)
if image_file:
    st.session_state.image_data = image_file.getvalue()

# 🖼️ Display Uploaded Image (But Not Camera-Taken Images)
if st.session_state.image_data and option == "Upload Image":
    st.image(st.session_state.image_data, caption="Uploaded Image", use_container_width=True)

# 🔍 Analyze Button (Prevents Re-Analysis)
if st.button("Analyze Image") and st.session_state.image_data:
    with st.spinner("🔄 Analyzing image..."):
        st.session_state.caption = get_image_caption(st.session_state.image_data)
    st.success("🔍 Identified Image: " + f"**{st.session_state.caption}**")

    question_prompt = f"What are the calories of {st.session_state.caption} and give me a table of its macronutrition and micronutrition."
    with st.spinner("🔄 Fetching Analysis..."):
        st.session_state.analysis_result = get_ai_response(question_prompt)  # Store Result
    st.success("💬 Results:")

# ✅ Display Previously Fetched Data (Even After Navigation)
if st.session_state.caption:
    st.success(f"🔍 Identified Image: **{st.session_state.caption}**")
if st.session_state.analysis_result:
    st.write(st.session_state.analysis_result)
