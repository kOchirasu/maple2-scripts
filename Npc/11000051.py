""" 11000051: Ruki """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180610000333$
            # - Ugh. This place makes me so uncomfortable.  Hmm... Your eyes... I can see you're a kindred spirit... How would you like to join us and walk among the shadows?
            return 1
        elif index == 1:
            # functionID=1 
            # $script:0831180610000334$
            # - Happiness, anger, sadness, forgiveness—emotions are just baggage that gets in the way. Your enemies don't deserve your mercy. 
            return -1
        return -1

