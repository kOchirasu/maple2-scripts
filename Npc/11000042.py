""" 11000042: Orde """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        x = self.job()//10
        if self.level() >= 10 and x == 1:
            return 1
        if x == 10:
            return 30
        if x == 20:
            return 40
        if x == 30:
            return 20
        return x + 10

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
