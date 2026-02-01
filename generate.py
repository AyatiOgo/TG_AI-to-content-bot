import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AKASH_API_KEY"),
    base_url="https://chatapi.akash.network/api/v1"
)

MODEL = "Meta-Llama-3-1-70B-Instruct-FP8"

def generate_short_form(transcript: str):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a social media content expert. "
                    "Your job is to take video transcripts and turn them into "
                    "engaging, short-form posts suitable for TikTok, Instagram Reels, or YouTube Shorts. "
                    "Each post should be 60–100 words, punchy, and attention-grabbing."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Convert the following video transcript into 3 separate, "
                    f"engaging short-form social media posts. "
                    f"Number them 1, 2, and 3.\n\n"
                    f"Transcript:\n{transcript}"
                )
            }
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content


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