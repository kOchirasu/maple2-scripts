""" 10002173: A Heartwarming Reunion """
from npc_api import Script
import random


class Main(Script):
    def __110(self, index: int, pick: int) -> int:
        # TODO: Job Condition: 110
        # $script:0809151402005727$
        # - 
        if pick == 0:
            # $script:0809151402005728$
            # - 
            return 111
        return -1

    def __200(self, index: int, pick: int) -> int:
        # $script:0831174302002550$
        # - 
        if pick == 0:
            # $script:0831174302002551$
            # - 
            # TODO: goto 201, 202
            # TODO: gotoFail 203
            return 203
        elif pick == 1:
            # $script:0831174302002552$
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
