import os
from dotenv import load_dotenv, find_dotenv
import groq

# Force reload environment variables
load_dotenv(find_dotenv(), override=True)

api_key = os.getenv('GROQ_API_KEY')
print(f"API Key found: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"API Key starts with: {api_key[:10]}...")

try:
    client = groq.Groq(api_key=api_key)
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": "Hello, this is a test message."}
        ],
        model="llama-3.3-70b-versatile",
        max_tokens=50
    )
    print("✅ API Key is valid!")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"❌ API Key error: {e}") 