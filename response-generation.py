def generate_response(matched_item):
    # Extracting item details from the matched item
    item_name, price, item_info = matched_item
    response = f"You have ordered {item_name}, priced at ${price}."
    return response

# Input example
# matched_item = ["Popcorn Chicken", 4, {'nutritionalInfo': {'kcal': 350, 'fat': 20, 'protein': 25, 'itemId': 6, 'allergens': ['wheat', 'soy']}, 'available': False}]
matched_item = matched_item_details
     
# Generating the response
response = generate_response(matched_item)
print(response)
