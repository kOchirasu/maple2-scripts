""" 11003096: Allon """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return -1 # No dialogue

    def select(self) -> int:
        return random.choice([0, 10])

