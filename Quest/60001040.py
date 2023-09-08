""" 60001040: QUESTDESCRIPTION_60001040_NAME """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0105153412001781$
        # - 
        if pick == 0:
            # $script:0105153412001782$
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
