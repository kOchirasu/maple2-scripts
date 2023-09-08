""" 11004288: MC Nagi """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 10


    def __10(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0218154407014480$
            # - Welcome to the rumble! You look like you're ready to get wild.
            return 10
        elif index == 1:
            # $script:0226180207014575$
            # - Let's start the match!
            if pick == 0:
                # $script:0226181607014578$
                # - I'm ready.
                # TODO: goto 20
                # TODO: gotoFail 60
                return 60
            return -1
        return -1

    def __20(self, index: int, pick: int) -> int:
        # $script:0218154407014481$
        # - So, what are we doing today?
        if pick == 0:
            # $script:0218154407014482$
            # - Start Over
            return 30
        elif pick == 1:
            # $script:0218154407014483$
            # - Continue
            # TODO: goto 40
            # TODO: gotoFail 50
            return 50
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
        if functionId == 4:
            # TODO: functionID 4
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
        if functionId == 4:
            # TODO: functionID 4
            return
        return
