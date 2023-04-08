""" 11000508: Ophelia """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0323154410001460$
        # - Do you want to change the bonus attributes on your gear? Then pick an item to change! Just remember that it needs to be epic or better armor and accessories at level 50 and above.
        return -1

    def __31(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0330140710001959$
        # - Okay, let's see the gear you want to enchant. I'm warning you now, it has to be marked with "Can be Enchanted."
        return -1
