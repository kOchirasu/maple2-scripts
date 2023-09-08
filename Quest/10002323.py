""" 10002323: QUESTDESCRIPTION_10002323_NAME """
from npc_api import Script
import random


class Main(Script):
    def __200(self, index: int, pick: int) -> int:
        # $script:0831174302003252$
        # - 
        if pick == 0:
            # $script:0831174302003253$
            # - 
            # TODO: goto 201, 202
            # TODO: gotoFail 203
            return 203
        elif pick == 1:
            # $script:0831174302003254$
            # - 
            return 204
        return -1

