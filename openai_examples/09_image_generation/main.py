import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Image.create(
    prompt='Painting of a red farmhouse with a tree in a peaceful valley with a stream and mountains in the background',
    n=1,
    size='1024x1024'
)

image_url = response['data'][0]['url']
print(image_url)
