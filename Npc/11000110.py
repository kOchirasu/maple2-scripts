""" 11000110: Cavan """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 50])


