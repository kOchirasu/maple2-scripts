""" 11002042: Dent """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([10, 20])


