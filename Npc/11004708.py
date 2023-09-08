""" 11004708 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30, 40, 50, 54, 55, 60, 70])


    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 8:
            # TODO: functionID 8
            return
        if functionId == 9:
            # TODO: functionID 9
            return
        if functionId == 10:
            # TODO: functionID 10
            return
        if functionId == 11:
            # TODO: functionID 11
            return
        if functionId == 3:
            # TODO: functionID 3
            return
        if functionId == 4:
            # TODO: functionID 4
            return
        if functionId == 6:
            # TODO: functionID 6
            return
        if functionId == 7:
            # TODO: functionID 7
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 8:
            # TODO: functionID 8
            return
        if functionId == 9:
            # TODO: functionID 9
            return
        if functionId == 10:
            # TODO: functionID 10
            return
        if functionId == 11:
            # TODO: functionID 11
            return
        if functionId == 3:
            # TODO: functionID 3
            return
        if functionId == 4:
            # TODO: functionID 4
            return
        if functionId == 6:
            # TODO: functionID 6
            return
        if functionId == 7:
            # TODO: functionID 7
            return
        return
