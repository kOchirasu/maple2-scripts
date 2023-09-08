""" 11004134: Ishura """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 100])


