""" 60110015: Donald's Demand """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0416153812003126$
        # - 
        if pick == 0:
            # $script:0813141612003220$
            # - 
            # TODO: goto 201, 202
            # TODO: gotoFail 203
            return 203
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
