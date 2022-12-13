""" 11003688 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1110142010001931$
        # - Give us 3 $itemPlural:30001010$ for a chance to spin the $npc:11003688$. How about it? Feeling lucky?
        if pick == 0:
            # $script:1110142010001932$
            # - (Pay 3 $item:30001010$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:1110142010001933$
            # - (Pay 30 $itemPlural:30001010$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:1110142010001934$
            # - (Pay 300 $itemPlural:30001010$ for a bunch of spins in a row!)
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:1110142010001935$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 31
        elif index == 1:
            # $script:1110142010001936$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:1110142010001937$
        # - You don't have enough coins. You need 3 $itemPlural:30001010$ to spin the $npc:11003688$ once.
        return -1

    def __40(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:1110142010001938$
            # - For one spin of $npcName:11003688$, you need 3 $itemPlural:30001010$. And guess what? You get $itemPlural:30001010$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating!
            return 40
        elif index == 1:
            # $script:1110142010001939$
            # - If you have $itemPlural:30001010$ to burn, be sure to come to $map:63000057$!
            return -1
        return -1

    def __10(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:1110142010001940$
            # - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
            return 10
        elif index == 1:
            # $script:1110142010001941$
            # - Spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:1110142010001942$
            # - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
            return 100
        elif index == 1:
            # $script:1110142010001943$
            # - Spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

