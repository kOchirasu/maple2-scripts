""" 11000003: Growlie """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 60])


