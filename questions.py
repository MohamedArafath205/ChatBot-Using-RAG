import os, json, requests
from dotenv import load_dotenv

load_dotenv()

CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_TOKEN")

def get_random_questions(topic: str):
    headers = {"Authorization": f"Bearer {CLOUDFLARE_API_KEY}"}
    payload = create_payload(topic)
    model = "@cf/meta/llama-3.1-8b-instruct"
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{model}"

    response = requests.post(url, headers=headers, data=payload)
    question_result = response.json()

    raw_response = question_result["result"]["response"]

    # Split into list based on line breaks
    questions = [q.strip() for q in raw_response.split("\n") if q.strip()]
    return questions

def create_payload(topic):
    return json.dumps({
        "messages": [
            {
                "role": "system",
                "content": (
                    f"You are an expert in generating interview questions."
                    f" Given only a topic, generate 5 different and random interview questions."
                    f" Only output the questions as a numbered list, nothing else. Be clear and concise."
                )
            },
            {
                "role": "user",
                "content": f"Topic: {topic}"
            }
        ]
    })