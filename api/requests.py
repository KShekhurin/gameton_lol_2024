from ..setup import API_TOKEN, SERVER_ADRESS
from ..models.data_models import *

import requests as req


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

def ():
    pass

def make_step():
    pass