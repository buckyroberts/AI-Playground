import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Image.create_variation(
    image=open('./bucky.png', 'rb'),
    n=1,
    size='1024x1024'
)

image_url = response['data'][0]['url']
print(image_url)
