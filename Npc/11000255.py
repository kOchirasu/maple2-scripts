""" 11000255: Rosetta """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180610000400$
        # - $MyPCName$, how shall we style your hair today? Anything you like, just say the word.
        if pick == 0:
            # $script:0831180610000401$
            # - Anything? Really? Well, in that case...
            return 0
        return -1

