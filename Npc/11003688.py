""" 11003688 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1110142010001931$
        # - Give us 3 $itemPlural:30001010$ for a chance to spin the $npc:11003688$. How about it? Feeling lucky?
        if pick == 0:
            # $script:1110142010001932$
            # - (Pay 3 $item:30001010$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:1110142010001933$
            # - (Pay 30 $itemPlural:30001010$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:1110142010001934$
            # - (Pay 300 $itemPlural:30001010$ for a bunch of spins in a row!)
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
