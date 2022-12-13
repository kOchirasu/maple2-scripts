""" 11000119: Frey """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 70, 120])

    def select(self) -> int:
        return 0

