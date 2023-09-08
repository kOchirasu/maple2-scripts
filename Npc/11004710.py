""" 11004710 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])


    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        return
