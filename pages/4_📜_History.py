import streamlit as st
import json

# Define the path to the history file
history_file_path = "history.json"

# Function to load history from file
def load_history():
    try:
        with open(history_file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

st.set_page_config(
    page_title="History",
    page_icon="📜"
)

# Configuration for the page (if you have a custom config function)
from utils import configuration_page
configuration_page()

st.title("📜 Analysis History")

# Load the history from the file (if any)
history = load_history()

# 🚨 Check if there's any history to display
if not history:
    st.info("No analysis history available yet. Go analyze something first!")
else:
    # 🔁 Show history in reverse (most recent first)
    for i, entry in enumerate(reversed(history), 1):
        st.subheader(f"📌 Entry #{len(history) - i + 1}")

        # 📋 Display the caption
        st.markdown(f"**📝 Caption:** {entry['caption']}")

        # 📊 Display the analysis
        st.markdown("**🔬 Nutritional Analysis:**")
        st.write(entry["analysis"])

        # Divider
        st.markdown("---")
