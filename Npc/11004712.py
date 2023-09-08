""" 11004712 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30, 40, 50])


    def __21(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:1101145407015373$
            # - 
            return 21
        elif index == 1:
            # $script:1108203507015703$
            # - 
            return 21
        elif index == 2:
            # $script:1101145407015374$
            # - 
            return 21
        elif index == 3:
            # $script:1101145407015375$
            # - 
            if pick == 0:
                # $script:1101145407015376$
                # - 
                # TODO: goto 22
                # TODO: gotoFail 25
                return 25
            elif pick == 1:
                # $script:1101145407015377$
                # - 
                return 23
            return -1
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
