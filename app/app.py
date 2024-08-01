from flask import Flask
from numpy import random
from flask import request

app = Flask(__name__)

@app.route("/")
def normal_json():
    ndvalues = get_nd_values(request)
    
    values = []
    for value in ndvalues:
        values.append(value)
    
    return values

def get_nd_values(request):
    count_to_generate = 20
    if request.args.get('count'):
        count_to_generate = int(request.args.get('count'))
    
    ndvalues = results = random.normal(
        loc=10000, 
        scale=2000, 
        size=(1, count_to_generate))
    
    return ndvalues[0]
