""" 11000215: Evan """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30, 40, 50, 60, 70, 80, 100])


    def __20(self, index: int, pick: int) -> int:
        # $script:0831180407000913$
        # - Mm? What is it? Are you having a problem posting $item:30000038$?
        if pick == 0:
            # $script:0831180407000914$
            # - Actually, I kinda lost my $item:30000038$...
            # TODO: goto 21, 22
            # TODO: gotoFail 23
            return 23
        elif pick == 1:
            # $script:0831180407000915$
            # - Where am I supposed to post $item:30000038$ again?
            return 24
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180407000920$
        # - Mm? What is it? Are you having a problem posting $item:30000038$?
        if pick == 0:
            # $script:0831180407000921$
            # - Actually, I kinda lost my $item:30000038$...
            # TODO: goto 31, 32
            # TODO: gotoFail 33
            return 33
        elif pick == 1:
            # $script:0831180407000922$
            # - Where am I supposed to post $item:30000038$ again?
            return 34
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180407000927$
        # - Mm? What is it? Are you having a problem posting $item:30000038$?
        if pick == 0:
            # $script:0831180407000928$
            # - Actually, I kinda lost my $item:30000038$...
            # TODO: goto 41, 42
            # TODO: gotoFail 43
            return 43
        elif pick == 1:
            # $script:0831180407000929$
            # - Where am I supposed to post $item:30000038$ again?
            return 44
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180407000934$
        # - Mm? What is it? Are you having a problem posting $item:30000038$?
        if pick == 0:
            # $script:0831180407000935$
            # - Actually, I kinda lost my $item:30000038$...
            # TODO: goto 51, 52
            # TODO: gotoFail 53
            return 53
        elif pick == 1:
            # $script:0831180407000936$
            # - Where am I supposed to post $item:30000038$ again?
            return 54
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
        if functionId == 5:
            # TODO: functionID 5
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
        if functionId == 5:
            # TODO: functionID 5
            return
        return
