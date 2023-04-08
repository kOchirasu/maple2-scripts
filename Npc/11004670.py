""" 11004670: NPCNAME_11004670_NAME:[F]Event """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0
