""" 11000007: Ellie """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        if self.current_map() == 2000146:
            return 30
        return 40

    def select(self) -> int:
        return 1
