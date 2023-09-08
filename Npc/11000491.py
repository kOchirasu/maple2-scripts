""" 11000491: Cathy Catalina """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 70, 80])


