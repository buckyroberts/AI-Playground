import os
import promptlayer

promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
OpenAI = promptlayer.openai.OpenAI
client = OpenAI()

messages = [
    {
        "role": "user",
        "content": "What's the weather like in Boston?",
    }
]

functions = [
    {
        "name": "function_1",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    },
]

promptlayer.prompts.publish(
    prompt_name="test_function_params",
    prompt_template={
        "function_call": "auto",  # or {"name": function_name} if you want to make sure the function gets called.
        "input_variables": [],  # list them here if it has any
        "messages": [
            {
                "role": role,
                "prompt": {
                    "input_variables": [],  # list them here if it has any
                    "template": content,
                    "template_format": "f-string",  # or "jinja"
                    "validate_template": True,  # optional
                    "_type": "prompt",
                },
            } for (role, content) in map(lambda x: x.values(), messages)
        ],
        "functions": functions,
        "_type": "chat_promptlayer_langchain",  # important if using gpt-3.5-turbo or gpt-4
    },
)

response, pl_request_id = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=messages,
    functions=functions,
    function_call="auto",
    return_pl_id=True,
)

promptlayer.track.prompt(
    request_id=pl_request_id,
    prompt_name='test_function_params',
    prompt_input_variables={
        'city': 'Pasadena',
        'interests': 'tacos, football, hiking'
    }
)
