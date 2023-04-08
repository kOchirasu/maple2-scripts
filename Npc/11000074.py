""" 11000074: Karl """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30, 40])

    def select(self) -> int:
        return 0
