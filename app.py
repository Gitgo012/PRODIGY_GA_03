from flask import Flask, render_template, jsonify
import markovify
import os

app = Flask(__name__)

# Load the Markov model from the saved JSON
model_path = os.path.join(os.path.dirname(__file__), "markov_model.json")
with open(model_path, "r") as f:
    model_json = f.read()

markov_model = markovify.NewlineText.from_json(model_json)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    sentence = markov_model.make_sentence()
    return jsonify({"line": sentence or "Couldn't generate. Try again."})

if __name__ == "__main__":
    app.run(debug=True)
