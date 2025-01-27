import os, json, requests, chromadb
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

CLOUDFLARE_ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
CLOUDFLARE_API_KEY = os.getenv("CLOUDFLARE_API_TOKEN")

contents = []
filenames = []

path = "assets/"
for filename in os.listdir(path):
    if filename.endswith(".md"):
        with open(path + filename) as f:
            contents.append(f.read())
            filenames.append(filename)

df = pd.DataFrame({"filename": filenames, "contents": contents})

docs = []
ids = []

for row in df.itertuples():
    docs.append(row.contents)
    ids.append(row.filename)

# preparing Cloudflare AI model request 
# refer - https://www.youtube.com/watch?v=uxUoB1JopcQ
model = "@cf/baai/bge-small-en-v1.5"
url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/{model}"
payload = json.dumps({"text": docs})
headers = {"Authorization": f"Bearer {CLOUDFLARE_API_KEY}"}

response = requests.request("POST", url, headers=headers, data=payload)
result = response.json()

embeddings = result["result"]["data"]

# creating ChromaDB
client = chromadb.PersistentClient(path="./chroma")
collection = client.get_or_create_collection("Interviews")

collection.add(
    documents=docs,
    embeddings=embeddings,
    ids=ids,
)
