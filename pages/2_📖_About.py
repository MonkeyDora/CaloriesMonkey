import streamlit as st
import time  # Simulating delay
from utils import configuration_page, get_ai_response

# Vitamin functions...
# (All your vitaminA(), vitaminB(), etc. functions remain unchanged)

st.set_page_config(
    page_title="About",
    page_icon="📖"
)

configuration_page()

st.title("About SnapMetrix")

# ✅ NEW: Add usage guide here
st.info("""
📸 **How to Use SnapMetrix for Nutrition Analysis:**
1. Go to the **Analyze** page.
2. **Take or upload a photo** of your meal.
3. Click on **Analyze Image**.
4. Get your results in terms of **Macronutrients (Carbs, Protein, Fat)** and **Micronutrients (Vitamins & Minerals)**.

🔬 It's that simple! Let SnapMetrix break down the nutrition for you!
""")

# Dictionary of Foods Categorized by Vitamins
vitamin_foods = {
    "Vitamin A": ["Carrots 🥕", "Sweet Potatoes 🍠", "Spinach 🌿", "Egg Yolks 🥚"],
    "Vitamin B": ["Whole Grains 🌾", "Legumes 🫘", "Eggs 🥚", "Milk 🥛"],
    "Vitamin C": ["Oranges 🍊", "Strawberries 🍓", "Bell Peppers 🫑", "Broccoli 🥦"],
    "Vitamin D": ["Salmon 🐟", "Mushrooms 🍄", "Egg Yolks 🥚", "Milk 🥛"],
    "Vitamin E": ["Almonds 🌰", "Sunflower Seeds 🌻", "Spinach 🌿", "Avocado 🥑"],
    "Vitamin K": ["Kale 🥬", "Broccoli 🥦", "Soybeans 🌱", "Green Tea 🍵"]
}

# Vitamin explanations
vitamin_info = {
    "Vitamin A": vitaminA,
    "Vitamin B": vitaminB,
    "Vitamin C": vitaminC,
    "Vitamin D": vitaminD,
    "Vitamin E": vitaminE,
    "Vitamin K": vitaminK
}

# About Page Header
st.subheader("🍽️ Food & Vitamins")
st.write("Explore different foods rich in essential vitamins. Click on a vitamin to learn more!")

# Initialize session state for tracking expanded vitamin
if "expanded_vitamin" not in st.session_state:
    st.session_state.expanded_vitamin = None

# Display vitamins dynamically
for vitamin, foods in vitamin_foods.items():
    with st.expander(f"🟢 {vitamin}"):
        st.write(", ".join(foods))  # Show food list
        vitamin_info[vitamin]()
