import requests as req

import sys
sys.path.append("..")
from setup import API_TOKEN, SERVER_ADDRESS
from models.data_models import *

headers = { 'X-Auth-Token': API_TOKEN }

def make_step(data: StepData):
    response = req.post(
        f"{SERVER_ADDRESS}/play/zombidef/command",
        json=data.as_dict(),
        headers=headers
    )

    if response.status_code != 200:
        return False
    return True


def participate():
    response = req.put(SERVER_ADDRESS + 'play/zombidef/participate', headers=headers)

    if (response.status_code != 200):
        raise Exception("[participate]: " + str(response.status_code) + " " + response.json()["error"])

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
    return NotChangingData(details)

def get_round():
    response = req.get(SERVER_ADDRESS + 'play/zombidef', headers=headers)
    
    if (response.status_code != 200):
        raise Exception("[get_round]: " + str(response.status_code) + " " + response.json()["error"])
    
    details = response.json()
    return GameRounds(details)