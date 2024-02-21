from data.first_page import input_data
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Define input data
# input_data = [
#     {"text": "Show me the first page.", "label": "open first page"},
#     {"text": "Take me to the main screen.", "label": "open first page"},
#     {"text": "Navigate to the opening page, please.", "label": "open first page"},
#     # Add more examples as needed
# ]


# Function to classify text using OpenAI API
def classify_text(text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=text,
        max_tokens=50,
        stop=["\n", "."],
        temperature=0.7,
        n=1,
        logprobs=0,
        echo=True
    )
    predicted_label = response.choices[0].text.strip()
    return predicted_label


# Classify input data
for example in input_data:
    input_text = example["text"]
    desired_label = example["label"]

    # Use OpenAI API for classification
    predicted_label = classify_text(input_text)

    print(f"Input Text: {input_text}")
    print(f"Desired Label: {desired_label}")
    print(f"Predicted Label: {predicted_label}\n")
