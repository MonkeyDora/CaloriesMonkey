import streamlit as st
import requests
import time

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
        # Send the request and get the response
        response = requests.post(url, headers=headers, json=payload)

        # Print the status code to the console for debugging
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            # If the response is successful, return the message content
            data = response.json()
            message_content = data.get("choices", [{}])[0].get("message", {}).get("content", "⚠️ No response received.")
            return message_content

        elif response.status_code == 429:
            # Handle rate limiting: Retry-After header suggests how long to wait
            retry_after = response.headers.get("Retry-After")
            if retry_after:
                print(f"Rate limit exceeded. Retrying after {retry_after} seconds...")
                time.sleep(int(retry_after))  # Wait for the specified duration before retrying
                return get_ai_response(user_input)  # Retry the request after waiting
            else:
                print("Rate limit exceeded, but no Retry-After header provided. Retrying after 60 seconds...")
                time.sleep(60)  # Default wait time of 60 seconds
                return get_ai_response(user_input)  # Retry after default wait

        else:
            # For any other status code, return an error message
            return f"Error: Received status code {response.status_code}. Response: {response.text}"

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions (e.g., network errors, timeout)
        print(f"Request Exception: {e}")
        return f"Please try again. Error: {e}"

# Example call to test
result = get_ai_response("Tell me about Vitamin A")
print(result)