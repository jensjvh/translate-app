from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "Initial"
