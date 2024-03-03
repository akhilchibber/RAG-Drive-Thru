!pip install annoy

# Importing the essential libraries
from annoy import AnnoyIndex
import json
import spacy
from gensim.models import Word2Vec
import numpy as np
import time
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from io import StringIO
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
     
dimension = 100  # Vector dimensionality
n_trees = 10  # More trees, better precision, slower build
index = AnnoyIndex(dimension, 'angular')  # Using angular distance

# Example: Add item with ID 0
index.add_item(0, [0.5]*dimension) 

# Build the index
index.build(n_trees)

# Saving the index to disk for reuse
index.save('menu_index.ann')
print("Index is built and saved.")

# Load the index back
index.load('menu_index.ann')
print("Index is loaded.")

# Provide the file path of the menu.json file
file_path = 'menu.json'   

# Open the file and load its content into a variable
with open(file_path, 'r') as file:
    menu_data = json.load(file) 

# Now, 'menu_data' contains the content of 'menu.json'
print(menu_data)  # This will print the content of the menu data

restructured_chicken = []
     
for item_id, details in menu_data["Chicken"].items():
    item_name, price, item_details = details
    nutritional_info = item_details['nutritionalInfo']
    available = item_details['available']
    allergens = nutritional_info.get('allergens', [])

    restructured_item = {
        "id": item_id,
        "name": item_name,
        "type": "Chicken",
        "price": price,
        "nutritionalInfo": nutritional_info,
        "available": available,
        "allergens": allergens
    }

    restructured_chicken.append(restructured_item)
     
print(restructured_chicken)

# Function to concatenate item information into a text string
def process_text(chicken_items):
    processed_items = []
    for item in chicken_items:
        # Combine name, type, and allergens into a string
        name_type = f"{item['name']} {item['type']}"
        allergens = " ".join(item['allergens']) if item['allergens'] else "No allergens"
        processed_text = f"{name_type} {allergens}"

        processed_items.append({
            'id': item['id'],
            'text': processed_text,
            'nutritionalInfo': item['nutritionalInfo'],
            'available': item['available']
        })
    return processed_items

# Process the chicken items to get text representation
processed_chicken_items = process_text(restructured_chicken)
     
# Creating an Empty list which we will be extending to include the entire restructured menu
menu = []
     
# Printing the menu list
menu

# Example output
for item in processed_chicken_items:
    print(item)

# Function to concatenate item information into a text string
def process_text(chicken_items):
    processed_items = []
    for item in chicken_items:
        # Combine name, type, and allergens into a string
        name_type = f"{item['name']} {item['type']}"
        allergens = " ".join(item['allergens']) if item['allergens'] else "No allergens"
        processed_text = f"{name_type} {allergens}"

        processed_items.append({
            'id': item['id'],
            'text': processed_text
        })
    return processed_items

# Process the chicken items to get text representation
processed_chicken_items = process_text(restructured_chicken)

# Example output
for item in processed_chicken_items:
    print(item)

# Extending the menu list to include the Restructured Chicken Menu
menu.extend(processed_chicken_items)
     
# Printing the menu list to view the updated items in the list
menu

# Initialize a list to hold restructured drink items
restructured_drinks = []

# Iterate over the "Drinks" category in your original JSON structure
for drink_id, details in menu_data["Drinks"].items():
    drink_name = details[0]
    price = details[1]
    # Some drinks might not have 'nutritionalInfo', so we use .get() method to safely extract it
    nutritional_info = details[2].get('nutritionalInfo', {})
    available = details[2].get('available', False)

    # Create a new dictionary for each drink including all its details and a 'type' field
    restructured_drink = {
        "id": drink_id,
        "name": drink_name,
        "type": "Drink",
        "price": price,
        "nutritionalInfo": nutritional_info,
        "available": available
    }

    # Append this dictionary to the list
    restructured_drinks.append(restructured_drink)
     
print(restructured_drinks)

def process_drink_text(drink_items):
    processed_items = []
    for item in drink_items:
        # Combine name and type
        name_type = f"{item['name']} {item['type']}"

        # Handle allergens, defaulting to "No allergens" if none are present
        allergens = " ".join(item['nutritionalInfo'].get('allergens', ['No allergens'])) if 'nutritionalInfo' in item and 'allergens' in item['nutritionalInfo'] else "No allergens"

        processed_text = f"{name_type} {allergens}"

        processed_items.append({
            'id': item['id'],
            'text': processed_text
        })
    return processed_items

# Process the drinks items to get text representation
processed_drinks_items = process_drink_text(restructured_drinks)
     

# Example output
for item in processed_drinks_items:
    print(item)

# Extending the menu list to include the Restructured Drinks Menu
menu.extend(processed_drinks_items)
     

# Printing the menu list to view the updated items in the list
menu
     
# New structure for items including nutritional information handling
restructured_burgers = []

