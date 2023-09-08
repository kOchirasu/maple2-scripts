""" 11003386: 2nd Anniversary Wheel of Joy """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0622191110001845$
        # - Welcome! Pay me 5 $itemPlural:30000782$, and I'll let you spin the $npcName:11003386$. How about it? Feeling lucky?
        if pick == 0:
            # $script:0622191110001846$
            # - Pay 5 $itemPlural:30000782$ to spin once.
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0622191110001847$
            # - Pay 50 $itemPlural:30000782$ to spin continuously.
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0622191110001848$
            # - Pay 500 $itemPlural:30000782$ to spin continuously.
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
