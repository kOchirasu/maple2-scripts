""" 11003511: Premium Lucky Wheel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0809174410001881$
        # - Welcome! Pay me 5 $itemPlural:30000875$ and I'll let you spin the $npc:11003511$! How about it? Feeling lucky?
        if pick == 0:
            # $script:0809174410001882$
            # - Pay 5 $itemPlural:30000875$ to spin once.
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0809174410001883$
            # - Pay 50 $itemPlural:30000875$ to spin continuously.
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0809174410001884$
            # - Pay 500 $itemPlural:30000875$ to spin continuously.
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0809174410001885$
            # - Spin the roulette for a chance to win great prizes! Come on, you know you want to!
            return 31
        elif index == 1:
            # $script:0809174410001886$
            # - May Lady Luck blow you a kiss, $MyPCName$!
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0809174410001887$
        # - You don't have enough coins. You need 5 $itemPlural:30000875$ to spin the $npc:11003511$ once.
        return -1

    def __40(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0809174410001888$
            # - To spin the $npc:11003511$, you need 5 $itemPlural:30000875$. Clear a premium dungeon to get $itemPlural:30000875$.
            return 40
        elif index == 1:
            # $script:0809174410001889$
            # - If you have $itemPlural:30000875$ to burn, be sure to come to $map:02000064$!
            return -1
        return -1

    def __10(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0809174410001890$
            # - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
            return 10
        elif index == 1:
            # $script:0809174410001891$
            # - Roulette spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0809174410001892$
            # - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
            return 100
        elif index == 1:
            # $script:0809174410001893$
            # - Roulette spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

