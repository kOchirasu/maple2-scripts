""" 11000745: Ghanush """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 60])


    def __30(self, index: int, pick: int) -> int:
        # $script:0831180407002894$
        # - Do you want to challenge me? You know how to play rock-paper-scissors, right? Heh, let's do it. Rock, paper, scissors!
        if pick == 0:
            # $script:0831180407002895$
            # - Scissors!
            # TODO: goto 31, 32, 33, 34, 35
            return -1
        elif pick == 1:
            # $script:0831180407002896$
            # - Rock!
            # TODO: goto 36, 37, 38, 39, 40
            return -1
        elif pick == 2:
            # $script:0831180407002897$
            # - Paper!
            # TODO: goto 41, 42, 43, 44, 45
            return -1
        return -1

    def __46(self, index: int, pick: int) -> int:
        # $script:0831180407002928$
        # - <font color="#909090">(She gives you a sideways scowl.)</font> 
        #   I think you played after I did. You're lucky that my eyes are too old to see clearly.
        if pick == 0:
            # $script:0831180407002929$
            # - Don't you have something for me?
            # TODO: goto 47, 48
            # TODO: gotoFail 49
            return 49
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180407002933$
        # - Let's get to it! Rock, paper, scissors!
        if pick == 0:
            # $script:0831180407002934$
            # - Scissors!
            # TODO: goto 31, 32, 33, 34, 35
            return -1
        elif pick == 1:
            # $script:0831180407002935$
            # - Rock!
            # TODO: goto 36, 37, 38, 39, 40
            return -1
        elif pick == 2:
            # $script:0831180407002936$
            # - Paper!
            # TODO: goto 41, 42, 43, 44, 45
            return -1
        return -1

    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        return
