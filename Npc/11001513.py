""" 11001513: Paulie """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 1


    def exit_state(self, functionId: int):
        if functionId == 1:
            self.move_player(99)
            self.open_dialog("BeautyShopDialog", "hair,random")
        return

    def enter_state(self, functionId: int):
        return
