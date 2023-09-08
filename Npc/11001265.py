""" 11001265: Eupheria """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 60, 70])


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

    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        if functionId == 3:
            # TODO: functionID 3
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        if functionId == 2:
            # TODO: functionID 2
            return
        if functionId == 3:
            # TODO: functionID 3
            return
        return
