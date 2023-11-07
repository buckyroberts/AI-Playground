import os

import promptlayer

openai = promptlayer.openai
openai.api_key = os.getenv('OPENAI_API_KEY')
promptlayer.api_key = os.environ.get('PROMPTLAYER_API_KEY')

"""
Prompt templates are customizable prompt strings with placeholders for variables.
"""

city_rating = promptlayer.prompts.get('city_rating')

# You can also optionally pass version to get an older version of a prompt.
# By default, the newest version of a prompt is returned.
# city_rating = promptlayer.prompts.get('city_rating', version=1)

city_rating_template = city_rating['template']

variables = {
    'city': 'Pasadena',
    'interests': 'tacos, football, hiking'
}

response, pl_request_id = openai.Completion.create(
    engine='text-davinci-003',
    prompt=city_rating_template.format(**variables),
    return_pl_id=True
)

answer = response.choices[0].text
print(answer)

# Associate request with a prompt template
promptlayer.track.prompt(
    request_id=pl_request_id,
    prompt_name='city_rating',
    prompt_input_variables=variables
)

# Attach multiple key value pairs as metadata to a request
# Using the PromptLayer UI you can search for specific metadata
promptlayer.track.metadata(
    request_id=pl_request_id,
    metadata={
        'client_type': 'browser',
        'request_date': '2023-08-30',
        'username': 'bucky',
    }
)
