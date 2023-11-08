from openai import OpenAI

client = OpenAI()

"""
Request data

model
- ID of model to use.
- https://platform.openai.com/docs/models
- https://openai.com/pricing

messages
- A list of messages comprising the conversation so far.

temperature
- What sampling temperature to use, between 0 and 2.
- Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and 
  deterministic.

max_tokens
- The maximum number of tokens to generate in the chat completion.
"""

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Which NHL team plays in Pittsburgh?'},
    ],
    temperature=0.5,
    max_tokens=1024
)

"""
Response data: chat completion object

https://platform.openai.com/docs/api-reference/chat/object

{
  "id": "chatcmpl-7sz349tSCvgxedXZSHbl7XSt6Eein",
  "object": "chat.completion",
  "created": 1693338738,
  "model": "gpt-4-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The NHL team that plays in Pittsburgh is the Pittsburgh Penguins."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 12,
    "total_tokens": 36
  }
}
"""

# print(response)
# print()
print(response.choices[0].message.content)
