from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Infinity2.0! 🚀"

@app.route("/chat", methods=["POST"])
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()

    # Simple rule-based logic
    if "hi" in user_message or "hello" in user_message:
        bot_reply = "Hello! 👋 I'm Infinity2.0. How can I help you today?"
    elif "your name" in user_message:
        bot_reply = "I'm Infinity2.0, your AI assistant 🤖"
    elif "bye" in user_message:
        bot_reply = "Goodbye! Have a great day 👋"
    else:
        bot_reply = "I'm still learning. Can you ask me something else?"

    return jsonify({"response": bot_reply})
