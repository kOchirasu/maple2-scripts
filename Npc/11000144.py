""" 11000144: Tristan """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 50, 60])

    def select(self) -> int:
        return 0

