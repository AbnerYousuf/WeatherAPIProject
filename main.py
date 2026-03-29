from flask import Flask, render_template, request
import os

app = Flask("WeatherAPI")

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)