# Restaurant Drive-Thru Order Processing Enhancement
<p align="center">
  <img src="https://github.com/akhilchibber/RAG-Drive-Thru/blob/main/Drive-thru.png?raw=true" alt="earthml Logo">
</p>

## Dataset
The menu.json dataset used in this project can be found at [Menu JSON Dataset](https://github.com/akhilchibber/RAG-Drive-Thru/blob/main/menu.json). 

## Overview
This project which is a Take Home Assignment which I got from [VOX AI](https://voxai.tech/) aims to revolutionize the drive-thru ordering process in restaurants by implementing a Retrieval-Augmented Generation (RAG) system. It leverages advanced NLP techniques to automate and accurately respond to customer inquiries about menu items in real-time, enhancing the overall customer experience.

## Components

1. **Vector Database Setup:** Creation of an in-memory vector database to store menu items as vector representations for efficient semantic similarity matching.

2. **Query Processing:** Interpreting customer queries, extracting relevant information, and converting it into a vector form to find the best matching menu items.

3. **Response Generation:** Using retrieved information to generate clear and concise responses to customer inquiries, detailing matched menu items.
<p align="center">
  <img src="https://github.com/akhilchibber/RAG-Drive-Thru/blob/main/VOX-AI.png?raw=true" alt="earthml Logo">
</p>

## Current Capabilities
This project is a preliminary implementation of a voice-based food ordering system. Currently, it is designed to handle basic queries, such as directly ordering specific items *(e.g. "Can you please order Popcorn for me?", "I want Crispy Tenders", "I would like to order a Pepsi", etc. or any other item available in the Menu but not Meals)*. The current version supports simple item recognition and pricing information based on vector matching from a structured dataset. Although after matching the user query with vector db, the matched dataset includes detailed information on nutritional content, allergens, and availability, these features are not yet incorporated into the response system but are straight forward to add in future iterations based on the current implementation.
<p align="center">
  <img src="https://github.com/akhilchibber/RAG-Drive-Thru/blob/main/RAG.png?raw=true" alt="earthml Logo">
</p>

## Dependencies
To run the project, ensure you have the following libraries:

- **spaCy:** For natural language processing. Ensure to download the English model with `python -m spacy download en_core_web_sm`.
- **numpy:** for numerical computations
- **gensim**: for Word2Vec model and text processing
- **annoy**: for building and querying the vector database
- **sklearn**: for using vector similarity measures outside of Annoy

You can install these dependencies using pip:

```bash
pip install spacy numpy gensim annoy scikit-learn
```

## Getting Started
To get started with this project:

1. Clone this repository to your local machine.
2. Ensure you have Jupyter Notebook installed and running.
3. Install the required dependencies.
4. Download the "Menu JSON Dataset" and place it in the designated directory.
5. Open and run the Jupyter Notebook "RAG_Assignment.ipynb" to run and evaluate the RAG Assignment.

## Contributing
We welcome contributions to enhance the functionality and efficiency of this script. Feel free to fork, modify, and make pull requests to this repository. To contribute:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request against the `main` branch.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact

Author: Akhil Chhibber

LinkedIn: https://www.linkedin.com/in/akhilchhibber/
