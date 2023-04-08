""" 11000119: Frey """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: uncomment once quests are implemented. Script ID 70 must play only when quest 91000022 in ongoing.
        # if self.quest_state(91000022, 2):
        #    return 70
        return random.choice([40, 120])

    def select(self) -> int:
        return 0
