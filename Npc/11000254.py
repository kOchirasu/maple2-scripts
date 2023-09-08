""" 11000254: Jane """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 60


    def __60(self, index: int, pick: int) -> int:
        # $script:0831180407001060$
        # - Hey, there! If you've got a style in mind, we can make it happen. If you don't, maybe a magazine will inspire you. Want one?
        if pick == 0:
            # $script:0831180407001061$
            # - Yep.
            if self.has_item(39000014):
                return 62  # Already have item
            if self.reward_item([(39000014, 1, 1)]):
                return 61
            return 63  # Inventory is full
        elif pick == 1:
            # $script:0831180407001062$
            # - I'd like some advice.
            return 64
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
