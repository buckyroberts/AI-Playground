from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
#   model="dall-e-2",
  prompt="Painting of a red farmhouse with a tree in a peaceful valley with a stream and mountains in the background",
  size="1024x1024",
  quality="standard",
  n=1,
#   n=2,
)

image_url = response.data[0].url
# image_url_2 = response.data[1].url

print(image_url)
# print()
# print(image_url_2)
