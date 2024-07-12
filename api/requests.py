import requests as req

import sys
sys.path.append("..")
from setup import API_TOKEN, SERVER_ADDRESS
from models.data_models import *

headers = { 'X-Auth-Token': API_TOKEN }

def make_step(data: StepData):
    response = req.post(
        f"{SERVER_ADRESS}/play/zombidef/command",
        json=data.as_dict(),
        headers=headers
    )

    if response.status_code != 200:
        return False
    return True


def participate():
    response = req.put(SERVER_ADDRESS + 'play/zombidef/participate', headers=headers)


def make_step():
    pass