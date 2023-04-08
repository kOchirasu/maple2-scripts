""" 11000157: Paul """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: uncomment once quests are implemented. Script ID 30 must play only when quest 91000061 in ongoing.
        # if self.quest_state(91000061, 2):
        #    return 30
        return 50

    def select(self) -> int:
        return 0
