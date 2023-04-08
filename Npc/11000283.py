""" 11000283: Duomo """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 50])

    def select(self) -> int:
        return 0
