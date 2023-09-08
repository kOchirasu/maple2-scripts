""" 11004317: Maple Spin """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1001153510002190$
        # - Give us 1 $item:30001202$ for a chance to spin the $npc:11004317$. How about it? Feeling lucky?
        if pick == 0:
            # $script:1001153510002191$
            # - (Pay 1 $item:30001202$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:1001153510002192$
            # - (Pay 10 $itemPlural:30001202$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:1001153510002193$
            # - (Pay 100 $itemPlural:30001202$ for a bunch of spins in a row!)
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
