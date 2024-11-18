#!/usr/bin/env python3
import chromadb
with open("doc.txt", "r") as f:
    document = f.read()
documents = [document]
ids = [str(i) for i in range(len(documents))]
client = chromadb.Client()
collection = client.create_collection(name="collection")
collection.add(documents=documents, ids=ids)
results = collection.query(query_texts=["vector database"])
