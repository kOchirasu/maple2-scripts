""" 11000074: Karl """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: uncomment once quests are implemented. Script ID 40 must play only when quest 91000022 in ongoing.
        #if self.quest_state(91000022, 2):
        #    return 40
        return 20 if random.random() > 0.7 else 10

    def select(self) -> int:
        return 0
