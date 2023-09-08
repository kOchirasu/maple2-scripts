""" 11000632: Jimmy """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 60])


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
