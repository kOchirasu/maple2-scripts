""" 11000071: Dixon """
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
        # $script:0831180610000383$
        # - Oooh, $MyPCName$, I'm so glad you found me. I can work miracles! Everyone says so. Now, what did you have in mind?
        if pick == 0:
            # $script:0831180610000384$
            # - Show me the possibilities.
            return 0
        return -1

