KnotebookLM

Overview

KnotebookLM is a RAG system that sends POST requests containing text and documents. Currently, it handles request submission and embedding creation. Will expand code in future.

Models

The system uses Google Generative AI for embeddings, with plans to incorporate LLM prompt interactions. Note: The API key is currently hard-coded.




api.py

This sets upnew endpoints to handle POST requests. It extracts id's and text from the request's JSON body, splits the text into chunks using split_text, and generates embeddings from documents. It returns a JSON response with the id's.

embed_and_store.py

The embedding code configures uses Google Generative AI embeddings with the text-embedding. The add_documents function adds documents to the vector store and stores their embeddings(kind of self explanitory).

post.py

This code sends a JSON file containing a sample text and id's  to the Flask server's endpoint. It uses the requests library to make the POST request with given text.It then prints the response JSON containing embedding IDs.

split.py

This code defines the split_text function that takes text and id's as inputs. It creates a document with the text. Using RecursiveCharacterTextSplitter, it splits the text into chunks of 500 characters.

test_split.py

This code tests out the split_text function.


How to Start

Add your Google API key if you want to send a .env file.

Provide a text input or use the one given.

Run python api.py to start the web server.

Open the generated website in your browser.

Run python post.py to send a POST request.

If successful , the response will include the number of text splits (based on chunk size and text length).

If failed, an error status code will pop up.


If you want to make a request, see post.py
