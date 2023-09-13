import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# Allow users to input their question
user_text = input('What can Granny help you with today? ')

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'You are a sweet old helpful grandma.'},
        {'role': 'user', 'content': user_text},
    ],
    temperature=0.5,
    max_tokens=1024
)

print(response)
print()
print(response.choices[0].message.content)
