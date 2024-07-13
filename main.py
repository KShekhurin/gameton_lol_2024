from setup import API_TOKEN
from models.data_models import *

from api.requests import participate, look_around, get_rounds, watch_eternity
from bussiness import wait_till_nearest

game = None
nearest_round = None

while (True):
    try:
        game = get_rounds()
        print(game.game_name)

        game.rounds.sort(key=lambda x: x.start_at)
        for r in game.rounds:
            if r.status == 'not started':
                nearest_round = r
                break

        break
    except Exception as exc:
        print(exc)

wait_till_nearest(nearest_round)

while (True):
    try:
        participate()
    except Exception as exc:
        print(exc)