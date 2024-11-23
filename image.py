import requests
import os
import json

# Load the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Define the endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Set up the headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Define the data for the image generation request
data = {
    "model": "dall-e-3",
    "prompt": "A cute baby kitten",
    "n": 1,
    "size": "1024x1024"
}

# Make the POST request to the OpenAI API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()
    for image_info in response_data['data']:
        print(f"Image URL: {image_info['url']}")
        print(f"Revised Prompt: {image_info['revised_prompt']}")
else:
    print(f"Failed to generate image. Status code: {response.status_code}")
    print(f"Response: {response.text}")
