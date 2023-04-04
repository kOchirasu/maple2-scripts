""" 11000096: Deke """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # Script ID 50 is a duplicate of 40, labeled feature Soulbinder. Script ID 30 is a pre-restart quest sensitive script, though it is unclear which specific quest that may be.
        return 40

    def select(self) -> int:
        return 0
