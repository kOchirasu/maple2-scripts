""" 40001010: QUESTDESCRIPTION_40001010_NAME """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0901101205000029$
        # - 
        if pick == 0:
            # $script:0901101205000030$
            # - 
            # TODO: goto 201, 202
            # TODO: gotoFail 203
            return 203
        elif pick == 1:
            # $script:0901101205000031$
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
