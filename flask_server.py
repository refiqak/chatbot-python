from flask import Flask, jsonify,make_response,request
from flask_cors import CORS
from chatbot import response_question
app = Flask(__name__)
CORS(app)

@app.route("/chatbot", methods=["POST"])
def chatbot():
    question = request.json['question']
    response = response_question(question)
    return jsonify(answer=response)
    
