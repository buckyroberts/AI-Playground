from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

anthropic = Anthropic()

completion = anthropic.completions.create(
    prompt=f'{HUMAN_PROMPT} Which NHL team plays in Pittsburgh?{AI_PROMPT}',
    model='claude-2',
    max_tokens_to_sample=300,
)

print(completion)
print(completion.completion)
