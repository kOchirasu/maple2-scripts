""" 11001871: Ophelia """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 10


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
