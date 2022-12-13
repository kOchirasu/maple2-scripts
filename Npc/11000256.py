""" 11000256: Ren """
from npc_api import Script


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180610000406$
        # - Nothing expresses the inner YOU like carefully-selected cosmetics. How'd you like to experiment with a new look?
        if pick == 0:
            # $script:0831180610000407$
            # - Yep, time to accessorize!
            self.move_player(99)
            self.open_dialog("BeautyShopDialog", "makeup")
            return -1
        return -1

