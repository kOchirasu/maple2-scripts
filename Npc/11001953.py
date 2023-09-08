""" 11001953: Kay's Event Wheel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1128172510001804$
        # - Give us 1 $item:30000610$ for a chance to spin $npc:11001953$. What do you say?
        if pick == 0:
            # $script:1128172510001805$
            # - (Pay 1 $item:30000610$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0612112710001842$
            # - (Pay 10 $itemPlural:30000610$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0612112710001843$
            # - (Pay 100 $itemPlural:30000610$ for a bunch of spins in a row!)
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
