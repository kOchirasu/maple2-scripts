""" 11001120: Lucky Wheel """
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
            # $script:0909140310001157$
            # - Look at all those $itemPlural:30000406$> you've got! You're sitting pretty! Why don't you invest them in a chance to spin the $npc:11001120$? Could be a wise investment, indeed!
            return 30
        elif index == 1:
            # functionID=1
            # $script:0909140310001158$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 30
        elif index == 2:
            # $script:0909140310001159$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1
