""" 11000025: Beth """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 60])

    def select(self) -> int:
        return 0

