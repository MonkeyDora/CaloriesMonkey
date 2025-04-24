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

def vitaminA():
    with st.spinner(f"🔄 Fetching explanation for Vitamin A..."):
        time.sleep(1)  # Simulating delay
        st.title("🥕 Vitamin A: The Essential Nutrient for Vision and Immunity")
        st.header("What is Vitamin A?")
        st.write("Vitamin A is a fat-soluble vitamin essential for **vision, immune function, reproduction, and skin health**. It also helps in organ development and tissue growth.")

        st.subheader("Types of Vitamin A")
        st.write("""
        - **Preformed Vitamin A (Retinoids)** – Found in **animal-based** foods like liver, egg yolks, and dairy products.
        - **Provitamin A (Carotenoids, e.g., Beta-Carotene)** – Found in **plant-based** foods like carrots, spinach, and sweet potatoes. The body converts it into active vitamin A as needed.
        """)

        st.subheader("✅ Health Benefits of Vitamin A")
        st.write("""
        - **Supports Eye Health** 👁️ – Prevents night blindness and maintains a clear cornea.
        - **Boosts Immunity** 🛡️ – Strengthens the immune system against infections.
        - **Promotes Skin Health** ✨ – Supports cell growth and reduces acne/wrinkles.
        - **Essential for Growth & Development** 👶 – Important during pregnancy.
        """)

        st.subheader("🥗 Best Food Sources of Vitamin A")
        food_sources = {
            "Carrots 🥕": "Rich in beta-carotene, great for eye health.",
            "Sweet Potatoes 🍠": "A powerful source of provitamin A.",
            "Spinach & Kale 🥬": "Packed with antioxidants and carotenoids.",
            "Egg Yolks 🥚": "Contain preformed vitamin A.",
            "Liver & Fish Oils 🐟": "Some of the richest sources of vitamin A."
        }
        for food, benefit in food_sources.items():
            st.write(f"**{food}** – {benefit}")

        st.subheader("⚠️ Vitamin A Deficiency")
        st.write("""
        - **Night blindness** and dry eyes.
        - **Weakened immune function**, making you more prone to infections.
        - **Dry skin and slow wound healing**.
        """)

        st.subheader("📌 Recommended Daily Intake")
        st.table({
            "Group": ["Men", "Women", "Children"],
            "Recommended Intake": ["~900 mcg/day", "~700 mcg/day", "~300–600 mcg/day"]
        })

        st.subheader("🚨 Can You Get Too Much Vitamin A?")
        st.write("""
        Yes! Excessive intake of **preformed vitamin A** (from supplements or animal sources) can cause:
        - **Dizziness, nausea, liver damage, and even birth defects** in pregnant women.
        - High intake of **beta-carotene** (from vegetables) is not toxic but may turn your skin slightly orange.
        """)

        st.success("💡 Tip: Balance your intake with a healthy diet rich in natural food sources!")

