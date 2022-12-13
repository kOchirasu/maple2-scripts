""" 11001238: Merkaz """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 60])

    def select(self) -> int:
        return 0

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

    def __42(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1125183507007506$
        # - I've created a portal for you down there. It will take you to $map:52000076$. Next time, use the portal instead of bothering me, all right?
        return -1

    def __51(self, index: int, pick: int) -> int:
        # functionID=2 
        # $script:1214150707007554$
        # - Heh heh heh... Off with you!
        return -1

