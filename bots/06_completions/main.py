import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

"""
Completions API (legacy)
- You provide a prompt, and the model returns a continuation of that prompt.
- Common uses might include generating a story, article writing, product descriptions, or simplifying complex topics

Chat Completions API
- This is designed to facilitate a more interactive, multi-turn conversation with the model.
"""

haiku = openai.Completion.create(
    model="text-davinci-003",
    prompt="Write a haiku about thenewboston.",
    max_tokens=64
)
print(haiku)

"""
Prompt engineering is about creating the right input to produce the desired output.

In order to get a highly relevant response, make sure that requests provide any important details or context. 
Otherwise you are leaving it up to the model to guess what you mean.
"""

bad_movie = openai.Completion.create(
    model="text-davinci-003",
    prompt="Recommend a movie.",
    max_tokens=64
)
print(bad_movie)

good_movie = openai.Completion.create(
    model="text-davinci-003",
    prompt=(
        "Recommend a thought-provoking movie from the 1990s. "
        "I prefer movies similar to Fight Club, Good Will Hunting."
    ),
    max_tokens=64
)
print(good_movie)

bad_question = openai.Completion.create(
    model="text-davinci-003",
    prompt="Who is the captain?",
    max_tokens=64,
    temperature=0
)
print(bad_question)

good_question = openai.Completion.create(
    model="text-davinci-003",
    prompt="Who was the captain of the Pittsburgh Penguins in 2001?",
    max_tokens=64,
    temperature=0
)
print(good_question)

"""
Another tip is to ask for specific structure
"""

structure = openai.Completion.create(
    model="text-davinci-003",
    prompt="Provide a bullet point pros and cons list about moving to the Philippines",
    max_tokens=1024
)
print(structure)
print(structure.choices[0].text)
