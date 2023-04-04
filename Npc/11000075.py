""" 11000075: Ereve """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # Script ID 10 is a pre-restart lore related dialog. Script IDs 30 and 40 are pre-restart quest sensitive scripts, though it is unclear which specific quests that may be.
        return 20

    def select(self) -> int:
        return 0
