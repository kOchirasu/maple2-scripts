""" 11000982: Christopher """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # $script:0831180610001142$
        # - $MyPCName$, what you did was fantastic!
        #   Now all you have to do is return to $map:02000062$ for a debriefing.
        #   It's 4,000 mesos to go back on the ship, the same fare as before.
        #   Do you want to depart for $map:02000062$ now?
        return -1
