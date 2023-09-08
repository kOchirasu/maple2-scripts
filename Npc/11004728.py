""" 11004728: Hide-and-Seek Wheel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1010204110002257$
        # - Give us 5 $itemPlural:30001442$ for a chance to spin the $npc:11004728$. How about it? Feeling lucky?
        if pick == 0:
            # $script:1010204110002258$
            # - (Pay 5 $item:30001442$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:1010204110002259$
            # - (Pay 50 $itemPlural:30001442$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:1010204110002260$
            # - (Pay 500 $itemPlural:30001442$ for a bunch of spins in a row!)
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
