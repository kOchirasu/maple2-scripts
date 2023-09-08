""" 10001003: QUESTDESCRIPTION_10001003_NAME """
from npc_api import Script
import random


class Main(Script):
    def __102(self, index: int, pick: int) -> int:
        # TODO: Job Condition: 110
        if index == 0:
            # $script:0802233102005683$
            # - 
            return 102
        elif index == 1:
            # $script:0802233102005684$
            # - 
            return 102
        elif index == 2:
            # $script:0802233102005685$
            # - 
            if pick == 0:
                # $script:0802233102005686$
                # - 
                return 103
            return -1
        return -1

