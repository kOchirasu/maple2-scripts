""" 40002605: QUESTDESCRIPTION_40002605_NAME:[F]Striker """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0705202805001615$
        # - 
        if pick == 0:
            # $script:0705202805001616$
            # - 
            # TODO: goto 201, 202
            # TODO: gotoFail 203
            return 203
        elif pick == 1:
            # $script:0705202805001617$
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
