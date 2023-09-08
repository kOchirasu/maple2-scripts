""" 11000960: Krin """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 20


    def __20(self, index: int, pick: int) -> int:
        # $script:0831180407003327$
        # - Wah! What are you doing? Don't you know how to knock?!
        if pick == 0:
            # $script:0831180407003328$
            # - I didn't know someone was in here.
            # TODO: goto 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
            return -1
        return -1

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
