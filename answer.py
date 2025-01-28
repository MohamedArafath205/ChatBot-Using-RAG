import os, json, requests, chromadb
from dotenv import load_dotenv

load_dotenv()

CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_TOKEN")

def answer_user_question(question: str):
    headers = {"Authorization": f"Bearer {CLOUDFLARE_API_KEY}"}
    model = "@cf/baai/bge-small-en-v1.5"
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{model}"
    payload = json.dumps({"text": [question]})
    response = requests.request("POST", url, headers=headers, data=payload)
    question_result = response.json()
    client = chromadb.PersistentClient(path="./chroma")
    collection = client.get_or_create_collection("Interviews")
    result = collection.query(query_embeddings=question_result["result"]["data"], n_results=2)
    results = result["documents"]
    return get_response_from_llm(question, results)

def get_response_from_llm(question, results):
    headers = {"Authorization": f"Bearer {CLOUDFLARE_API_KEY}"}
    payload = create_payload(question, results[0][0])
    model = "@cf/meta/llama-3.1-8b-instruct"
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{model}"
    response = requests.request("POST", url, headers=headers, data=payload)
    question_result = response.json()

    return question_result["result"]["response"]


def create_payload(sentence, context):
    # input_prompt = (f"You are being interviewed by a company. Provide a brief summary of the question based on your knowledge. If you don't know the answer, just say that you don't know." 
    # f"Context: {context} \nQuestion: {sentence}"
    # )

    return json.dumps({
        "messages": [
            {
                "role": "system",
                "content": "You are being interviewed by a company. Provide a answer suitable to the question based on your knowledge. If you don't know the answer, just say that you don't know."
            },
            {
                "role": "user",
                "content": f"Context: {context}\nQuestion: {sentence}"
            }
        ]
    })

print(answer_user_question("What is the difference between bias and variance trade off ?"))