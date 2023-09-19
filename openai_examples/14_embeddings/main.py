import numpy as np
import openai

MODEL = 'text-similarity-ada-001'

response = openai.Embedding.create(
    input="corn",
    engine=MODEL,
)
print(response)
print(len(response['data'][0]['embedding']))

response = openai.Embedding.create(
    input=["cat", "feline"],
    engine=MODEL,
)
a = response['data'][0]['embedding']
b = response['data'][1]['embedding']
score = np.dot(a, b)
print(score)

response = openai.Embedding.create(
    input=["elephant", "microscope"],
    engine=MODEL,
)
a = response['data'][0]['embedding']
b = response['data'][1]['embedding']
score = np.dot(a, b)
print(score)
