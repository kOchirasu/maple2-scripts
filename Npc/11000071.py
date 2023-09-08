""" 11000071: Dixon """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 1


    def exit_state(self, functionId: int):
        if functionId == 1:
            self.move_player(99)
            self.open_dialog("BeautyShopDialog", "face")
        return

    def enter_state(self, functionId: int):
        return
