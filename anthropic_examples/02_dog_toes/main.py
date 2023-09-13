import promptlayer
import os

anthropic = promptlayer.anthropic
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

completion = client.completions.create(
    prompt=f'{anthropic.HUMAN_PROMPT} How many toes do dogs have? {anthropic.AI_PROMPT}',
    stop_sequences=[anthropic.HUMAN_PROMPT],
    model='claude-v1-100k',
    max_tokens_to_sample=100,
    pl_tags=['animal-toes']
)

print(completion)
print(completion.completion)
