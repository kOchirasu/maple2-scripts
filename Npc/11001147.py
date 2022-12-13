""" 11001147: Magic Pot """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])

    def select(self) -> int:
        return 0

    def __21(self, index: int, pick: int) -> int:
        # $script:0916043407003995$
        # - (Add the first ingredient.) 
        if pick == 0:
            # $script:0916043407003996$
            # - (Add 10 $itemPlural:30000390$.)
            # TODO: goto 41
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:0916043407003997$
            # - (Add 9 $itemPlural:30000390$.)
            # TODO: goto 42
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:0916043407003998$
            # - (Add 8 $itemPlural:30000390$.)
            # TODO: goto 22
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:0916043407003999$
            # - (Add 7 $itemPlural:30000390$.)
            # TODO: goto 44
            # TODO: gotoFail 28
            return 28
        return -1

    def __22(self, index: int, pick: int) -> int:
        # $script:0916043407004000$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:0916043407004001$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 23
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:0916043407004002$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:0916043407004003$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:0916043407004004$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __23(self, index: int, pick: int) -> int:
        # $script:0916043407004005$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:0916043407004006$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:0916043407004007$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:0916043407004008$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:0916043407004009$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 24
            # TODO: gotoFail 28
            return 28
        return -1

    def __24(self, index: int, pick: int) -> int:
        # $script:0916043407004010$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:0916043407004011$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:0916043407004012$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 25
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:0916043407004013$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:0916043407004014$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

    def __25(self, index: int, pick: int) -> int:
        # $script:0916043407004015$
        # - <font color="#909090">(Continue cooking the dish.)</font>
        if pick == 0:
            # $script:0916043407004016$
            # - (Cook over high heat for 5 minutes.)
            return 35
        elif pick == 1:
            # $script:0916043407004017$
            # - (Cook over high heat for 3 minutes.)
            return 35
        elif pick == 2:
            # $script:0916043407004018$
            # - (Cook over low heat for 5 minutes.)
            # TODO: goto 26
            # TODO: gotoFail 27
            return 27
        elif pick == 3:
            # $script:0916043407004019$
            # - (Cook over low heat for 3 minutes.)
            return 35
        return -1

    def __26(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0916043407004020$
        # - <font color="#909090">(The syrupy candy crystallizes into a $item:30000395$ with a pop. 
        #   Quickly, remove the candy from the $npcName:11001147$!)</font>
        return -1

    def __41(self, index: int, pick: int) -> int:
        # $script:1027181907004303$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004304$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 51
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004305$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004306$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004307$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __42(self, index: int, pick: int) -> int:
        # $script:1027181907004308$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004309$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 51
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004310$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004311$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004312$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __43(self, index: int, pick: int) -> int:
        # $script:1027181907004313$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004314$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 51
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004315$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004316$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004317$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __44(self, index: int, pick: int) -> int:
        # $script:1027181907004318$
        # - <font color="#909090">(Add the second ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004319$
            # - (Add 10 $itemPlural:30000392$.)
            # TODO: goto 51
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004320$
            # - (Add 9 $itemPlural:30000392$.)
            # TODO: goto 52
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004321$
            # - (Add 8 $itemPlural:30000392$.)
            # TODO: goto 53
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004322$
            # - (Add 7 $itemPlural:30000392$.)
            # TODO: goto 54
            # TODO: gotoFail 28
            return 28
        return -1

    def __51(self, index: int, pick: int) -> int:
        # $script:1027181907004323$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004324$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004325$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004326$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004327$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 64
            # TODO: gotoFail 28
            return 28
        return -1

    def __52(self, index: int, pick: int) -> int:
        # $script:1027181907004328$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004329$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004330$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004331$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004332$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 64
            # TODO: gotoFail 28
            return 28
        return -1

    def __53(self, index: int, pick: int) -> int:
        # $script:1027181907004333$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004334$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004335$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004336$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004337$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 64
            # TODO: gotoFail 28
            return 28
        return -1

    def __54(self, index: int, pick: int) -> int:
        # $script:1027181907004338$
        # - <font color="#909090">(Add the third ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004339$
            # - (Add 10 $itemPlural:30000391$.)
            # TODO: goto 61
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004340$
            # - (Add 9 $itemPlural:30000391$.)
            # TODO: goto 62
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004341$
            # - (Add 8 $itemPlural:30000391$.)
            # TODO: goto 63
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004342$
            # - (Add 7 $itemPlural:30000391$.)
            # TODO: goto 64
            # TODO: gotoFail 28
            return 28
        return -1

    def __61(self, index: int, pick: int) -> int:
        # $script:1027181907004343$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004344$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004345$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 72
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004346$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004347$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

    def __62(self, index: int, pick: int) -> int:
        # $script:1027181907004348$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004349$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004350$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 72
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004351$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004352$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

    def __63(self, index: int, pick: int) -> int:
        # $script:1027181907004353$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004354$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004355$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 72
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004356$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004357$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

    def __64(self, index: int, pick: int) -> int:
        # $script:1027181907004358$
        # - <font color="#909090">(Add the fourth ingredient.)</font> 
        if pick == 0:
            # $script:1027181907004359$
            # - (Add 10 $itemPlural:30000393$.)
            # TODO: goto 71
            # TODO: gotoFail 28
            return 28
        elif pick == 1:
            # $script:1027181907004360$
            # - (Add 9 $itemPlural:30000393$.)
            # TODO: goto 72
            # TODO: gotoFail 28
            return 28
        elif pick == 2:
            # $script:1027181907004361$
            # - (Add 8 $itemPlural:30000393$.)
            # TODO: goto 73
            # TODO: gotoFail 28
            return 28
        elif pick == 3:
            # $script:1027181907004362$
            # - (Add 7 $itemPlural:30000393$.)
            # TODO: goto 74
            # TODO: gotoFail 28
            return 28
        return -1

