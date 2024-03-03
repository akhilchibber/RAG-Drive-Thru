# Load the spaCy model
nlp = spacy.load("en_core_web_sm")
     
def process_query(query):
    # Process the query with spaCy
    doc = nlp(query)

    # Extract relevant parts of the query
    items = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    attributes = [token.lemma_ for token in doc if token.pos_ == 'ADJ']

    # Construct a representation similar to menu item entries
    query_representation = ' '.join(items + attributes)

    return query_representation

# Example Query
query = "Can I get a Popcorn Chicken?"
query_representation = process_query(query)

# Function to convert query representation to vector using the Word2Vec model
def query_to_vector(query_representation, model):
    words = query_representation.split()
    # Ensure all words are in the model's vocabulary
    vector = np.mean([model.wv[word] for word in words if word in model.wv], axis=0)
    return vector
     
# Example Usage
query = "Can I get a Popcorn Chicken?"
processed_query = process_query(query)  # Assuming process_query is your function from the previous step
query_vector_representation = query_to_vector(processed_query, model)

print(f"Query Vector: {query_vector_representation}")

# Assuming dimension is the dimensionality of your vectors
dimension = 100
index = AnnoyIndex(dimension, 'angular')

# Assuming you've already built and saved your index
index.load('menu_index.ann')  # Load the saved index

def find_similar_items(query_vector, n=1):
    """
    Find `n` most similar items in the vector database for the given query vector.

    Parameters:
    - query_vector: The vector representation of the user's query.
    - n: The number of similar items to retrieve.

    Returns:
    A list of tuples containing the index of the similar items and their similarity scores.
    """
    similar_items = index.get_nns_by_vector(query_vector, n, include_distances = True)
    return similar_items
     
# Example usage
query_vector = query_vector_representation # Your query vector here
similar_items = find_similar_items(query_vector_representation, n = 5)  # Adjust `n` as needed

print(f"Similar Items: {similar_items}")

# Assuming `vector_data` is your list of dictionaries with 'id' and 'vector' from the in-memory database
# And `query_vector` is the vector representation of your query

def find_most_similar(vector, vector_data, top_n=1):
    # Convert vector_data to a list of vectors for comparison
    vectors = [item['vector'] for item in vector_data]
    # Calculate cosine similarity between the query vector and all vectors in the database
    similarities = cosine_similarity([vector], vectors)[0]
    # Get the top N indices of the most similar vectors
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    # Retrieve IDs and similarities for the most similar items
    similar_items = [(vector_data[i]['id'], similarities[i]) for i in top_indices]
    return similar_items

# Example usage
top_similar_items = find_most_similar(query_vector_representation, vector_data, top_n=5)
print(f"Top Similar Items: {top_similar_items}")

top_similar_items

similarity_index = top_similar_items[0][0]
     
similarity_index

# Function to retrieve menu item details using vector ID
def retrieve_matched_items(vector_id, menu_data, mapping):
    # Translate vector ID to menu ID
    menu_id = mapping[vector_id]

    # Initialize result variable
    matched_item_details = {}

    # Iterate through menu categories and items
    for category, items in menu_data.items():
        if menu_id in items:
            matched_item_details = items[menu_id]
            break

    return matched_item_details
     
# Example usage
# vector_id = 36  # Example vector ID
vector_id = similarity_index

mapping = number_to_id

matched_item_details = retrieve_matched_items(vector_id, menu_data, mapping)

print(f"Matched Item Details: {matched_item_details}")