""" 11000474: Wheel of Joy """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 30
        return random.choice([40])


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
