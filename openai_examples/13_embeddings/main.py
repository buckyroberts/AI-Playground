import numpy as np
from openai import OpenAI

client = OpenAI()

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(input, model):
    return client.embeddings.create(
        input=input,
        model=model,
    )

MODEL = 'text-embedding-ada-002'

response = get_embedding('corn', MODEL)
print(response)
print(len(response.data[0].embedding))

response = get_embedding(["cat", "feline"], MODEL)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between 'cat' and 'feline': {score}")

response = get_embedding(["elephant", "microscope"], MODEL)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between 'elephant' and 'microscope': {score}")
