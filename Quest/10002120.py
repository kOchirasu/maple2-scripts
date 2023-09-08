""" 10002120: Wisdom of a Sage """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0831174302002389$
        # - 
        if pick == 0:
            # $script:0831174302002390$
            # - 
            # TODO: goto 201, 202
            # TODO: gotoFail 203
            return 203
        elif pick == 1:
            # $script:0831174302002391$
            # - 
            return 204
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
