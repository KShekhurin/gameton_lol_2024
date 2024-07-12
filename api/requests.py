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

def make_step():
    pass