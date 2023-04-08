""" 11000116: Anthony """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __31(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1
            # $script:0831180407000496$
            # - ...
            return 31
        elif index == 1:
            # $script:0831180407000497$
            # - All right. Fine. Just keep thinking that way.
            return -1
        return -1
