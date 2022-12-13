""" 11000212: David """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 40])

    def select(self) -> int:
        return 0

