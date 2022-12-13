""" 11000420: Moma """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([90, 100])

    def select(self) -> int:
        return 0

