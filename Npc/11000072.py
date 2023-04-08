""" 11000072: Zenko """
from npc_api import Script


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180610000389$
        # - Welcome, $MyPCName$. Thinking about spicing up your look? I can give you any skin tone you like. Care to take a peek?
        if pick == 0:
            # $script:0831180610000390$
            # - Yeah, let's do it!
            self.move_player(99)
            self.open_dialog("BeautyShopDialog", "skin")
            return -1
        return -1
