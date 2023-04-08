""" 11004288: MC Nagi """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

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

    def __30(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0218154407014484$
        # - Taking it from the top, eh? Exciting! Now, let's get to it!
        return -1

    def __40(self, index: int, pick: int) -> int:
        # functionID=2
        # $script:0218154407014485$
        # - You already beat everyone, ya goof! Why don't we start over, instead?
        return -1

    def __50(self, index: int, pick: int) -> int:
        # functionID=3
        # $script:0226191507014580$
        # - Great! Keep up that fighting spirit! Now start!
        return -1

    def __60(self, index: int, pick: int) -> int:
        # functionID=4
        # $script:0226191507014581$
        # - Here's your first challenge. Good luck!
        return -1
