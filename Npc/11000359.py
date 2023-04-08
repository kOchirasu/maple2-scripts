""" 11000359: Hendel """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0
