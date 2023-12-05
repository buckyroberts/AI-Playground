import os
import promptlayer

promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
OpenAI = promptlayer.openai.OpenAI
client = OpenAI()

"""
All PromptLayer requests have unique IDs, and these can be optionally returned
when logging the request. Using PromptLayer (and the request ID) we can score
a request with an integer 0 - 100. This is most often used to understand how
effective certain prompts are in production.
"""

response, pl_request_id = client.chat.completions.create(
    model='gpt-3.5-turbo-1106',
    messages=[{'role': 'user', 'content': 'What is the capital of New York?'}],
    max_tokens=64,
    pl_tags=['scoring_example'],
    return_pl_id=True  # Make sure to set this to True
)

print(response)
print()
print(pl_request_id)
print()
answer = response.choices[0].message.content
print(answer)
correct_answer = 'albany' in answer.lower()

# Log score to PromptLayer
promptlayer.track.score(
    request_id=pl_request_id,
    # score_name="capital_of_ny",
    score=100 if correct_answer else 0,
)
