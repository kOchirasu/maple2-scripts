""" 11000600: Charles Kim """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60, 70, 80, 90, 100, 110, 120, 130])

    def select(self) -> int:
        return 0

    def __65(self, index: int, pick: int) -> int:
        # $script:0831180407002418$
        # - Good, then it's 10,000 mesos for a $item:30000145$.
        if pick == 0:
            # $script:0831180407002419$
            # - Here's the money.
            # TODO: goto 66
            # TODO: gotoFail 67
            return 67
        return -1

    def __66(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002420$
        # - Here's your $item:30000145$. I hope you enjoy your new home. Bye for now!
        return -1

    def __95(self, index: int, pick: int) -> int:
        # $script:0831180407002434$
        # - Good, then it's 10,000 mesos for a $item:30000255$.
        if pick == 0:
            # $script:0831180407002435$
            # - Here's the money.
            # TODO: goto 96
            # TODO: gotoFail 97
            return 97
        return -1

    def __96(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002436$
        # - Here's your $item:30000255$. I hope you enjoy your new home. Bye for now!
        return -1

    def __115(self, index: int, pick: int) -> int:
        # $script:0831180407002449$
        # - Good, then it's 10,000 mesos for a $item:30000254$.
        if pick == 0:
            # $script:0831180407002450$
            # - Here's the money.
            # TODO: goto 116
            # TODO: gotoFail 117
            return 117
        return -1

    def __116(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002451$
        # - Here's your $item:30000254$. I hope you enjoy your new home. Bye for now!
        return -1

    def __135(self, index: int, pick: int) -> int:
        # $script:0831180407002464$
        # - Good, then it's 10,000 mesos for a $item:30000253$.
        if pick == 0:
            # $script:0831180407002465$
            # - Here's the money.
            # TODO: goto 136
            # TODO: gotoFail 137
            return 137
        return -1

    def __136(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002466$
        # - Here's your $item:30000253$. I hope you enjoy your new home. Bye for now!
        return -1

