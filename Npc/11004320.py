""" 11004320: Dunba """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

