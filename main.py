from flask import Flask, render_template, request
import pandas
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/documentation/')
def about():
    return render_template('about.html')

@app.route('/weather/<station>/<date>')
def weather(station, date):
    #df = pandas.read_csv()
    #temperature = df[]['temperature'].values
    temperature = 67
    return {
        'station': station,
        'date': date,
        'temperature': temperature
    }

if __name__ == '__main__':
    app.run(debug=True)