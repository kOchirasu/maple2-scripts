""" 11003552: Yoharang """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])


    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        if functionId == 3:
            # TODO: functionID 3
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        if functionId == 3:
            # TODO: functionID 3
            return
        return
