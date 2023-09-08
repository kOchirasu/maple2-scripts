""" 11003471 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return -1 # No dialogue


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
