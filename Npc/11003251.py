""" 11003251: Einos """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 60])

    def select(self) -> int:
        return 0

    def __41(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0526174607008532$
        # - Here you go. The crystal should react to this.
        return -1

