import promptlayer
import os

anthropic = promptlayer.anthropic
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

completion = client.messages.create(
    messages=[
        {
            'content': 'How many toes do dogs have?',
            'role': 'user',
        },
    ],
    temperature=0.0,
    system='Respond only in Yoda-speak',
    model='claude-3-haiku-20240307',
    max_tokens=256,
    pl_tags=['animal-toes']
)
print()
print(completion)
print()
print(completion.content[0].text)
print()
