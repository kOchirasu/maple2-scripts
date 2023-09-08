""" 11003347: Ralph's Lackey """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 30


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
