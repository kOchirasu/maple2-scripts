""" 11003511: Premium Lucky Wheel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0809174410001881$
        # - Welcome! Pay me 5 $itemPlural:30000875$ and I'll let you spin the $npc:11003511$! How about it? Feeling lucky?
        if pick == 0:
            # $script:0809174410001882$
            # - Pay 5 $itemPlural:30000875$ to spin once.
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0809174410001883$
            # - Pay 50 $itemPlural:30000875$ to spin continuously.
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0809174410001884$
            # - Pay 500 $itemPlural:30000875$ to spin continuously.
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
