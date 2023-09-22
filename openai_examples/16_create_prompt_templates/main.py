import os

import promptlayer

openai = promptlayer.openai
openai.api_key = os.getenv('OPENAI_API_KEY')
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')

template = {
    'input_variables': ['food', 'recipes_string'],
    'template': 'My favorite food is {food}\n\n{recipes_string}',
    'template_format': 'f-string',
}

promptlayer.prompts.publish("recipe_template", prompt_template=template)
