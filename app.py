# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from flask import make_response,Response
app = Flask(__name__)
import rpc,json
import os
import dbm



def update_votings_index():
    db = dbm.open('db/votings_index', 'c')
    votings_index=0
    if ("index" in db):
        votings_index = int(db["index"].decode('utf-8'))
        votings_index = int(votings_index)+1
        db["index"] = str(votings_index)
    else:
        db["index"] = "0"
    db.close()
    return votings_index

update_votings_index()

@app.route('/',methods=['GET'])
def votings():
    return render_template("votings.html")

@app.route('/voting/<string:index>',methods=['GET'])
def voting(index):
    return render_template("voting.html",index=index)

@app.route('/set',methods=['GET'])
def set():
    return render_template("set.html")

@app.route('/api/votings/add',methods=['POST'])
def votings_add():
    if request.method == 'POST':
        name=request.form.get('name')

        db = dbm.open('db/votings', 'c')


        votings_index = str(update_votings_index())

        db[str(votings_index)] = name
        db.close()

        return jsonify(votings_index)

@app.route('/api/votings',methods=['GET'])
def votings_all():
    json=[]
    db = dbm.open('db/votings', 'c')
    for key in db.keys():
        voting = {}
        voting["index"] = key.decode('utf-8')
        voting["name"] = db[key].decode('utf-8')
        json.append(voting)
        print (voting["index"])
    db.close()

    return jsonify(json)

@app.route('/api/voting/<string:index>',methods=['GET'])
def votings_of(index):
    json={}
    voting={}
    selectlist=[]

    db = dbm.open('db/votings', 'c')
    if index in db:
        voting["index"] = index
        voting["name"] = db[index].decode('utf-8')
        json["voting"]=voting
    else:
        json="error"
    db.close()

    db = dbm.open("db/voting_{0}".format(index), 'c')

    for key in db.keys():
        select = {}
        select["name"] = key.decode('utf-8')
        select["address"] = db[key].decode('utf-8')
        selectlist.append(select)
    
    db.close()
    json["selectlist"]=selectlist
    return jsonify(json)

@app.route('/api/select/add',methods=['POST'])
def select_add():
    if request.method == 'POST':
        name=request.form.get('name')
        address=rpc.make_a_new_address()
        voting_id=request.form.get('voting_id')

        db = dbm.open("db/voting_{0}".format(voting_id), 'c')
        db[name] = address
        db.close()

        return jsonify("ok")

# RPC apis

@app.route('/api/address',methods=['GET'])
def get_address_all():
    return jsonify(rpc.get_all_address())

@app.route('/api/address/new',methods=['GET'])
def make_a_address(address):
    return jsonify(rpc.make_a_new_address())

@app.route('/api/address/<string:address>',methods=['GET'])
def check_address_of(address):
    return jsonify(rpc.check_address(address))

@app.route('/api/balance',methods=['GET'])
def get_balance():
    return jsonify(rpc.get_balance_all())

@app.route('/api/balance/<string:address>',methods=['GET'])
def get_balance_of(address):
    return jsonify(rpc.get_balance_of(address))

@app.route('/api/pay',methods=['POST'])
def pay():
    if request.method == 'POST':
        address=request.form.get('address')
        amount=request.form.get('amount')
        text=request.form.get('text')
        return jsonify(rpc.pay(address,amount,text))

@app.route('/api/keys')
def api_key():
    keysfile = "{0}/.config/lightwallet/keys.json".format(os.environ['HOME'])
    return jsonify(json.loads(open(keysfile).read()))

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(debug=True,host='0.0.0.0',port=port)
