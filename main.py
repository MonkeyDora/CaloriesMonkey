import streamlit as st
import requests

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
        return f"⚠️ Exception: {str(e)}"

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

# Sidebar Navigation
st.sidebar.title("🍽️ Navigation")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Identify", "History"])
if "history_data" not in st.session_state:
        st.session_state.history_data = None

# Home Page
if app_mode == "Home":
    st.title("🍎 Food Nutrition Analyze")
    st.image("home.jpg", use_container_width=True)
    st.write("""
        Have you ever thought about how the food you eat affects your health?  
        Our mission is to help you make informed decisions about nutrition.  
        Use this app to analyze food images and ask questions about them.
    """)
    # Ask Questions About the Image
    st.subheader("Ask About This Food:")
    questions = ["1+1", "2+2", "3+3", "4+4", "5+5", "is apple red?", "", "", "", ""]
    question = st.selectbox("Q&A", questions)
    # user_question = st.text_input("Enter your question:", placeholder="What food do you want to eat?")
    
    # if st.button("Get Answer"):
    #     for i in range(len(staticQuests)):
    #         if(question==staticQuests[i]):
    #             st.write(staticResponse[i])
    #         elif(question==randomQuests[i]):
    #             question_prompt = f"{question[i]}"
    #             with st.spinner("🔄 Analyze..."):
    #                 response = get_ai_response(question_prompt)
    #             st.success("💬 AI Response:")
    #             st.write(response)
        # if user_question.strip():
        # else:
        #     st.warning("⚠️ Please enter a question.")
        

# About Page
elif app_mode == "About":
    st.title("About This App")
    st.write("""
        This app used to recognize foods and estimate their calorie content.
        It supports various fruits, vegetables, and common meals.
    """)
    st.code("Supported Foods: Banana, Apple, Orange, Pizza, Burger, etc.")

# 🍽️ Food Analizing Page
elif app_mode == "Identify":
    st.title("🍽️ Food Image Analysis & Q&A")

    # ✅ Session State Initialization
    if "caption" not in st.session_state:
        st.session_state.caption = None
    if "image_data" not in st.session_state:
        st.session_state.image_data = None

    # Image Upload or Camera Input
    option = st.radio("Choose an Image:", ["Upload Image", "Take a Picture"])
    image_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"]) if option == "Upload Image" else st.camera_input("Take a Picture")

    # Store Image in Session State
    if image_file:
        st.session_state.image_data = image_file.getvalue()
        st.image(st.session_state.image_data, caption="Uploaded Image", use_container_width=True)

        # Generate Image Caption
        if st.button("Generate Caption"):
            with st.spinner("🔄 Analyzing image..."):
                st.session_state.caption = get_image_caption(st.session_state.image_data)
            st.success("🔍 Identified Food:" + f"**{st.session_state.caption}**")
            question_prompt = f"What the calories of {st.session_state.caption}"
            with st.spinner("🔄 Analyze..."):
                response = get_ai_response(question_prompt)
            st.success("💬 Results:")   
            st.write(response)
#             if st.session_state.history_data is not None:
#                 st.session_state.history_data = response

# #History
# elif app_mode == "History":
#     st.write(st.session_state.history_data)
    
