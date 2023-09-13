import os
import openai
import json

openai.api_key = os.getenv('OPENAI_API_KEY')


# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)


def run():
    # Step 1: specify any available functions that the model can use
    # https://platform.openai.com/docs/api-reference/chat/create#functions
    functions = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            # The parameters the functions accepts, described as a JSON Schema object
            # https://json-schema.org/understanding-json-schema/
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                    },
                },
                "required": ["location"],
            },
        }
    ]

    # Step 2: send the conversation and available functions to GPT
    messages = [{"role": "user", "content": "What's the weather like in Boston?"}]
    first_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )

    print(first_response)
    print()

    first_response_message = first_response["choices"][0]["message"]

    # Step 3: check if GPT wanted to call a function
    # https://platform.openai.com/docs/api-reference/chat/create#messages-function_call
    if first_response_message.get("function_call"):
        # Step 4: call the function
        # only one function in this example, but you can have multiple
        available_functions = {
            "get_current_weather": get_current_weather,
        }
        function_name = first_response_message["function_call"]["name"]
        function_args = json.loads(first_response_message["function_call"]["arguments"])  # {'location': 'Boston, MA'}
        function_to_call = available_functions[function_name]
        function_return_value = function_to_call(
            location=function_args.get("location"),
            unit=function_args.get("unit"),
        )

        # Step 5: send the details about the function call and return value back to GPT

        # extend conversation with assistant's reply
        messages.append(first_response_message)

        # extend conversation with function response
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_return_value,
            }
        )

        # get a new response from GPT where it can see the function response
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )

        print(second_response)
        print()
        print(second_response.choices[0].message.content)


if __name__ == "__main__":
    run()
