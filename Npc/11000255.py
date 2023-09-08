""" 11000255: Rosetta """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 1

    def exit_state(self, functionId: int):
        if functionId == 1:
            self.move_player(99)
            self.open_dialog("BeautyShopDialog", "hair,style")
            return
        return

    def enter_state(self, functionId: int):
        return
