from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AKASH_API_KEY"),
    base_url="https://chatapi.akash.network/v1"
)

try:
    response = client.chat.completions.create(
        model="Meta-Llama-3-1-70B-Instruct-FP8",
        messages=[
            {"role": "system", "content": "You are a social media expert."},
            {"role": "user", "content": "Hello, test"}
        ],
        max_tokens=100
    )
    
    print("Response type:", type(response))
    print("Response:", response)
    
    if hasattr(response, 'choices'):
        print("Content:", response.choices[0].message.content)
    else:
        print("Raw response (not expected format):", response)
        
except Exception as e:
    print(f"Error: {type(e).__name__}")
    print(f"Details: {e}")