""" 11000021: Santiago """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 40])

    def select(self) -> int:
        return 0
