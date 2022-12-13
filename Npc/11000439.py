""" 11000439: Dark Wind Watchman """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60])

    def select(self) -> int:
        return 1

