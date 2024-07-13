from setup import API_TOKEN
from models.data_models import *
import matplotlib.pyplot as plt

from api.requests import participate, look_around, get_rounds

while (True):
    try:
        rounds = get_rounds()
        print(rounds)
        print(len(rounds.rounds))
        for r in rounds.rounds:
            print(r.name)

        break
    except Exception as exc:
        print(exc)