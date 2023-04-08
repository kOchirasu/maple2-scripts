""" 11000323: Tony """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 60, 70])

    def select(self) -> int:
        return 0
