""" 11000960: Krin """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __20(self, index: int, pick: int) -> int:
        # $script:0831180407003327$
        # - Wah! What are you doing? Don't you know how to knock?!
        if pick == 0:
            # $script:0831180407003328$
            # - I didn't know someone was in here.
            # TODO: goto 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
            return -1
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180407003329$
        # - Get out of here! Oh, and take this with you.
        return -1
