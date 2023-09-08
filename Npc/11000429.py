""" 11000429: Remy """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 41])


