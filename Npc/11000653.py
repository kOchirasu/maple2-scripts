""" 11000653: Prisoner 170125 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0
