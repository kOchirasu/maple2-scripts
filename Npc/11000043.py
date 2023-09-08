""" 11000043: Trini """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])


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
