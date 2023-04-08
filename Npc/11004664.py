""" 11004664: NPCNAME_11004664_NAME:[F]Event """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return -1  # No dialogue

    def select(self) -> int:
        return 0
