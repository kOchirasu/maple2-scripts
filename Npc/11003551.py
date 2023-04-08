""" 11003551 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0902174710001915$
        # - Give us 3 $itemPlural:30000878$ for a chance to spin the $npc:11003551$. How about it? Feeling lucky?
        if pick == 0:
            # $script:0902174710001916$
            # - (Pay 3 $item:30000878$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0902174710001917$
            # - (Pay 30 $itemPlural:30000878$ for a bunch of spins in a row!)
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0902174710001918$
            # - (Pay 300 $itemPlural:30000878$ for a bunch of spins in a row!)
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1
            # $script:0902174710001919$
            # - Spin the roulette for a chance to win great prizes!
            #   Come on, you know you want to!
            return 31
        elif index == 1:
            # $script:0902174710001920$
            # - May Lady Luck blow you a kiss, $MyPCName$!
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0902174710001921$
        # - You don't have enough coins.
        #   Therefore, you need 3 <font color="#ffd200">$itemPlural:30000878$</font> to spin $npc:11003551$ once.
        return -1

    def __40(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1
            # $script:0902174710001922$
            # - For one spin of $npcName:11003551$, you need 3 $itemPlural:30000878$. And guess what? You get $itemPlural:30000878$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating!
            return 40
        elif index == 1:
            # $script:0902174710001923$
            # - If you have $itemPlural:30000878$ to burn, be sure to come to $map:63000057$!
            return -1
        return -1

    def __10(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1
            # $script:0902174710001924$
            # - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
            return 10
        elif index == 1:
            # $script:0902174710001925$
            # - Roulette spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1
            # $script:0902174710001926$
            # - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
            return 100
        elif index == 1:
            # $script:0902174710001927$
            # - Roulette spin number $rouletteCurrent$! Good luck!
            return -1
        return -1
