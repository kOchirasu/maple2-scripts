""" 60110045: Lunch Delivery """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0416153812003192$
        # - 
        if pick == 0:
            # $script:0814134512003224$
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
