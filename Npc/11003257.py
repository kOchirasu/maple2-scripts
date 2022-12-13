""" 11003257: Cheshire Carmen Bella Jr. II """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 60])

    def select(self) -> int:
        return 0

    def __42(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0530154407008545$
        # - I'm trying! Close your eyes. It'll work for sure this time!
        return -1