# Iterate over Burgers
for burger_key, burger_value in menu_data["Burgers"].items():
    # Initialize a dictionary for each burger
    burger_dict = {
        "id": burger_key,
        "name": burger_value[0],
        "price": burger_value[1],
        "type": "Burger",
        "available": burger_value[2].get("available", True)  # Default to True if not specified
    }

    # Check if nutritionalInfo exists, then include it
    if "nutritionalInfo" in burger_value[2]:
        burger_dict["nutritionalInfo"] = burger_value[2]["nutritionalInfo"]

    # Append the burger dictionary to the items list
    restructured_burgers.append(burger_dict)

print(restructured_burgers)

def process_burger_text(burger_items):
    processed_items = []
    for item in burger_items:
        # Combine name and type
        name_type = f"{item['name']} {item['type']}"

        # Check for allergens in nutritionalInfo, defaulting to "No allergens" if none are present
        allergens = " ".join(item['nutritionalInfo'].get('allergens', ['No allergens'])) if 'nutritionalInfo' in item and 'allergens' in item['nutritionalInfo'] else "No allergens"

        processed_text = f"{name_type} {allergens}"

        processed_items.append({
            'id': item['id'],
            'text': processed_text
        })
    return processed_items

# Assuming restructured_burgers is your list of burgers with the new structure
processed_burgers_items = process_burger_text(restructured_burgers)
     
# Example output
for item in processed_burgers_items:
    print(item)

# Extending the menu list to include the Restructured Burgers Menu
menu.extend(processed_burgers_items)
     
# Printing the menu list to view the updated items in the list
menu

# New structure for sauces
restructured_sauces = []

# Iterate over the "Sauces" section
for sauce_id, details in menu_data["Sauces"].items():
    sauce_dict = {
        "id": sauce_id,
        "name": details[0],
        "price": details[1],
        "type": "Sauce",
        # Default availability to True if not specified
        "available": details[2].get("available", True)
    }
    # Add the structured sauce dictionary to the sauces list
    restructured_sauces.append(sauce_dict)
     
print(restructured_sauces)

def process_sauce_text(sauce_items):
    processed_items = []
    for item in sauce_items:
        # Since there's no nutritional info or allergens provided, just combine name and type
        name_type = f"{item['name']} {item['type']}"

        processed_text = name_type  # For sauces, we might not have allergens or other detailed info

        processed_items.append({
            'id': item['id'],
            'text': processed_text
        })
    return processed_items

# Process the sauces items to get text representation
processed_sauces_items = process_sauce_text(restructured_sauces)
     
# Example output
for item in processed_sauces_items:
    print(item)

# Extending the menu list to include the Restructured Sauces Menu
menu.extend(processed_sauces_items)
     
# Printing the menu list to view the updated items in the list
menu

# Initialize a list to hold restructured drink items
restructured_sd = []

# Iterate over the "Drinks" category in your original JSON structure
for sd_id, details in menu_data["Side dishes"].items():
    sd_name = details[0]
    price = details[1]
    # Some drinks might not have 'nutritionalInfo', so we use .get() method to safely extract it
    nutritional_info = details[2].get('nutritionalInfo', {})
    available = details[2].get('available', False)

    # Create a new dictionary for each drink including all its details and a 'type' field
    restructured_dict = {
        "id": sd_id,
        "name": sd_name,
        "type": "Side dish",
        "price": price,
        "nutritionalInfo": nutritional_info,
        "available": available
    }

    # Append this dictionary to the list
    restructured_sd.append(restructured_dict)
     
restructured_sd

def process_side_dish_text(side_dish_items):
    processed_items = []
    for item in side_dish_items:
        # Combine name and type
        name_type = f"{item['name']} {item['type']}"

        # Handle allergens, defaulting to "No allergens" if none are present
        allergens = " ".join(item['nutritionalInfo'].get('allergens', ['No allergens'])) if 'nutritionalInfo' in item and 'allergens' in item['nutritionalInfo'] and item['nutritionalInfo']['allergens'] else "No allergens"

        processed_text = f"{name_type} {allergens}"

        processed_items.append({
            'id': item['id'],
            'text': processed_text
        })
    return processed_items

# Process the side dishes items to get text representation
processed_side_dishes_items = process_side_dish_text(restructured_sd)

# Example output
for item in processed_side_dishes_items:
    print(item)

# Extending the menu list to include the Restructured Side Dish Menu
menu.extend(processed_side_dishes_items)
     
# Printing the menu list to view the updated items in the list
menu

# Initialize a list to hold restructured drink items
restructured_dessert = []

# Iterate over the "Drinks" category in your original JSON structure
for dessert_id, details in menu_data["Desserts"].items():
    dessert_name = details[0]
    price = details[1]
    # Some drinks might not have 'nutritionalInfo', so we use .get() method to safely extract it
    nutritional_info = details[2].get('nutritionalInfo', {})
    available = details[2].get('available', False)

    # Create a new dictionary for each drink including all its details and a 'type' field
    restructured_dessert_dict = {
        "id": dessert_id,
        "name": dessert_name,
        "type": "Desserts",
        "price": price,
        "nutritionalInfo": nutritional_info,
        "available": available
    }

    # Append this dictionary to the list
    restructured_dessert.append(restructured_dessert_dict)
     
restructured_dessert

