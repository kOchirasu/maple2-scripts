""" 11000045: Ikas """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        x = self.job()//10
        if self.level() >= 10 and x == 1:
            return 1
        if x == 50:
            return 20
        if x < 50:
            return x + 20
        return x + 10

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180610000193$
            # - The Green Hoods are a militia group with a long, storied history. Right now, we're keeping an eye on the opportunists who might try to take advantage of the chaos of recent events. We want to prevent as much crime as possible, but that requires talent and mettle. And you... you look like you've got both of those.
            return 1
        elif index == 1:
            # functionID=1
            # $script:0831180610000194$
            # - Our sharp arrows never miss their targets. How would you like to join us on our mission to restore order to this world?
            return -1
        return -1
