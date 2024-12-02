from flask import Flask, render_template, request, redirect
from transformers import pipeline

app = Flask(__name__)

# Load model when app is started
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-fi")

@app.route('/', methods = ["get", "post"])
def index():
    """
    Function for handling a route for the main page of the app.
    """
    output = None
    if request.method == "POST":
        input_text = request.form['dataInput']
        if len(input_text) == 0:
            return render_template("index.html", output="Please enter some text.")
        result = pipe(input_text)
        output = result[0]['translation_text']
        return render_template("index.html", prompt = input_text, output=output)

    return render_template("index.html")