def vitaminB():
     with st.spinner(f"🔄 Fetching explanation for Vitamin B..."):
        time.sleep(1)  # Simulating delay
        st.title("🏋️ Vitamin B: The Energy Booster & Brain Supporter")

        st.header("🔹 What is Vitamin B?")
        st.write("Vitamin B is **not a single vitamin** but a group of **eight essential B vitamins**, known as the **B-complex vitamins**. These vitamins play a crucial role in **energy production, brain function, red blood cell formation, and metabolism**.")

        st.header("🔹 Types of B Vitamins & Their Benefits")

        vitamin_b_data = {
            "B1 (Thiamine)": ("Converts food into energy, supports nerve function", "Whole grains, nuts, pork"),
            "B2 (Riboflavin)": ("Helps with energy production and skin health", "Dairy, eggs, leafy greens"),
            "B3 (Niacin)": ("Supports digestion, skin health, and brain function", "Meat, fish, nuts, whole grains"),
            "B5 (Pantothenic Acid)": ("Essential for hormone production and metabolism", "Avocados, eggs, mushrooms"),
            "B6 (Pyridoxine)": ("Helps brain development, immune function, and mood regulation", "Bananas, poultry, potatoes"),
            "B7 (Biotin)": ("Promotes healthy hair, skin, and nails", "Eggs, nuts, seeds"),
            "B9 (Folate/Folic Acid)": ("Essential for cell growth, especially during pregnancy", "Leafy greens, beans, citrus fruits"),
            "B12 (Cobalamin)": ("Supports nerve function and red blood cell production", "Meat, fish, dairy, fortified cereals"),
        }

        for vitamin, (benefits, sources) in vitamin_b_data.items():
            st.subheader(f"🔹 {vitamin}")
            st.write(f"**Benefits:** {benefits}")
            st.write(f"**Sources:** {sources}")
            st.markdown("---")  # Separator for better readability

        st.header("🔹 Why is Vitamin B Important?")
        st.write("✅ **Boosts Energy**: Helps break down carbs, fats, and proteins into usable energy")
        st.write("✅ **Supports Brain Health**: Essential for memory, focus, and preventing cognitive decline")
        st.write("✅ **Promotes Red Blood Cell Production**: Prevents anemia and keeps oxygen flowing")
        st.write("✅ **Crucial for Pregnancy**: Folic acid (B9) prevents birth defects and supports fetal growth")

        st.header("🔹 Vitamin B Deficiency Symptoms")
        st.warning("⚠️ A lack of B vitamins can cause:")
        st.write("- Fatigue & weakness")
        st.write("- Memory problems & mood swings")
        st.write("- Skin issues (dryness, acne)")
        st.write("- Tingling in hands & feet (B12 deficiency)")

        st.header("🔹 Conclusion")
        st.success("Vitamin B is **vital for energy, brain health, and cell function**. Make sure to include **whole grains, meat, dairy, nuts, and leafy greens** in your diet to stay healthy! 🥦🥚🐟")

def vitaminC():
    with st.spinner(f"🔄 Fetching explanation for Vitamin C..."):
        time.sleep(1)  # Simulating delay
        # Title and Introduction
        st.title("🍊 Vitamin C: The Immunity-Boosting Antioxidant")

        st.header("What is Vitamin C?")
        st.write("Vitamin C, also known as **ascorbic acid**, is a water-soluble vitamin essential for "
                "**immune function, collagen production, wound healing, and antioxidant protection**. "
                "Since our bodies cannot produce it, we must get it from food or supplements.")

        st.header("Health Benefits of Vitamin C")
        st.write("✅ **Boosts Immunity** – Helps the body fight infections and illnesses.")
        st.write("✅ **Promotes Skin Health** – Supports collagen production for healthy skin, hair, and nails.")
        st.write("✅ **Acts as a Powerful Antioxidant** – Protects cells from damage caused by free radicals.")
        st.write("✅ **Enhances Iron Absorption** – Helps the body absorb iron from plant-based foods.")
        st.write("✅ **Speeds Up Wound Healing** – Plays a vital role in tissue repair and recovery.")

        st.header("Food Sources of Vitamin C")
        st.write("🥝 **Fruits** – Oranges, strawberries, kiwis, guavas, pineapples.")
        st.write("🥦 **Vegetables** – Bell peppers, broccoli, Brussels sprouts, tomatoes.")
        st.write("🍊 **Citrus Fruits** – Lemons, limes, grapefruits, mandarins.")

        st.header("Vitamin C Deficiency Symptoms")
        st.write("⚠️ Fatigue and weakness")
        st.write("⚠️ Frequent infections and slow wound healing")
        st.write("⚠️ Dry skin and brittle hair")
        st.write("⚠️ Swollen or bleeding gums (scurvy)")

        st.success("Make sure to include Vitamin C-rich foods in your diet for a healthy immune system! 🥦🍊")

def vitaminD():
    with st.spinner(f"🔄 Fetching explanation for Vitamin D..."):
        time.sleep(1)  # Simulating delay
        st.title("🌞 Vitamin D: The Sunshine Vitamin")

        st.subheader("📌 What is Vitamin D?")
        st.write("""
            Vitamin D is a **fat-soluble vitamin** that helps the body absorb **calcium and phosphorus**.
            It plays a crucial role in maintaining **strong bones, immunity, and mental health**.
            """)

        st.subheader("💡 Health Benefits of Vitamin D")
        st.write("""
        - ✅ **Bone Health** – Prevents rickets & osteoporosis.
        - ✅ **Immune System Boost** – Reduces inflammation.
        - ✅ **Mood & Mental Health** – Linked to lower depression risks.
        - ✅ **Heart Health** – Supports cardiovascular function.
        """)

        st.subheader("🍽️ Best Sources of Vitamin D")
        st.write("""
        - 🌞 **Sunlight exposure** – Natural production in the skin.
        - 🐟 **Fatty fish** (Salmon, Mackerel, Tuna).
        - 🥛 **Fortified dairy & plant-based milk**.
        - 🍄 **Mushrooms** (especially sun-exposed ones).
        - 🥚 **Egg Yolks**.
        """)

        st.success("✅ Get enough Vitamin D to stay healthy and strong!")


