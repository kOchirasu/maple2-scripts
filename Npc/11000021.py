""" 11000021: Santiago """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: uncomment once quests are implemented. Script ID 40 must play only when quest 10001000 in ongoing.
        # if self.quest_state(10001000, 2):
        #    return 40
        return 10

    def select(self) -> int:
        return 0
