""" 11000351: Mirror """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 0


    def exit_state(self, functionId: int):
        if functionId == 1:
            self.move_player(99)
            self.open_dialog("BeautyShopDialog", "mirror")
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            self.move_player(99)
            self.open_dialog("BeautyShopDialog", "mirror")
        return
