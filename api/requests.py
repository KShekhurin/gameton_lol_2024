from ..setup import API_TOKEN, SERVER_ADRESS
from ..models.data_models import *

import requests as req

headers = { 'X-Auth-Token': API_TOKEN }

def make_step(data: StepData):
    response = req.post( json=data.as_dict())

def make_step():
    pass

def make_step():
    pass