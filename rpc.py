#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json

url = "http://info.trustnote.org:6552"
headers = {'content-type': 'application/json'}

def get_result(payload):
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    note = response['result']['base']['stable']
    mn = note/1000000
    return mn


def getbalance(address):
    payload = {
        "method": "getbalance",
        "params": [address],
        "jsonrpc": "2.0",
        "id": 1,
    }
    return get_result(payload)
