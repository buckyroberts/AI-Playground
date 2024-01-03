from openai import OpenAI
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

client = OpenAI()

MODEL = 'text-embedding-ada-002'

response = client.embeddings.create(
    input="corn",
    model=MODEL,
)
print(response)
print(len(response.data[0].embedding))

response = client.embeddings.create(
    input=["cat", "feline"],
    model=MODEL,
)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between 'cat' and 'feline': {score}")

response = client.embeddings.create(
    input=["elephant", "microscope"],
    model=MODEL,
)
a = response.data[0].embedding
b = response.data[1].embedding
score = cosine_similarity(a, b)
print(f"Similarity score between 'elephant' and 'microscope': {score}")
