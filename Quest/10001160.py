""" 10001160: QUESTDESCRIPTION_10001160_NAME """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0831174302000445$
        # - 
        if pick == 0:
            # $script:0831174302000446$
            # - 
            # TODO: goto 201, 202
            # TODO: gotoFail 203
            return 203
        elif pick == 1:
            # $script:0831174302000447$
            # - 
            return 204
        return -1

    def __310(self, index: int, pick: int) -> int:
        # TODO: Job Condition: 110
        # $script:0809151402005719$
        # - 
        if pick == 0:
            # $script:0809151402005720$
            # - 
            return 311
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
