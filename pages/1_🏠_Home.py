import streamlit as st
from utils import configuration_page

st.set_page_config(
    page_title="Main",
    page_icon="🏠"
)

configuration_page()

st.title("🚀SnapMetrix")
st.image("home.jpg", use_container_width=True)
# Engaging Introduction
st.markdown("""
### 🌍 **Food: The Fuel of Life**  
Have you ever stopped to wonder **how much energy** it takes just to exist?  
Every breath, every blink, and even your thoughts—**all require energy**.  

We live in an era where **food is abundant**, yet **nutritional knowledge is scarce**.  
The paradox? Many of us eat too much yet **lack the nutrients our bodies need to thrive**.  

---

### 🔥 **Even the Smallest Activities Burn Energy**  
Did you know that just **sitting and thinking** burns calories?  
What about **laughing, fidgeting, or even digesting food**?  

Your body is a complex machine, constantly working—even when you feel like you’re doing nothing.  
Imagine if you could understand exactly how much energy you **use** and how much you **consume**.  

Would you start making **better food choices**?  

---

### 🏆 **Our Vision: A Smarter, Healthier World**  
- To **help you** understand the energy value of food and how your body uses it.  
- To **educate** people on how to balance nutrition, so we don’t just eat—we **fuel** ourselves.  
- To **build a healthier future**, one informed decision at a time.  

We realize that many struggle with **finding the right foods** or **understanding how diet affects their health**.  
That’s why we’re here: To provide **clear, accurate, and personalized nutrition insights**—**for everyone**.  

---
""")

# Section: The Invisible Energy You Use Daily
st.header("💡 The Invisible Energy You Use Every Day")

activities = {
    "Sleeping 😴": "50 kcal per hour",
    "Sitting 🪑": "75 kcal per hour",
    "Standing 🚶‍♂️": "100 kcal per hour",
    "Light Walking 🚶": "200 kcal per hour",
    "Jogging 🏃": "400 kcal per hour",
    "Laughing 😂": "20 kcal per 10 mins"
}

for activity, calories in activities.items():
    st.write(f"✅ **{activity}**: Burns **{calories}**")

st.markdown("---")

# Section: Calories in Everyday Foods
st.header("🍎 Calories in Foods We Consume Daily")

food_calories = {
    "Slice of Pizza 🍕": "285 kcal",
    "Bowl of Rice 🍚": "200 kcal",
    "Chicken Breast 🍗": "165 kcal",
    "Cup of Coffee ☕": "2 kcal (without sugar/milk)",
    "Ice Cream 🍦": "207 kcal per scoop",
    "Avocado 🥑": "234 kcal per fruit"
}

for food, calories in food_calories.items():
    st.write(f"🍽️ **{food}**: Contains **{calories}**")

st.markdown("---")

st.success("""
💡 **Knowledge is power**. The more we understand what fuels our bodies,  
the better choices we can make—for our health, our energy, and our future.  
Are you ready to take control of your nutrition? 🚀  
""")



