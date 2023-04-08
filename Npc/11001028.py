""" 11001028: Mett """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 51, 52])

    def select(self) -> int:
        return 0
