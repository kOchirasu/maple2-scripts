""" 11001871: Ophelia """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1021213710001703$
        # - We can do that! Just show me the item you want to retool. Remember, I can only work on Epic or Legendary armor and accessories at Level 50 or above.
        return -1

    def __31(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:1021213710001709$
            # - Okay, let's see the gear you want to enchant. I'm warning you now, it has to be marked with "Can be Enchanted."
            return 31
        elif index == 1:
            # functionID=1 
            # $script:0330144110002047$
            # - Okay, let's see the gear you want to enchant. I'm warning you now, it has to be marked with "Can be Enchanted."
            return -1
        return -1

