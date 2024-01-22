import os
import promptlayer

promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
OpenAI = promptlayer.openai.OpenAI
client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a helpful {type} assistant. You only answer {type} related questions. " +
        "Anything that isn't related to {type} will be politely declined and you will gently correct " + 
        "the user.",
    },
]

promptlayer.prompts.publish(
    prompt_name="assistant_type_2",
    prompt_template={
        "input_variables": [ "type" ],  # list them here if it has any
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
    },
)