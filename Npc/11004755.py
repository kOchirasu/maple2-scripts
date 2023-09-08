""" 11004755 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])


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
