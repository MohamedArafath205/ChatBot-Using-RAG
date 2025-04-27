import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_TOKEN")

def check_answer(question: str, answer: str):
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_KEY}",
        "Content-Type": "application/json",
    }
    
    payload = json.dumps({
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert evaluator for interview answers."
                    " Given a question and a user's answer, grade the answer on a scale of 1 to 10."
                    " Also provide a short 1-2 sentence feedback."
                    " Respond strictly in JSON format like this: {\"score\": number, \"feedback\": \"your feedback here\"}."
                    " Only output the JSON, nothing else."
                )
            },
            {
                "role": "user",
                "content": f"Question: {question}\nAnswer: {answer}"
            }
        ]
    })
    
    model = "@cf/meta/llama-3.1-8b-instruct"
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{model}"

    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code != 200:
        raise Exception(f"Failed to call AI API: {response.text}")

    response_data = response.json()
    raw_response = response_data["result"]["response"]

    try:
        evaluation = json.loads(raw_response)
    except json.JSONDecodeError:
        raise Exception(f"Invalid AI response: {raw_response}")

    return evaluation
