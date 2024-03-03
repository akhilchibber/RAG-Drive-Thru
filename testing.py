# Defining a function to test a given query by the customer
def query_testing(query):
  # Start the timer
  start_time = time.time()

  # query = "Can I get a Popcorn Chicken?"
  # query = "Can you please order a Pepsi for me?"

  # RAG based Processing
  processed_query = process_query(query)  # Assuming process_query is your function from the previous step
  query_vector_representation = query_to_vector(processed_query, model)
  query_vector = query_vector_representation # Your query vector here
  similar_items = find_similar_items(query_vector_representation, n = 3)  # Adjust `n` as needed
  top_similar_items = find_most_similar(query_vector_representation, vector_data, top_n=3)
  similarity_index = top_similar_items[0][0]
  matched_item_details = retrieve_matched_items(similarity_index, menu_data, mapping)
  response = generate_response(matched_item_details)

  # End the timer
  end_time = time.time()

  # Calculate the duration in milliseconds
  duration_ms = (end_time - start_time) * 1000

  # Print the response and the time taken
  print(response)
  print(f"Response generated in {duration_ms:.2f} milliseconds.")
     
query = "Can you please order a Crispy Tenders for me?"
query_testing(query)