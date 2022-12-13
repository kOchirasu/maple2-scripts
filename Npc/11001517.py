""" 11001517: Lucky Wheel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # $script:0217184010001441$
        # - Would you like to spin the $npcName:11001517$?
        if pick == 0:
            # $script:0217184010001442$
            # - (Pay 50,000 mesos for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0217184010001443$
            # - (Pay 1 $item:30000522$ for 1 spin.)
            # TODO: goto 33
            # TODO: gotoFail 34
            return 34
        return -1

    def __31(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0217184010001444$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 31
        elif index == 1:
            # $script:0217184010001445$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

    def __33(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0217184010001447$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 33
        elif index == 1:
            # $script:0217184010001448$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

