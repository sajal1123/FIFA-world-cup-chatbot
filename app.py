from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import project_p4 as chat

app = Flask(__name__)
CORS(app)

params = chat.initialize()
answers = []
@app.post("/message")
def message():
    
    text = request.get_json().get("message")
    print("\n\nTHE TEXT IS :", text)
    prev = request.get_json().get("prompt")
    print("\n\nTHE PROMPT IS :", prev,'\n\n')
    if text == "END":
        return

    response = chat.reply("Who is your favorite player?", text, params, answers)
    
    message = {"answer": response}

    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)