import json

import openai
from flask import Flask, render_template, request, jsonify
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_SECRET_KEY"]

app = Flask(__name__, template_folder="templates")

messages = [
    {"role": "system",
     "content": "Create color palettes based on user's input. The number of colors should be between 2 and 6. Reply with JSON array of hexadecimal colors"},
    {"role": "user", "content": "Google colors"},
    {"role": "assistant", "content": """[ "#4285F4", "#34A853", "#FBBC05", "#EA4335" ]"""}
]


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    data = json.loads(request.data)
    query = data['query']

    prompt = [{"role": "user", "content": query}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages + prompt,
        max_tokens=200,
        temperature=0
    )
    return jsonify(json.loads(response["choices"][0]["message"]["content"]))


if __name__ == '__main__':
    app.run()
