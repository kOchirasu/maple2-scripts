""" 11000670: Misplaced Book """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])

    def select(self) -> int:
        return 0

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

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180407002732$
        # - A stupid monster brought me back here. Please, you've got to take me with you!
        return -1
