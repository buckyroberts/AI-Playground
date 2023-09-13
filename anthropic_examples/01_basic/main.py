import promptlayer

anthropic = promptlayer.anthropic

client = anthropic.Anthropic()

completion = client.completions.create(
    prompt=f'{anthropic.HUMAN_PROMPT} Which NHL team plays in Pittsburgh?{anthropic.AI_PROMPT}',
    model='claude-2',
    max_tokens_to_sample=300,
)

print(completion)
print(completion.completion)
