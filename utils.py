import streamlit as st
import requests

def configuration_page():
    # Custom CSS to make the text stick to the very bottom of the sidebar
    sidebar_footer_css = """
        <style>
        [data-testid="stSidebar"] {
            position: relative;
            height: 100vh;
        }
        .sidebar-footer {
            position: absolute;
            bottom: 10px;
            left: 20px;
            font-size: 14px;
            color: grey;
            font-weight: bold;
        }
        </style>
    """

    sidebar_style = """
    <style>
    [data-testid="stSidebarNav"]::before {
        content: "📌 Navigation";  /* Change Sidebar Title */
        font-size: 20px;
        font-weight: bold;
        display: block;
        padding: 10px;
    }
    </style>
    """
    st.markdown(sidebar_style, unsafe_allow_html=True)

    hide_main_page_css = """
        <style>
        [data-testid="stSidebarNav"] ul li:first-child {
            display: none;
        }
        </style>
    """
    st.markdown(hide_main_page_css, unsafe_allow_html=True)
 



openrouter_api_key = st.secrets["secrets"]["OPENROUTER_API_KEY"]
huggingface_api_key = st.secrets["secrets"]["HUGGINGFACE_API_KEY"]

# Hugging Face Image Captioning API URL
IMAGE_API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"


# Function to Generate Image Caption
def get_image_caption(image_data):
    headers = {"Authorization": f"Bearer {huggingface_api_key}"}
    try:
        response = requests.post(IMAGE_API_URL, headers={"Content-Type": "image/jpeg", **headers}, data=image_data)
        if response.status_code == 200:
            data = response.json()
            return data[0]["generated_text"] if data else "⚠️ No caption generated."
        return f"❌ Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"⚠️ Please Try Again"

# 💬 Function to Get AI Response
def get_ai_response(user_input):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {openrouter_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [{"role": "user", "content": user_input}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        data = response.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "⚠️ No response received.")
    except requests.exceptions.RequestException as e:
        return f"Please Try Again"