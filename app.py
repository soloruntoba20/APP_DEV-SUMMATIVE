import numpy as np
import csv
import pandas as pd
import requests
from flask import Flask, request, jsonify, render_template
import pickle
import dashboard

server = Flask(__name__)
app = dashboard.get_dash(server)
solar_model = pickle.load(open('solar.pkl', 'rb'))
wind_model = pickle.load(open('wind_data.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = solar_model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Power Output should be'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


@app.route('/upload', methods=['POST'])
def upload_schedule():
    if request.method == 'POST':
        # Create variable for uploaded file
        f = request.files['fileupload']

        # store the file contents as a string
        fstring = f.read()

        # create list of dictionaries keyed by header row
        csv_dicts = [{k: v for k, v in row.items()} for row in
                     csv.DictReader(fstring.splitlines(), skipinitialspace=True)]

        # do something list of dictionaries
        print
    return "success"

if __name__ == "__main__":
    app.run_server(debug=True)
