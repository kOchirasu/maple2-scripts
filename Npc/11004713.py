""" 11004713 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30, 35, 40, 45])


    def __21(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:1101145407015396$
            # - 
            return 21
        elif index == 1:
            # $script:1101145407015397$
            # - 
            return 21
        elif index == 2:
            # $script:1101145407015398$
            # - 
            return 21
        elif index == 3:
            # $script:1101145407015399$
            # - 
            if pick == 0:
                # $script:1101145407015400$
                # - 
                # TODO: goto 22
                # TODO: gotoFail 25
                return 25
            elif pick == 1:
                # $script:1101145407015401$
                # - 
                return 23
            return -1
        return -1

    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        if functionId == 3:
            # TODO: functionID 3
            return
        if functionId == 4:
            # TODO: functionID 4
            return
        if functionId == 5:
            # TODO: functionID 5
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        if functionId == 3:
            # TODO: functionID 3
            return
        if functionId == 4:
            # TODO: functionID 4
            return
        if functionId == 5:
            # TODO: functionID 5
            return
        return
