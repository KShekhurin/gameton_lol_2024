import requests as req

import sys
sys.path.append("..")
from setup import API_TOKEN, SERVER_ADDRESS
from models.data_models import *

headers = { 'X-Auth-Token': API_TOKEN }

def make_step(data: StepData):
    response = req.post( json=data.as_dict())

def participate():
    response = req.put(SERVER_ADDRESS + 'play/zombidef/participate', headers=headers)

def look_around():
    response = req.get(SERVER_ADDRESS + 'play/zombidef/units', headers=headers)
    
    if (response.status_code != 200):
        raise Exception("[look_around]: " + str(response.status_code) + " " + response.json()["error"])
    
    details = response.json()
    return ChangingData(details)

def watch_eternity():
    response = req.get(SERVER_ADDRESS + 'play/zombidef/world', headers=headers)
    
    if (response.status_code != 200):
        raise Exception("[watch_eternity]: " + str(response.status_code) + " " + response.json()["error"])
    
    details = response.json()
    return ChangingData(details)