""" 11001514: Lolly """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0420153110001495$
        # - Hiiii, $MyPCName$! I'm $npcName:11001513[gender:0]$'s assistant! He lets me handle the $itemPlural:20300246$! If you have some, I can give you an absolutely darling hairstyle!
        if pick == 0:
            # $script:0420153110001496$
            # - Sure, let's spend some $itemPlural:20300246$.
            return 0
        return -1

