""" 11000003: Growlie """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: uncomment once quests are implemented. Script ID 60 must play only when quest 91000021 in ongoing. Script ID 40 is never played.
        # if self.quest_state(91000021, 2):
        #    return 60
        return 50

    def select(self) -> int:
        return 0
