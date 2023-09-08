""" 11004324: Lennon """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])


