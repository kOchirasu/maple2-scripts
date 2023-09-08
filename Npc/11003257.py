""" 11003257: Cheshire Carmen Bella Jr. II """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 60])


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
