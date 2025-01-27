import os, json, requests
from dotenv import load_dotenv

load_dotenv()

CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_TOKEN")

def answer_user_question(question: str):
    headers = {"Authorization": f"Bearer {CLOUDFLARE_API_KEY}"}
    model = "@cf/baai/bge-small-en-v1.5"
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{model}"

    payload = json.dumps({"prompt": question})