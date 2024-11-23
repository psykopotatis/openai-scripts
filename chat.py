from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Load environment variables from the .env file in the script's directory, overriding existing ones
load_dotenv(os.path.join(script_dir, '.env'), override=True)

# Fetch the API key from the environment
client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY')

def ask_openai(question):
    try:
        # Correct method for chat completions with GPT-4
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
            max_tokens=150,
            temperature=0.7
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except OpenAIError as e:
        return f"OpenAI API Error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    question = "hi, what is your memory?"
    answer = ask_openai(question)
    print(f"GPT-4 says: {answer}")
