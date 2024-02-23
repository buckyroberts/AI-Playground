import promptlayer
Anthropic = promptlayer.anthropic.Anthropic

anthropic = Anthropic()
message = anthropic.messages.create(
    model="claude-2.1",
    max_tokens=200,
    system="You area helpful assistant. You only answer the exact question asked, you don't add any additional information to the answer.",
    messages=[
        {"role": "user", "content": "Which NHL team plays in Pittsburgh?"}
    ]
)

print(message.content[0].text)
