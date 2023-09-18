import numpy as np
import openai

response = openai.Embedding.create(
    input="corn",
    engine="text-similarity-davinci-001"
)
print(response)

response = openai.Embedding.create(
    input=["cat", "feline"],
    engine="text-similarity-davinci-001",
)
a = response['data'][0]['embedding']
b = response['data'][1]['embedding']
score = np.dot(a, b)
print(score)

response = openai.Embedding.create(
    input=["elephant", "microscope"],
    engine="text-similarity-davinci-001",
)
a = response['data'][0]['embedding']
b = response['data'][1]['embedding']
score = np.dot(a, b)
print(score)
