""" 11000042: Orde """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180610000108$
            # - Honestly, I don't care about politics or the court. My time is much better spent reading books in $map:02000031$.
            return 1
        elif index == 1:
            # functionID=1 
            # $script:0831180610000109$
            # - People don't understand the value to be found in dusty tomes and conversing with the fairies in $map:02000023$. But you have a certain inquisitiveness in your eyes, an intellectual spark. You might make a good Wizard. I'm not going to push, but if you're the arcane arts, I'd be willing to assist you.
            return -1
        return -1

