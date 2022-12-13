""" 11001498: Dunba """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # $script:0118150907005831$
        # - Don't just stare at your food, eat it! So rude.
        if pick == 0:
            # $script:0120170607005853$
            # - Tell me about your past.
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0120170607005854$
        # - If not for him...
        return -1

