""" 11001056: Intertimer """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # $script:0831180610001153$
        # - Do you want to use this experimental teleportation device?
        #   Destination: $map:02000259$
        #   Cost: 5,000 mesos
        return -1

