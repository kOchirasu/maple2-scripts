""" 11000981: Christopher """
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
        # $script:0831180610001131$
        # - The Marco has a noble purpose, to transport adventurers on missions for the $map:02000068$. And lately, it's also been carrying adventurers to $map:02000183$ where they battle pirates in the eastern straits. If you're one of these adventurers, then you can board the ship for 4,000 mesos. Is that what you want to do?
        return -1

