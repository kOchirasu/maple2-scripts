""" 11000670: Misplaced Book """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])


    def __20(self, index: int, pick: int) -> int:
        # $script:0831180407002730$
        # - Hey! Did you just throw me on the ground? 
        if pick == 0:
            # $script:0831180407002731$
            # - How did you end up on the bookshelf?
            # TODO: goto 21
            # TODO: gotoFail 22
            return 22
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
