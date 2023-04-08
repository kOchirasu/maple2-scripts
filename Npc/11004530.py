""" 11004530: Reika """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 50])

    def select(self) -> int:
        return random.choice([0, 40])
