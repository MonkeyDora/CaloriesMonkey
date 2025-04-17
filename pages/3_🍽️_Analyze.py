import streamlit as st
import json
from utils import configuration_page, get_ai_response, get_image_caption

# Define the path to store the history file
history_file_path = "history.json"

# Function to load history from file
def load_history():
    try:
        with open(history_file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

# Function to save history to the file
def save_history(history):
    with open(history_file_path, "w") as file:
        json.dump(history, file)

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

# Load the history from the file (if any)
if "history" not in st.session_state:
    st.session_state.history = load_history()

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
        caption = get_image_caption(st.session_state.image_data)
        st.session_state.caption = caption

    question_prompt = f"What are the calories of {caption} and give me a table of its macronutrition and micronutrition."
    with st.spinner("🔄 Fetching Analysis..."):
        analysis_result = get_ai_response(question_prompt)
        st.session_state.analysis_result = analysis_result

    # ✅ Add to history (Storing only caption and analysis result)
    st.session_state.history.append({
        "caption": caption,
        "analysis": analysis_result
    })

    # Save the updated history to the file
    save_history(st.session_state.history)

    st.success(f"🔍 Identified Image: **{caption}**")
    st.success("💬 Results:")

# ✅ Display Results After Analysis
if st.session_state.caption:
    st.success(f"🔍 Identified Image: **{st.session_state.caption}**")
if st.session_state.analysis_result:
    st.write(st.session_state.analysis_result)

# 🔁 Optional link to history page
st.page_link("pages/4_📜_History.py", label="📜 View Analysis History")
