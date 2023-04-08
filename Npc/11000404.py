""" 11000404: Snowy """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 60])

    def select(self) -> int:
        return 0
