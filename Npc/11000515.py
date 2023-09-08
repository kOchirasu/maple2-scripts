""" 11000515: Jayce """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60])


