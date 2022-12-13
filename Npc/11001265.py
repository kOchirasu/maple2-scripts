""" 11001265: Eupheria """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 60, 70])

    def select(self) -> int:
        return 0

    def __52(self, index: int, pick: int) -> int:
        # $script:1216035207005151$
        # - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
        if pick == 0:
            # $script:1216035207005152$
            # - Sure.
            # TODO: goto 53
            # TODO: gotoFail 90
            return 90
        return -1

    def __53(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:1216035207005153$
        # - Here, take it. You're lucky I transcribed an extra copy.
        return -1

    def __62(self, index: int, pick: int) -> int:
        # $script:1216035207005159$
        # - You're here for the $item:40000024$? Please wait a moment.
        if pick == 0:
            # $script:1216035207005160$
            # - (Wait several moments.)
            # TODO: goto 63
            # TODO: gotoFail 69
            return 69
        return -1

    def __64(self, index: int, pick: int) -> int:
        # $script:1216035207005163$
        # - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
        if pick == 0:
            # $script:1216035207005164$
            # - Sure.
            # TODO: goto 65
            # TODO: gotoFail 90
            return 90
        return -1

    def __65(self, index: int, pick: int) -> int:
        # functionID=2 openTalkReward=True 
        # $script:1216035207005165$
        # - Here, take it. You're lucky I transcribed an extra copy.
        return -1

    def __72(self, index: int, pick: int) -> int:
        # $script:1216031507005132$
        # - You're here for the $item:40000023$? Please wait a moment.
        if pick == 0:
            # $script:1216031507005133$
            # - (Wait several moments.)
            # TODO: goto 73
            # TODO: gotoFail 79
            return 79
        return -1

    def __74(self, index: int, pick: int) -> int:
        # $script:1216031507005136$
        # - I know we wouldn't have found it without you, but please... don't lose this again. It contains valuable information regarding our legacy as Runeblades!
        if pick == 0:
            # $script:1216031507005137$
            # - Sure.
            # TODO: goto 75
            # TODO: gotoFail 90
            return 90
        return -1

    def __75(self, index: int, pick: int) -> int:
        # functionID=3 openTalkReward=True 
        # $script:1216031507005138$
        # - Here, take it. You're lucky I transcribed an extra copy.
        return -1

