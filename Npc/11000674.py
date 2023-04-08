""" 11000674: Altar of Rage """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __11(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180610000470$
        # - <i>The wrathful shadows have devoured every one of your blessings and taken over your mind.
        #   Now, you see that friendship is a myth, and everyone is your enemy!</i>
        return -1
