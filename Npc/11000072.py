""" 11000072: Zenko """
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
        # $script:0831180610000389$
        # - Welcome, $MyPCName$. Thinking about spicing up your look? I can give you any skin tone you like. Care to take a peek?
        if pick == 0:
            # $script:0831180610000390$
            # - Yeah, let's do it!
            return 0
        return -1

