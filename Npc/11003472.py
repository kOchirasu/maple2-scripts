""" 11003472: Cathy Mart Lucky Wheel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0710202510001867$
        # - Welcome! Pay me 5 $itemPlural:30000869$, and I'll let you spin the $npc:11003472$. How about it? Feeling lucky?
        if pick == 0:
            # $script:0710202510001868$
            # - Pay 5 $itemPlural:30000869$ to spin once.
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0710202510001869$
            # - Pay 50 $itemPlural:30000869$ to spin continuously.
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0710202510001870$
            # - Pay 500 $itemPlural:30000869$ to spin continuously.
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        return
