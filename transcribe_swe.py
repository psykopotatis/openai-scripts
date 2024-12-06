import requests
import os
import json

# Load the OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found!")

url = "https://api.openai.com/v1/audio/transcriptions"

headers = {
    "Authorization": f"Bearer {api_key}",
}

# Folder containing movie files
movies_folder = os.path.join(os.path.dirname(__file__), "__ibra")

# Check if the folder exists
if not os.path.exists(movies_folder):
    raise FileNotFoundError(f"The folder '__ibra' was not found in the script directory.")

# Iterate over all movie files in the folder
for filename in os.listdir(movies_folder):
    if filename.lower().endswith(('.mp4', '.mkv', '.avi', '.mov', '.mp3')):  # Add supported extensions here
        file_path = os.path.join(movies_folder, filename)

        # Check if JSON file already exists
        json_filename = os.path.splitext(filename)[0] + ".json"
        json_path = os.path.join(movies_folder, json_filename)
        if os.path.exists(json_path):
            print(f"Skipping {filename}, JSON file already exists: {json_path}")
            continue

        print(f"Processing file: {filename}")

        # Open the file for reading
        with open(file_path, 'rb') as file:
            files = {
                'file': (filename, file),
            }
            data = {
                'model': 'whisper-1',
                'language': 'sv'  # ISO 639-1 code for Swedish
            }

            # Send the file to OpenAI API
            print("[GET] " + url)
            response = requests.post(url, headers=headers, files=files, data=data)
            print(response)

            if response.status_code == 200:
                transcription = response.json()
                print(f"Transcription successful for: {filename}")

                # Save the transcription to the JSON file
                with open(json_path, 'w', encoding='utf-8') as json_file:
                    json.dump({
                        "filename": filename,
                        "transcription": transcription.get("text", ""),
                    }, json_file, ensure_ascii=False, indent=4)

                print(f"Saved transcription to: {json_path}")
            else:
                print(
                    f"Failed to transcribe {filename}. Status code: {response.status_code}, Response: {response.text}")
