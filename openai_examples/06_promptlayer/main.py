import os
import promptlayer

promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
OpenAI = promptlayer.openai.OpenAI
client = OpenAI()

"""
Makes your request to OpenAI and then log the request to PromptLayer
"""

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        { 'role': 'system', 'content': 'You are a helpful assistant.' },
        { 'role': 'user', 'content': 'Who was the first president of the United States?' }
    ],
    temperature=0.5,
    max_tokens=64,
    pl_tags=['US Presidents']
)

print(response)
