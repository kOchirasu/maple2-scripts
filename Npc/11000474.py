""" 11000474: Wheel of Joy """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 30
        return random.choice([40])

    def select(self) -> int:
        return 0

    # Job
    def __30(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180610000452$
            # - Spin, spin!
            return 30
        elif index == 1:
            # functionID=1 
            # $script:0831180610000453$
            # - Welcome!
            #   $npc:11000474$ is filled with <font color="#ffd200">wondrous items</font>!
            return 30
        elif index == 2:
            # $script:0831180610000454$
            # - Spin $npc:11000474$ for your chance to win the wondrous items!
            #   May luck be with you, <font color="#ffd200">$MyPCName$</font>!
            return -1
        return -1

