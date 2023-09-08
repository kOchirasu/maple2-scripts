""" 11003551 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0902174710001915$
        # - Give us 3 $itemPlural:30000878$ for a chance to spin the $npc:11003551$. How about it? Feeling lucky?
        if pick == 0:
            # $script:0902174710001916$
            # - (Pay 3 $item:30000878$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0902174710001917$
            # - (Pay 30 $itemPlural:30000878$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0902174710001918$
            # - (Pay 300 $itemPlural:30000878$ for a bunch of spins in a row!)
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
