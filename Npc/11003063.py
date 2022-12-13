""" 11003063: Surmany """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __41(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0207083707007922$
        # - There you go. This is because you got those materials for me, you know. Helping others pays off!
        return -1

