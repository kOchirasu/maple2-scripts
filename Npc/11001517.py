""" 11001517: Lucky Wheel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 30


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
