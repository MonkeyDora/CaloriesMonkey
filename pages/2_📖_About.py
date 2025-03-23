import streamlit as st
from utils import configuration_page, get_ai_response

st.set_page_config(
    page_title="About",
    page_icon="📖"
)

configuration_page()

st.title("About SnapMetrix")
# Dictionary of Foods Categorized by Vitamins
vitamin_foods = {
    "Vitamin A": ["Carrots 🥕", "Sweet Potatoes 🍠", "Spinach 🌿", "Egg Yolks 🥚"],
    "Vitamin B": ["Whole Grains 🌾", "Legumes 🫘", "Eggs 🥚", "Milk 🥛"],
    "Vitamin C": ["Oranges 🍊", "Strawberries 🍓", "Bell Peppers 🫑", "Broccoli 🥦"],
    "Vitamin D": ["Salmon 🐟", "Mushrooms 🍄", "Egg Yolks 🥚", "Milk 🥛"],
    "Vitamin E": ["Almonds 🌰", "Sunflower Seeds 🌻", "Spinach 🌿", "Avocado 🥑"],
    "Vitamin K": ["Kale 🥬", "Broccoli 🥦", "Soybeans 🌱", "Green Tea 🍵"]
}

# About Page Header
st.subheader("🍽️ Food & Vitamins")
st.write("Explore different foods rich in essential vitamins. Click on a vitamin to learn more!")

# Initialize session state for vitamin explanations
if "vitamin_explanations" not in st.session_state:
    st.session_state.vitamin_explanations = {}

# Display categories dynamically
for vitamin, foods in vitamin_foods.items():
    with st.expander(f"🟢 {vitamin}"):
        st.write(", ".join(foods))  # Display foods as a list
        # Check if explanation is already stored
        if vitamin not in st.session_state.vitamin_explanations:
            with st.spinner(f"🔄 Explaining {vitamin}..."):
                response = get_ai_response(vitamin)  # Simulate AI response
                st.session_state.vitamin_explanations[vitamin] = response  # Store in session state
        # Show the stored response
        st.success(f"💡 Explanation for {vitamin}")
        st.write(st.session_state.vitamin_explanations[vitamin])