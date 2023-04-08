""" 11001397: Akamorro """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __46(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:1227015507005624$
            # - So impertinent! I was just getting to the good part. In short...
            return 46
        elif index == 1:
            # $script:1227015507005625$
            # - I've created a potion that can alleviate the ailments that $npcName:11001396[gender:1]$ told me about. Note that I am being most humble here. When I say alleviate, I mean completely cure.
            if pick == 0:
                # $script:1227015507005626$
                # - Thank you.
                # TODO: goto 47
                # TODO: gotoFail 48
                return 48
            return -1
        return -1

    def __47(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:1227015507005627$
        # - Take this to $npcName:11001396[gender:1]$. And tell her she's welcome.
        return -1
