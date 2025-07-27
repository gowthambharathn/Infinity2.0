from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Infinity2.0! 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    # TODO: Replace this with your real AI model later
    bot_reply = f"Infinity2.0 received: '{user_message}' 🤖"

    return jsonify({"response": bot_reply})
