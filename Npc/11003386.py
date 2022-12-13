""" 11003386: 2nd Anniversary Wheel of Joy """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0622191110001845$
        # - Welcome! Pay me 5 $itemPlural:30000782$, and I'll let you spin the $npcName:11003386$. How about it? Feeling lucky?
        if pick == 0:
            # $script:0622191110001846$
            # - Pay 5 $itemPlural:30000782$ to spin once.
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0622191110001847$
            # - Pay 50 $itemPlural:30000782$ to spin continuously.
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0622191110001848$
            # - Pay 500 $itemPlural:30000782$ to spin continuously.
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0622191110001849$
            # - Spin the roulette for a chance to win great prizes!
            #   Come on, you know you want to!
            return 31
        elif index == 1:
            # $script:0622191110001850$
            # - May Lady Luck blow you a kiss, $MyPCName$!
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0622191110001851$
        # - You don't have enough coins.
        #   Therefore, you need 5 <font color="#ffd200">$itemPlural:30000782$</font> to spin $npc:11003386$ once.
        return -1

    def __40(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0622191110001852$
            # - For one spin of $npcName:11003386$, you need 5 $itemPlural:30000782$. And guess what? You get $itemPlural:30000782$ in your mailbox every day just for logging in! You also get bonus coins as you spend more time in Maple World. And let's not forget that many of our events also give away coins just for participating!
            return 40
        elif index == 1:
            # $script:0622191110001853$
            # - If you have $itemPlural:30000782$ to burn, be sure to come to $map:63000055$!
            return -1
        return -1

    def __10(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0622191110001854$
            # - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
            return 10
        elif index == 1:
            # $script:0622191110001855$
            # - Roulette spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0622191110001856$
            # - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
            return 100
        elif index == 1:
            # $script:0622191110001857$
            # - Roulette spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