def vitaminE():
    with st.spinner(f"🔄 Fetching explanation for Vitamin E..."):
        time.sleep(1)  # Simulating delay

        st.title("🌿 Vitamin E: The Antioxidant Powerhouse")

        # Expander for interactive content
        st.subheader("📌 What is Vitamin E?")
        st.write("""
        Vitamin E is a **fat-soluble vitamin** that acts as a **powerful antioxidant**, protecting cells from free radical damage.
        It supports **immune function, skin health, and heart health**.
        """)

        st.subheader("💡 Health Benefits of Vitamin E")
        st.write("""
        - ✅ **Antioxidant Protection** – Fights free radicals.
        - ✅ **Skin Health** – Supports glowing skin and reduces aging.
        - ✅ **Boosts Immunity** – Strengthens the immune system.
        - ✅ **Heart Health** – Reduces oxidative stress and supports cardiovascular function.
        - ✅ **Eye Health** – May help prevent macular degeneration.
        """)

        st.subheader("🍽️ Best Sources of Vitamin E")
        st.write("""
        - 🥑 **Avocado** – Rich in Vitamin E.
        - 🌰 **Almonds** – One of the best natural sources.
        - 🌻 **Sunflower Seeds** – High in Vitamin E and healthy fats.
        - 🥦 **Spinach & Broccoli** – Leafy greens packed with nutrients.
        - 🐟 **Fatty Fish** – Moderate sources include salmon & trout.
        - 🥜 **Peanuts & Hazelnuts** – Great nut-based options.
        """)

        st.success("✅ Ensure you get enough Vitamin E for a healthier body!")

def vitaminK():
    with st.spinner(f"🔄 Fetching explanation for Vitamin K..."):
        time.sleep(1)  # Simulating delay

        st.title("🥬 Vitamin K: The Blood Clotting & Bone Health Vitamin")

        # Expander for interactive content
        st.subheader("📌 What is Vitamin K?")
        st.write("""
        Vitamin K is a **fat-soluble vitamin** essential for **blood clotting, bone health, and heart function**.
        It helps regulate calcium in bones and arteries.
        """)

        st.subheader("💡 Health Benefits of Vitamin K")
        st.write("""
        - ✅ **Supports Blood Clotting** – Prevents excessive bleeding.
        - ✅ **Boosts Bone Strength** – Helps in calcium absorption.
        - ✅ **Heart Health** – Reduces arterial calcification.
        - ✅ **Brain Function** – May protect against cognitive decline.
        """)

        st.subheader("🔬 Types of Vitamin K")
        st.write("""
        - 🔹 **Vitamin K1 (Phylloquinone)** – Found in leafy greens, supports blood clotting.
        - 🔹 **Vitamin K2 (Menaquinone)** – Found in fermented foods and animal products, supports bone & heart health.
        """)

        st.subheader("🍽️ Best Sources of Vitamin K")
        st.write("""
        - 🥬 **Kale & Spinach** – Top plant-based sources.
        - 🥦 **Broccoli & Brussels Sprouts** – Cruciferous vegetables rich in Vitamin K.
        - 🍵 **Green Tea** – Contains a small amount of Vitamin K.
        - 🧀 **Cheese & Egg Yolks** – Good sources of Vitamin K2.
        - 🥩 **Liver & Meat** – Found in small amounts in animal-based diets.
        - 🍣 **Natto (Fermented Soybeans)** – The richest natural source of Vitamin K2.
        """)

        st.success("✅ Ensure you consume enough Vitamin K for strong bones and a healthy heart!")


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

# # Check if Vitamin D was expanded
# if st.session_state.expanded_vitamin == "Vitamin A":
