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
    res = int(response[0])
    if int(response[0]) == 1: 
        return render_template("index1.html",answer=" 1 is Correct Answer ")
    return render_template("index2.html",a=res,answer=" is Wrong Answer ")

@app.route('/homepage')
def homepage():
	return render_template("index.html")

@app.route('/answer1')
def answer1():
	return render_template("answer1.html")


if __name__=="__main__":
    app.run(debug=True)

