import os
from openai import OpenAI

from data.first_page import input_data
os.environ["OPENAI_API_KEY"] = "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"
# Set your OpenAI API key here
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()


def predict_intent(user_command):
    # Prepare the conversation context
    conversation = [
        {"role": "system", "content": "The following are user commands with their corresponding intents. Respond with "
                                      "the intent in a simple phrase format like 'open first page'."},
        # Add examples from your data as part of the system's instructions
        *[
            {"role": "system", "content": f"User command: '{item['text']}' Intent: {item['label']}"}
            for item in input_data[:5]  # Use a subset of examples to keep the prompt concise
        ],
        {"role": "user", "content": user_command}
    ]

    # Make the API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Adjust the model as needed
        messages=conversation,
        temperature=0.2,
        max_tokens=60
    )

    # Extract and return the predicted intent
    predicted_intent = response.choices[0].message.content.strip()
    return predicted_intent
