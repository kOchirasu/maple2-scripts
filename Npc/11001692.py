""" 11001692: Hub Computer """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([5, 10, 11, 12, 13, 14, 15, 20, 30, 40, 50, 60])

    def select(self) -> int:
        return 0

    def __41(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0804163407007059$
        # - System Command: Absorb target's energy.
        return -1

