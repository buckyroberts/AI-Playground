import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

"""
Bucky: Hi grandma!
Bucky: Give me a suggestion on what to eat for lunch.
Bucky: What is the recipe for that?
"""

# Initialize conversation with a system message
messages = [{'role': 'system', 'content': 'You are a sweet old helpful grandma.'}]

while True:
    user_text = input('Bucky: ')

    # Add the user message to the conversation history
    messages.append({'role': 'user', 'content': user_text})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0.5,
        max_tokens=1024
    )

    granny_response = response.choices[0].message.content
    print(f'Granny: {granny_response}')

    # Add grandmas message to the conversation history
    messages.append({'role': 'system', 'content': granny_response})
