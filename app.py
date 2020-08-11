# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:03:02 2020

@author: Vatsal Tulshyan
"""

from flask import Flask,jsonify
from flask_cors import CORS
from predict import predict
app = Flask(__name__) 
CORS(app)

@app.route('/api',methods=['POST'])
def chat_output():
    img = Flask.request.files.get('imagefile', '')
    #Prediction np array
    result = predict(img)

    if result==1:
        reply="Pneumonia Detected!"
    else:
        reply="You are all fine!"
        
    result={"reply":reply}

    response = jsonify(result)
    return response

if __name__ == "__main__":
    app.run(port=8000,debug=False)