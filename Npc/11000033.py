""" 11000033: Jorge """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: uncomment once quests are implemented. Script ID 40 must play only if one the following quests are ongoing: 50001573, 50001580-50001584, 50001603-50001665, 50001669 and player is in map 02000023
        # if self.multi_quest_state(["50001573", "50001580", 50001581", "50001582", "50001583", "50001584", "50001603", "50001604", "50001665", "50001669"], 2) and self.current_map() == 02000023:
        #    return 40
        return 50

    def select(self) -> int:
        return 0

    def __41(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0530154307008542$
        # - $npcName:11000031[gender:0]$ says you're all right, so fine. Off you go.
        self.move_player(105)
        return -1
