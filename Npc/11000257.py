""" 11000257: Douglas """
from npc_api import Script


class Main(Script):
    def first(self) -> int:
        return 1

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180610000413$
        # - Being strong is important, but looking fabulous while you fight is the true key to happiness, y'know. So... wanna spruce up your gear?
        if pick == 0:
            # $script:0831180610000414$
            # - Yes! I need more color in my life!
            self.move_player(99)
            self.open_dialog("BeautyShopDialog", "itemcolor")
            return -1
        return -1

