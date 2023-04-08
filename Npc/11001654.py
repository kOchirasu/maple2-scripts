""" 11001654: Festival Lucky Wheel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __30(self, index: int, pick: int) -> int:
        # $script:0615152810001561$
        # - Give us 3 $itemPlural:30000554$ for a chance to spin the $npc:11001654$. How about it? Feeling lucky?
        if pick == 0:
            # $script:0620113310001566$
            # - (Pay 3 $itemPlural:30000554$ for 1 spin.)
            # TODO: goto 31
            # TODO: gotoFail 32
            return 32
        elif pick == 1:
            # $script:0125175010001818$
            # - Pay 30 $itemPlural:30000554$ to spin 10 times.
            # TODO: goto 10
            # TODO: gotoFail 32
            return 32
        elif pick == 2:
            # $script:0125175010001819$
            # - Pay 300 $itemPlural:30000554$ to spin 100 times.
            # TODO: goto 100
            # TODO: gotoFail 32
            return 32
        return -1

    def __31(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1
            # $script:0615152810001562$
            # - Spin the wheel for a chance at great prizes! You know you want to.
            return 31
        elif index == 1:
            # $script:0615152810001563$
            # - Here's hoping Lady Luck's on your side!
            return -1
        return -1

    def __10(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1
            # $script:0125175010001820$
            # - All right, let's spin it 10 times in a row! Keep your fingers crossed, $MyPCName$!
            return 10
        elif index == 1:
            # $script:0125175010001821$
            # - Roulette spin number $rouletteCurrent$! Good luck!
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1
            # $script:0125175010001822$
            # - All right, let's spin it 100 times in a row! Keep your fingers crossed, $MyPCName$!
            return 100
        elif index == 1:
            # $script:0125175010001823$
            # - Roulette spin number $rouletteCurrent$! Good luck!
            return -1
        return -1
