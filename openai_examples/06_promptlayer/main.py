import os

import promptlayer

openai = promptlayer.openai
openai.api_key = os.getenv('OPENAI_API_KEY')
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')

"""
Makes your request to OpenAI and then log the request to PromptLayer
"""

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt='Recommend a book.',
    max_tokens=64,
    pl_tags=['movies']
)

print(response)
