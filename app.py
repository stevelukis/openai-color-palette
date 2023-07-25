import json

import openai
from flask import Flask, render_template, request, jsonify
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_SECRET_KEY"]

app = Flask(__name__, template_folder="templates")

prompt = """"You will create color palettes based on the input.
The number of colors should be between 2 and 6. Only output the necessary colors.

Output format: json array of hexadecimal color.
Example: ["#F2A900", "#FFDE00", "#D83F67", "#C11B17"]

Input: %s colors

Output:
"""


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    data = json.loads(request.data)
    query = data['query']
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt % query,
        max_tokens=200,
        stop=["\n"]
    )
    return jsonify(json.loads(response["choices"][0]["text"]))



if __name__ == '__main__':
    app.run()
