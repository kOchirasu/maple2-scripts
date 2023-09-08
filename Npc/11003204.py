""" 11003204: Gogh """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])


