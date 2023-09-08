""" 11001654: Festival Lucky Wheel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def __30(self, index: int, pick: int) -> int:
        # $script:0615152810001561$
        # - Give us 3 $itemPlural:30000554$ for a chance to spin the $npc:11001654$. How about it? Feeling lucky?
        if pick == 0:
            # $script:0620113310001566$
            # - (Pay 3 $itemPlural:30000554$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0125175010001818$
            # - Pay 30 $itemPlural:30000554$ to spin 10 times.
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0125175010001819$
            # - Pay 300 $itemPlural:30000554$ to spin 100 times.
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