def process_dessert_text(dessert_items):
    processed_items = []
    for item in dessert_items:
        # Combine name and type
        name_type = f"{item['name']} {item['type']}"

        # Handle allergens, defaulting to "No allergens" if none are present
        allergens = " ".join(item['nutritionalInfo'].get('allergens', ['No allergens'])) if 'nutritionalInfo' in item and 'allergens' in item['nutritionalInfo'] and item['nutritionalInfo']['allergens'] else "No allergens"

        processed_text = f"{name_type} {allergens}"

        processed_items.append({
            'id': item['id'],
            'text': processed_text
        })
    return processed_items

# Process the desserts items to get text representation
processed_desserts_items = process_dessert_text(restructured_dessert)
     
# Example output
for item in processed_desserts_items:
    print(item)

# Extending the menu list to include the Restructured Dessert Menu
menu.extend(processed_desserts_items)
     
# Printing the menu list to view the updated items in the list
menu

# Initialize a list to hold restructured drink items
restructured_vegetarian = []

# Iterate over the "Drinks" category in your original JSON structure
for vegetarian_id, details in menu_data["Vegetarian"].items():
    vegetarian_name = details[0]
    price = details[1]
    # Some drinks might not have 'nutritionalInfo', so we use .get() method to safely extract it
    nutritional_info = details[2].get('nutritionalInfo', {})
    available = details[2].get('available', False)

    # Create a new dictionary for each drink including all its details and a 'type' field
    restructured_vegetarian_dict = {
        "id": vegetarian_id,
        "name": vegetarian_name,
        "type": "Vegetarian",
        "price": price,
        "nutritionalInfo": nutritional_info,
        "available": available
    }

    # Append this dictionary to the list
    restructured_vegetarian.append(restructured_vegetarian_dict)
     
restructured_vegetarian

def process_vegetarian_text(vegetarian_items):
    processed_items = []
    for item in vegetarian_items:
        # Combine name and type
        name_type = f"{item['name']} {item['type']}"

        # Handle allergens, defaulting to "No allergens" if none are present
        allergens = " ".join(item['nutritionalInfo'].get('allergens', ['No allergens'])) if 'nutritionalInfo' in item and 'allergens' in item['nutritionalInfo'] and item['nutritionalInfo']['allergens'] else "No allergens"

        processed_text = f"{name_type} {allergens}"

        processed_items.append({
            'id': item['id'],
            'text': processed_text
        })
    return processed_items

# Process the vegetarian items to get text representation
processed_vegetarian_items = process_vegetarian_text(restructured_vegetarian)
     
# Example output
for item in processed_vegetarian_items:
    print(item)

# Extending the menu list to include the Restructured Vegetarian Menu
menu.extend(processed_vegetarian_items)
     
# Printing the menu list to view the updated items in the list
menu

# Initialize variables
id_to_number = {}
number_to_id = {}
current_number = 1  # Start numbering from 1

# Iterate over each item in the dataset and assign numbers to IDs
for item in menu:
    item_id = item['id']
    # Check if the ID already has a number assigned
    if item_id not in id_to_number:
        # Assign a new number to the ID
        id_to_number[item_id] = current_number
        number_to_id[current_number] = item_id
        current_number += 1  # Increment the number for the next ID
     
# Update IDs in the menu to their corresponding numbers
for item in menu:
    item['id'] = id_to_number[item['id']]
     
# Example output
print("ID to Number Mapping:", id_to_number)
print("Number to ID Mapping:", number_to_id)
print("Updated Menu:", menu)

id_to_number

number_to_id

# Printing the menu list to view the updated items in the list
menu

# Simulate a file-like object for gensim LineSentence
text_data = "\n".join([item['text'] for item in menu])
file_like_text_data = StringIO(text_data)

# Training the Word2Vec model
model = Word2Vec(LineSentence(file_like_text_data), vector_size=100, window=5, min_count=1, workers=4)

# Converting text to vectors
vector_data = []
for item in menu:
    words = item['text'].split()
    vector = np.mean([model.wv[word] for word in words if word in model.wv], axis=0)
    vector_data.append({'id': item['id'], 'vector': vector})
     
# Now vector_data contains the vectors for each item
for item in vector_data:  # Example: showing vectors for the first two items
    print(item['id'], item['vector'])

 # Assuming each vector is 100-dimensional
dimension = 100
index = AnnoyIndex(dimension, 'angular')  # Initialize Annoy index

# Insert vectors into the index, assuming vector_data is a list of dictionaries as shown in your output
for item in vector_data:
    item_id = item['id']  # This should already be an integer
    vector = item['vector']
    index.add_item(item_id, vector)  # Directly use item_id without conversion

# Build the index
index.build(10)  # 10 trees

# Save the index to disk (optional but recommended for persistence)
index.save('menu_index.ann')

# Assuming 'vector_data' list's 'id' values have been converted to integers as per the mapping
first_item_id = vector_data[0]['id']  # This is already an integer now
first_vector = index.get_item_vector(first_item_id)

print(f"Vector for ID {first_item_id}: {first_vector}")