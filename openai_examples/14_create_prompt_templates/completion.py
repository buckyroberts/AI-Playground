import os
import promptlayer
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')
OpenAI = promptlayer.openai.OpenAI
client = OpenAI()

# Create a prompt template
template = {
    'input_variables': ['food', 'recipes_string'],
    'template': 'My favorite food is {food}\n\n{recipes_string}',
    'template_format': 'f-string',
}

promptlayer.prompts.publish("recipe_template", prompt_template=template)
