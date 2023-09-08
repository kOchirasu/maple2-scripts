""" 11001665: Karl """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])


