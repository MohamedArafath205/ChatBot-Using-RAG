from flask import Flask, request
from answer import answer_user_question

app = Flask(__name__)

@app.route("/ask-question", methods=["POST", "GET"])
def ask_question():
    json_content = request.json
    question = json_content.get('question')

    answer = answer_user_question(question)
    return {"question": question, "answer": answer}

@app.route("/")
def show_api_info():
    return {
        "name": "RAG ChatBot API",
        "endpoints": [
            {
                "path": "/ask-question",
                "methods": ["POST", "GET"],
                "description": "Ask a question and get an AI-generated answer"
            }
        ]
    }
if __name__ == "__main__":
    app.run()