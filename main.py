from setup import API_TOKEN
from models.data_models import *

from api.requests import participate, look_around

try:
    participate()
    look_around()
except Exception as exc:
    print(exc)