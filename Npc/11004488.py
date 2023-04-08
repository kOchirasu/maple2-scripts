""" 11004488: Oranda """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 12])

    def select(self) -> int:
        return 0
