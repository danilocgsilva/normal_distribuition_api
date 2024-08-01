from flask import Flask
from numpy import random

app = Flask(__name__)

@app.route("/")
def normal_json():
    ndvalues = random.normal(loc=10000, scale=2000, size=(1,20))[0]
    values = []
    for value in ndvalues:
        values.append(value)
    
    return values
