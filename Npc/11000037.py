""" 11000037: Lea """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        if self.has_item(30000435):
            return 40
        return 30

    def select(self) -> int:
        return 0
