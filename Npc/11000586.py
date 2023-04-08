""" 11000586: Injured Guard """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60, 70, 80])

    def select(self) -> int:
        return 0
