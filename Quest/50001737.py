""" 50001737: An Ally in Prison """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0720003111007203$
        # - 
        if pick == 0:
            # $script:0720003111007204$
            # - 
            # TODO: goto 201, 202
            # TODO: gotoFail 203
            return 203
        elif pick == 1:
            # $script:0720003111007205$
            # - 
            return 204
        return -1

