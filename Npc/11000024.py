""" 11000024: Lydia """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: uncomment once quests are implemented. Script ID 40 must play only when quest 91000020 in ongoing.
        # if self.quest_state(91000020, 2):
        #    return 40
        return 30

    def select(self) -> int:
        return 0
