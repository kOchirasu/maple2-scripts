""" 11000208: Nick """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0
