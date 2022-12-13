""" 11004317: Maple Spin """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1001153510002190$
        # - Give us 1 $item:30001202$ for a chance to spin the $npc:11004317$. How about it? Feeling lucky?
        if pick == 0:
            # $script:1001153510002191$
            # - (Pay 1 $item:30001202$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:1001153510002192$
            # - (Pay 10 $itemPlural:30001202$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:1001153510002193$
            # - (Pay 100 $itemPlural:30001202$ for a bunch of spins in a row!)
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:1001153510002194$
            # - Wonderful! Are you ready to spin?
            return 31
        elif index == 1:
            # $script:1001153510002195$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1001153510002196$
        # - You don't have enough coins. You need 1 $itemPlural:30001202$ to spin the $npc:11004317$ once.
        return -1

    def __40(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:1001153510002197$
            # - You need at least 1 $item:30001202$ to spin $npcName:11004317$. And you can get $itemPlural:30001202$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating!
            return 40
        elif index == 1:
            # $script:1001153510002198$
            # - If you have $itemPlural:30001202$ to burn, be sure to come to $map:63000064$!
            return -1
        return -1

    def __10(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:1001153510002199$
            # - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
            return 10
        elif index == 1:
            # $script:1001153510002200$
            # - Spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:1001153510002201$
            # - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
            return 100
        elif index == 1:
            # $script:1001153510002202$
            # - Spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

