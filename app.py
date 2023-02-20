from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import project_p4 as chat

app = Flask(__name__)
CORS(app)

params = chat.initialize()
answers = []
@app.post("/message")
def message():
    print("Entered message()")
    text = request.get_json().get("message")
    print("\n\nTHE TEXT IS :", text)
    prev = request.get_json().get("prompt")
    print("\n\nTHE PROMPT IS :", prev,'\n\n')
    if text == "END":
        return
    print("about to call chat.reply()")
    response = chat.reply("Are you excited for the upcoming FIFA World Cup?", text, params, answers)
    prompt = "THIS IS THE ENXT PROMPT"
    print("Called chat.reply()")
    message = {"answer": response, "nextPrompt": prompt}
    print("\n\n\nANSWERS  =  ", answers, "\n\n\n")
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)