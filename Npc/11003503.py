""" 11003503: Ranshu """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])


    def __50(self, index: int, pick: int) -> int:
        # $script:0816160115008989$
        # - I work alone, but I'll be in need of a partner in the future.
        if pick == 0:
            # $script:0816211715009063$
            # - What about me?
            # TODO: goto 51, 52
            return -1
        return -1

