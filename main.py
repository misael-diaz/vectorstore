#!/usr/bin/env python3
import chromadb
import ollama
with open("doc.txt", "r") as f:
    document = f.read()
documents = [document]
embeddings = []
ids = []
model = "all-minilm"
for n, document in enumerate(documents):
    ids.append(str(n))
    res = ollama.embeddings(model=model, prompt=document)
    embedding = res["embedding"]
    embeddings.append(embedding)

client = chromadb.Client()
collection = client.create_collection(name="collection")
collection.add(documents=documents, embeddings=embeddings, ids=ids)
results = collection.query(query_texts=["vector database"])
