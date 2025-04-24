st.set_page_config(
    page_title="About",
    page_icon="📖"
)

configuration_page()

st.title("About SnapMetrix")

# Guide to using the Analyze page
st.info("📸 **Tip:** To analyze the nutrients in your food, go to the **Analyze** page, take a photo of your meal, and let SnapMetrix do the magic! 🧠 It will give you insights into both **macronutrients** and **micronutrients**. 🍽️")

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
