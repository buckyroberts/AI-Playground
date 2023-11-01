import os

import promptlayer

openai = promptlayer.openai
openai.api_key = os.getenv('OPENAI_API_KEY')
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')

"""
All PromptLayer requests have unique IDs, and these can be optionally returned when logging the request.
Using PromptLayer (and the request ID) we can score a request with an integer 0 - 100.
This is most often used to understand how effective certain prompts are in production.
"""

response, pl_request_id = openai.Completion.create(
    engine='text-davinci-003',
    prompt='What is the capital of New York?',
    max_tokens=64,
    pl_tags=['getting_started_example'],
    return_pl_id=True  # Make sure to set this to True
)

print(response)
print(pl_request_id)

answer = response.choices[0].text
print(answer)
correct_answer = 'albany' in answer.lower()

# Log score to PromptLayer
promptlayer.track.score(
    request_id=pl_request_id,
    score=100 if correct_answer else 0,
)
