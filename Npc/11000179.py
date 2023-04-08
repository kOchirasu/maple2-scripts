""" 11000179: Albert """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 70])

    def select(self) -> int:
        return 0
