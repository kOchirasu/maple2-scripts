""" 11000033: Jorge """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __41(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0530154307008542$
        # - $npcName:11000031[gender:0]$ says you're all right, so fine. Off you go.
        return -1

