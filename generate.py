import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
load_dotenv()

client = OpenAI(
    api_key=os.getenv("AKASH_API_KEY"),
    base_url="https://chatapi.akash.network/api/v1"
)

AKASH_API_KEY = os.getenv("AKASH_API_KEY")
AKASH_URL = "https://chatapi.akash.network/v1/chat/completions"
MODEL = "Meta-Llama-3-1-70B-Instruct-FP8"


AKASH_API_KEY = os.getenv("AKASH_API_KEY")
AKASH_URL = "https://api.akashml.com/v1/chat/completions"  
SHORT_FORM_MODEL = "deepseek-ai/DeepSeek-V3.2"             
BLOG_MODEL = "deepseek-ai/DeepSeek-V3.2"                 

HEADERS = {
    "Authorization": f"Bearer {AKASH_API_KEY}",
    "Content-Type": "application/json"
}


def generate_short_form(transcript: str):
    payload = {
        "model": SHORT_FORM_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a social media content expert. Turn transcripts into engaging short-form posts (60–100 words)."
            },
            {
                "role": "user",
                "content": f"Convert this transcript into 3 engaging short-form posts. Number them 1, 2, and 3.\n\nTranscript:\n{transcript}"
            }
        ],
        "max_tokens": 1000
    }

    response = requests.post(AKASH_URL, headers=HEADERS, json=payload)
    
    if response.status_code != 200:
        print("Akash API Error:", response.status_code, response.text)
        raise Exception("Akash request failed")
    
    data = response.json()

    posts = []
    for i, choice in enumerate(data["choices"], 1):
        text = choice["message"]["content"].strip()
        posts.append(f"📱 Post {i}:\n{text}")

    return "\n\n" + "\n\n" + ("-"*80 + "\n\n").join(posts)



def generate_blog_post(transcript: str):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional blog writer. "
                    "Your job is to take video transcripts and turn them into well-structured, "
                    "engaging blog posts. Include a strong introduction, clear sections with subheadings, "
                    "and a conclusion. Write in a professional but approachable tone."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Convert the following video transcript into a comprehensive blog post "
                    f"(800–1200 words). Include an introduction, main body with subheadings, "
                    f"and a conclusion.\n\n"
                    f"Transcript:\n{transcript}"
                )
            }
        ],
        max_tokens=2000
    )

    return response.choices[0].message.content