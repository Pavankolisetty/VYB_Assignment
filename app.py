import streamlit as st
import pandas as pd

st.title("VYB AI Nutrition Helper")

# Load your data
nutrition_df = pd.read_csv("data/nutrition.csv")
st.write("Nutrition Data Preview", nutrition_df.head())

# Add some input fields
food_item = st.text_input("Enter a food item:")
if food_item:
    results = nutrition_df[nutrition_df["Food"].str.contains(food_item, case=False)]
    st.write("Search Results", results)
