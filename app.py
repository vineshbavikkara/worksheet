#  For Deployment
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict1',methods=['POST'])
def predict1():
    response = [x for x in request.form.values()]
    if int(response[0]) == 1: 
        return render_template("index.html",predicted1="Correct")
    return render_template("index.html",predicted1="Wrong")

if __name__=="__main__":
    app.run(debug=True)