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
    count_to_generate, mean, std_deviation = get_default_values(request)
    
    ndvalues = results = random.normal(
        loc=mean, 
        scale=std_deviation, 
        size=(1, count_to_generate))
    
    return ndvalues[0]

def get_default_values(request):
    count_to_generate = 20
    if request.args.get('count'):
        count_to_generate = int(request.args.get('count'))
        
    mean = 10000
    if request.args.get('mean'):
        mean = int(request.args.get('mean'))
        
    std_deviation = 2000
    if request.args.get('std_deviation'):
        std_deviation = int(request.args.get('std_deviation'))
    
    return count_to_generate, mean, std_deviation
