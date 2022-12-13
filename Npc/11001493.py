""" 11001493: Startz """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # $script:0118150907005812$
        # - Everything happens for a reason.
        if pick == 0:
            # $script:0120154307005850$
            # - Tell me about your past.
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0120154307005851$
        # - Ah, you want to know what happened back then.
        return -1

