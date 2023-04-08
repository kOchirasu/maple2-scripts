""" 11004552: Chocola """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([90, 100, 110])

    def select(self) -> int:
        return 30

    def __90(self, index: int, pick: int) -> int:
        # $script:0116132907012729$
        # - Hey, do you need a Valentine chocolate box and some sprinkles? I've got some that I can give you. If you keep making chocolate every day, you'll get a special gift!
        if pick == 0:
            # $script:0116132907012730$
            # - Give me a $item:30001287$ and $item:30001288$!
            # TODO: goto 91
            # TODO: gotoFail 92
            return 92
        return -1

    def __91(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0116132907012731$
        # - Here you go! I hope you save some chocolate for me!
        return -1
