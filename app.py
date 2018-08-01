# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from flask import make_response,Response
app = Flask(__name__)
import rpc,json
import os



#print(rpc.getbalance("2SATGZDFDXNNJRVZ52O4J6VYTTMO2EZR"))
#print(rpc.getbalance("G35X2DSESYNWASV5YLY3UZNCBCMGAJ7R"))

@app.route('/api/<string:address>',methods=['GET'])
def get_balance(address):
    return jsonify(rpc.getbalance(address))
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)
