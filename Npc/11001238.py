""" 11001238: Merkaz """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 60])


    def __41(self, index: int, pick: int) -> int:
        # $script:1125183507007504$
        # - What I am <i>trying</i> to say is that you shouldn't be here right now. I will send you to where you should be.
        if pick == 0:
            # $script:1125183507007505$
            # - Please send me there again.
            # TODO: goto 42
            # TODO: gotoFail 43
            return 43
        return -1

    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        return
