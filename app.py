import streamlit as st
import pandas as pd

# Load nutrition data
nutrition_df = pd.read_csv("data/nutrition.csv")

# Define mapping of dishes to ingredients
dish_ingredients = {
    "paneer butter masala": ["Paneer", "Butter", "Tomato", "Onion", "Cream", "Garlic", "Garam Masala", "Oil"],
    "dal fry": ["Dal", "Onion", "Tomato", "Garlic", "Cumin", "Turmeric", "Oil"],
    "chole masala": ["Chickpeas", "Onion", "Tomato", "Garlic", "Garam Masala", "Oil"],
    "aloo gobi": ["Potato", "Cauliflower", "Onion", "Tomato", "Cumin", "Turmeric", "Oil"],
    "vegetable pulao": ["Rice", "Carrot", "Green Peas", "Onion", "Cumin", "Oil"]
}

# App layout
st.title("VYB AI Nutrition Helper")
st.subheader("Nutrition Data Preview")
st.dataframe(nutrition_df)

# Input from user
food_item = st.text_input("Enter a food item:")

if food_item:
    # Standardize input
    food_item_lower = food_item.lower().strip()

    if food_item_lower in dish_ingredients:
        matched_ings = dish_ingredients[food_item_lower]
        results = nutrition_df[nutrition_df["Ingredient"].isin(matched_ings)]

        st.subheader(f"Nutritional Information for '{food_item.title()}'")
        st.dataframe(results)


        st.subheader("Total Nutrition")
        st.write(results.drop(columns=["Ingredient"]).sum(numeric_only=True))
    else:
        st.warning("Dish not found. Please enter one of: " + ", ".join(dish_ingredients.keys()))
