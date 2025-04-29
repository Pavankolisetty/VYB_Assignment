import pandas as pd
import json
import os

# Load Household Measurement Mapping
try:
    with open('C:/Users/pavan kumar/OneDrive/Desktop/Vyb/env/data/householding.json', 'r') as f:
        household_mapping = json.load(f)
except FileNotFoundError:
    print("Error: 'data/household_mapping.json' not found. Please check the path.")
    household_mapping = {}

# Load Nutrition Database
try:
    nutrition_data = pd.read_csv('C:/Users/pavan kumar/OneDrive/Desktop/Vyb/env/data/nutrition.csv')
    nutrition_data.set_index("Ingredient", inplace=True)
except FileNotFoundError:
    print("Error: 'nutrition.csv' not found. Please check the path.")
    nutrition_data = pd.DataFrame()

# Ingredient name normalization
# Expanded Ingredient name normalization mapping (case-insensitive)
ingredient_mapping = {
    "ghee": "Butter",
    "toor dal": "Dal",
    "arhar dal": "Dal",
    "moong dal": "Dal",
    "masoor dal": "Dal",
    "paneer": "Paneer",
    "cream": "Cream",
    "jeera": "Cumin",
    "cumin seeds": "Cumin",
    "rai": "Mustard",
    "mustard seeds": "Mustard",
    "garlic": "Garlic",
    "garlic cloves": "Garlic",
    "onions": "Onion",
    "onion": "Onion",
    "tomatoes": "Tomato",
    "tomato": "Tomato",
    "green chili": "Chili",
    "red chili": "Chili",
    "chili": "Chili",
    "coriander powder": "Coriander",
    "turmeric powder": "Turmeric",
    "hing": "Asafoetida",
    "cloves": "Clove",
    "garam masala": "Garam Masala"
    # Add more mappings as needed
}


# Simulate fetching a recipe for a dish
def get_recipe_for_dish(dish_name):
    dummy_recipes = {
        "Paneer Butter Masala": [
            "Paneer - 200g",
            "Butter - 50g",
            "Tomato - 3 medium",
            "Onion - 2 medium",
            "Cream - 2 tablespoons",
            "Garam Masala - 1 teaspoon"
        ],
        "Dal Tadka": [
            "Toor Dal - 100g",
            "Ghee - 2 tablespoons",
            "Onion - 1 large",
            "Tomato - 2 medium",
            "Garlic - 4 cloves",
            "Cumin Seeds - 1 teaspoon"
        ],
        "Chole Masala": [
            "Chickpeas - 150g",
            "Onion - 2 medium",
            "Tomato - 2 medium",
            "Garlic - 3 cloves",
            "Garam Masala - 1 teaspoon",
            "Oil - 2 tablespoons"
        ],
        "Aloo Gobi": [
            "Potato - 2 medium",
            "Cauliflower - 1 small",
            "Turmeric Powder - 1 teaspoon",
            "Cumin Seeds - 1 teaspoon",
            "Onion - 1 medium",
            "Oil - 2 tablespoons"
        ],
        "Vegetable Pulao": [
            "Rice - 150g",
            "Carrot - 1 medium",
            "Green Peas - 50g",
            "Onion - 1 medium",
            "Ghee - 1 tablespoon",
            "Cumin Seeds - 1 teaspoon"
        ]
    }

    if dish_name in dummy_recipes:
        return dummy_recipes[dish_name]
    else:
        print(f"Recipe for '{dish_name}' not found. Returning a dummy recipe.")
        return [
            "Ingredient1 - 100g",
            "Ingredient2 - 50g"
        ]


# Parse an ingredient list and convert quantities to grams
def parse_and_standardize_ingredients(recipe):
    standardized_ingredients = []
    
    for item in recipe:
        try:
            # Split the ingredient into name, quantity, and unit
            parts = item.split(" - ")
            ingredient = parts[0].strip()
            quantity_unit = parts[1].strip()
            
            # Extract the numeric quantity and the unit
            quantity = float(''.join([c for c in quantity_unit if c.isdigit() or c == '.']))
            unit = ''.join([c for c in quantity_unit if not c.isdigit() and c != '.']).strip().lower()
            
            # Convert to grams using household mapping
            grams = None
            if unit in household_mapping.get("Wet Sabzi", {}):
                grams = quantity * household_mapping["Wet Sabzi"][unit]
            elif unit in household_mapping.get("Dry Sabzi", {}):
                grams = quantity * household_mapping["Dry Sabzi"][unit]
            elif unit in household_mapping.get("Spices", {}):
                grams = quantity * household_mapping["Spices"][unit]
            elif unit in household_mapping.get("Vegetables", {}):
                grams = quantity * household_mapping["Vegetables"][unit]
            elif unit in household_mapping.get("Miscellaneous", {}):
                grams = quantity * household_mapping["Miscellaneous"][unit]
            else:
                grams = quantity  # Assume it's already in grams if no mapping is found
            
            # Normalize ingredient names
            # Normalize ingredient names (case-insensitive)
            normalized_ingredient = ingredient_mapping.get(ingredient.lower(), ingredient)

            
            # Append the standardized ingredient
            standardized_ingredients.append({"ingredient": normalized_ingredient, "grams": grams})
        except Exception as e:
            print(f"Warning: Could not parse or convert ingredient '{item}'. Error: {e}")
    
    return standardized_ingredients

# Calculate total nutrition per 100g
def calculate_nutrition(ingredients):
    total_nutrition = {"Calories": 0, "Protein": 0, "Carbs": 0, "Fat": 0, "Fiber": 0}
    
    for item in ingredients:
        ingredient = item["ingredient"]
        grams = item["grams"]
        
        if ingredient in nutrition_data.index:
            nutrition_per_100g = nutrition_data.loc[ingredient]
            for key in total_nutrition:
                total_nutrition[key] += (grams / 100) * nutrition_per_100g[key]
        else:
            print(f"Warning: Nutrition data not found for ingredient '{ingredient}'. Skipping.")
    
    return total_nutrition

# Calculate nutrition per standard serving
def calculate_per_serving(total_nutrition, total_weight, serving_weight=180):
    scaling_factor = serving_weight / total_weight
    return {key: value * scaling_factor for key, value in total_nutrition.items()}

# Main function
def main():
    print("VYB AI Project Initialized!")
    print("Household Mapping Loaded:")
    print(household_mapping)
    
    # Fetch a recipe for a given dish name
    dish_name = input("Enter the dish name: ")
    recipe = get_recipe_for_dish(dish_name)
    print("\nFetched Recipe:")
    print(recipe)
    
    # Parse and standardize the recipe ingredients
    standardized_ingredients = parse_and_standardize_ingredients(recipe)
    print("\nStandardized Ingredients:")
    total_weight = 0
    for item in standardized_ingredients:
        print(f"{item['ingredient']}: {item['grams']} grams")
        total_weight += item["grams"]
    
    # Calculate total nutrition
    total_nutrition = calculate_nutrition(standardized_ingredients)
    print("\nTotal Nutrition (for full dish):")
    print(total_nutrition)
    
    # Calculate nutrition per standard serving
    nutrition_per_serving = calculate_per_serving(total_nutrition, total_weight)
    print("\nNutrition Per Standard Serving (180g):")
    print(nutrition_per_serving)

if __name__ == "__main__":
    main()