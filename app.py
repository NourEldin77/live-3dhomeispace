#!/usr/bin/python3
from flask import Flask, render_template, url_for, flash, redirect


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)