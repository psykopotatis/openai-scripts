import requests
import os

url = "https://api.openai.com/v1/audio/transcriptions"
# Load the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
print(api_key)

headers = {
    "Authorization": f"Bearer {api_key}",
}

# No need to specify full path, just use the filename
files = {
    'file': ('pod.mp3', open('pod.mp3', 'rb')),
}


data = {
    'model': 'whisper-1'
}

response = requests.post(url, headers=headers, files=files, data=data)

print(response.json())
