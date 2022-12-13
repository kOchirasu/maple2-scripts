""" 11004215: Stellar Chest """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 50])

    def select(self) -> int:
        return 0

    def __10(self, index: int, pick: int) -> int:
        # $script:0808172007010850$
        # - <font color="#909090">(Do you wish to create some $itemPlural:20301849$?)</font>
        if pick == 0:
            # $script:0808172007010851$
            # - (Create 1.)
            # TODO: goto 11
            # TODO: gotoFail 14
            return 14
        elif pick == 1:
            # $script:0808172007010852$
            # - (Create 10.)
            # TODO: goto 21
            # TODO: gotoFail 24
            return 24
        elif pick == 2:
            # $script:0808172007010853$
            # - (Not now.)
            return 15
        return -1

    def __11(self, index: int, pick: int) -> int:
        # $script:0808172007010854$
        # - <font color="#909090">(Consume 10 $itemPlural:30001187$ and 1 $item:30001188$ to make 1 $item:20301849$?)</font> 
        if pick == 0:
            # $script:0808172007010855$
            # - (Create 1 $item:20301849$.)
            # TODO: goto 12
            # TODO: gotoFail 13
            return 13
        return -1

    def __12(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0808172007010856$
        # - <font color="#909090">(The process has been completed. The chest awaits your next command.)</font> 
        return -1

    def __21(self, index: int, pick: int) -> int:
        # $script:0808172007010857$
        # - <font color="#909090">(Consume 100 $itemPlural:30001187$ and 10 $itemPlural:30001188$ to make 10 $itemPlural:20301849$?)</font> 
        if pick == 0:
            # $script:0808172007010858$
            # - (Create 10 $itemPlural:20301849$.)
            # TODO: goto 22
            # TODO: gotoFail 13
            return 13
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=2 openTalkReward=True 
        # $script:0808172007010859$
        # - <font color="#909090">(The process has been completed. The chest awaits your next command.)</font> 
        return -1

