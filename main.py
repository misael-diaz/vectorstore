#!/usr/bin/env python3
import chromadb
document = """
A vector database, vector store or vector search engine is a
database that can store vectors (fixed-length lists of numbers) along with other
data items. Vector databases typically implement one or more Approximate Nearest
Neighbor algorithms, so that one can search the database with a query vector to
retrieve the closest matching database records.

Vectors are mathematical representations of data in a high-dimensional space. In
this space, each dimension corresponds to a feature of the data, with the number
of dimensions ranging from a few hundred to tens of thousands, depending on the
complexity of the data being represented. A vector's position in this space
represents its characteristics. Words, phrases, or entire documents, as well as
images, audio, and other types of data, can all be vectorized.

These feature vectors may be computed from the raw data using machine learning
methods such as feature extraction algorithms, word embeddings or deep
learning networks. The goal is that semantically similar data items receive
feature vectors close to each other.
"""
documents = [document]
ids = [i for i in range(len(documents))]
client = chromadb.Client() collection
= client.create_collection(name="collection")
collection.add(documents=documents, ids=ids)
