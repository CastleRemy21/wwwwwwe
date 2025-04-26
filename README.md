KnotebookLM

Overview

KnotebookLM is a RAG system that sends POST requests containing text and documents. Currently, it handles request submission and embedding creation. Will expand code in future.

Models

The system uses Google Generative AI for embeddings, with plans to incorporate LLM prompt interactions. Note: The API key is currently hard-coded.



How to Start

Add your Google API key if you want to send a .env file.

Provide a text input or use the one given.

Run python api.py to start the web server.

Open the generated website in your browser.

Run python post.py to send a POST request.

If successful , the response will include the number of text splits (based on chunk size and text length).

If failed, an error status code will pop up.


If you want to make a request, see post.py
