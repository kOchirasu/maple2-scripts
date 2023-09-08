""" 11001146: Recipe Note """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 21, 23])


