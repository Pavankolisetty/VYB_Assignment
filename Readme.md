# VYB AI Project

## Introduction

This project aims to estimate the nutritional values of home-cooked Indian dishes based on a given dish name. The AI pipeline fetches ingredient lists, converts quantities into standardized household measurements, and calculates the total nutrition based on a provided nutrition database.

## Prerequisites

You need the following dependencies depending on the language you are using:

### Python Setup:

1. Install Python dependencies:
   ```bash
   pip install requests openai pandas
2. Place the provided nutrition_database.csv and household_mapping.json files in the data/ folder.

### Node.js Setup:

1. Install Node.js dependencies:
``` bash 
npm install axios openai
```

2.  Place the provided nutrition_database.csv and household_mapping.json files in the data/ folder.
Running the Project
Python:
Run the Python script:
```bash
python main.py
```
This will fetch the recipe data, map the ingredients, and calculate the nutritional values for a given dish.

Node.js:
Run the Node.js app:
```
node app.js
```
This will do the same functionality as the Python script but using Node.js.

### File Structure

VYB_AI_Project/
│
├── data/
│   ├── nutrition_database.csv
│   └── household_mapping.json
│
├── main.py (or app.js)
├── README.md
└── requirements.txt (for Python projects)


### Assumptions and Notes
The recipe input should be a valid Indian dish name, and the script will fetch the ingredient list from a predefined source (or simulate it if no source is available).

Quantities will be converted into standardized household measurements (like katori, cup, etc.) before performing the nutritional calculation.

Nutrition is estimated per 100g and extrapolated based on standard serving sizes.

The program handles missing or invalid data gracefully without crashing, logging errors where applicable.


### Live Streaming Link
https://vybassignment-sqbruvbabv2yzz7sqzrtpl.streamlit.app/


### Output Screenshots
![Screenshot (33)](https://github.com/user-attachments/assets/a7048bba-a8f8-46bc-a69b-a62230c48281)

![Screenshot (34)](https://github.com/user-attachments/assets/d256fe48-4b8d-4db3-985c-7a64053f69d8)

![Screenshot (35)](https://github.com/user-attachments/assets/8e3db156-0dec-459b-ad21-32bbe9acdd97)

![Screenshot (36)](https://github.com/user-attachments/assets/9c45d92d-a624-4746-a64a-93ff2266c74b)


### Handling Edge Cases
The program gracefully handles cases where ingredients are missing or the recipe data is incomplete.

Missing ingredients are either ignored or assigned a fallback value, ensuring the program doesn't crash.

The program also deals with different synonyms for ingredients intelligently (e.g., "paneer" vs. "cottage cheese").

### Contributing
Feel free to contribute by opening an issue or submitting a pull request. This project is aimed at improving the nutritional estimation process for home-cooked Indian dishes, and we welcome any improvements or suggestions.

### License
This project is licensed under the MIT License.


This is your updated `README.md` with all the modifications mentioned. Just copy this content into your `README.md` file in your project! Let me know if you need anything else.
