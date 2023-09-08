""" 11001692: Hub Computer """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([5, 10, 11, 12, 13, 14, 15, 20, 30, 40, 50, 60])


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
