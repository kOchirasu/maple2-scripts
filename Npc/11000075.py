""" 11000075: Ereve """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30, 40])

    def select(self) -> int:
        return 0

