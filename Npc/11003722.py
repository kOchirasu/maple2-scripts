""" 11003722 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30, 40])

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # $script:1130102607009374$
        # - Hey there! It's me, Little Zakum. You know, Zakum, but little. I have a gift for you!
        if pick == 0:
            # $script:1130104707009376$
            # - Oh, oh, what is it?
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:1130104707009377$
        # - You've got to open it to find out! I hope you like this gift to you from me, Little Zakum.
        return -1
