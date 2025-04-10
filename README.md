# KnotebookLM RAG Service
To explain the code I'm going to go through what each of the 5 .pys does

api.py - It creates a flask using the info from the Json folder
. then there's the text split function, which does what it is named, and there is the storage of the embedding id's.

embed_and_store.py - Starts by importing Langchain and Google gen ai. In this there is the vector storage and at the end of this code, there is the edition of documents.

post.py - This is just code to use on a test text.

split.py - Starts by importing document and reverse text splitter. This is the code that defines the earlier text split function used in api.py, that gets a document as input and returns a list of split documents as an output.

test_split.py - This is the testing for the split function.
