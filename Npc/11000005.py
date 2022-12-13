""" 11000005: Anne """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([80, 90])

    def select(self) -> int:
        return 0

