""" 11001513: Paulie """
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
        # $script:0420153110001493$
        # - Looking for some head-turning hair? Then you came to the right place, $MyPCName$. My special hairstyles are unmatched!
        if pick == 0:
            # $script:0420153110001494$
            # - I leave my special hairstyle to you, maestro.
            return 0
        return -1

