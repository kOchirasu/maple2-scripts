""" 11000430: Antoine """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 41])

    def select(self) -> int:
        return 0

