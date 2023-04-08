""" 11000374: Tann """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 60])

    def select(self) -> int:
        return 0
