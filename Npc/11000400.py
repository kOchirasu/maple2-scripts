""" 11000400: Newton """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])


