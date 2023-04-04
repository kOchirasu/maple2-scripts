""" 11000005: Anne """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: uncomment once quests are implemented. Script ID 80 must play only when quest 91000061 in ongoing.
        #if self.quest_state(91000061, 2):
        #    return 80
        return 90

    def select(self) -> int:
        return 0
