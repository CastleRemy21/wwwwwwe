KnotebookLM

Overview

KnotebookLM is a RAG system that sends POST requests containing text and documents. Currently, it handles request submission and embedding creation. Will expand code in future.

Models

The system uses Google Generative AI for embeddings, with plans to incorporate LLM prompt interactions. Note: The API key is currently hard-coded.



Getting Started





Optionally, add your Google API key to a .env file.



Provide your desired text input or use the default.



Run python api.py to start the web server.





Open the generated website in your browser.



Run python post.py to send a POST request.





On success, the response will include the number of text splits (based on chunk size and text length).



On failure, an error status code will be displayed.

Making a Request

Refer to post.py for details on constructing requests.
