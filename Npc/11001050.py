""" 11001050: Lazy Prisoner 11 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return -1  # No dialogue

    def select(self) -> int:
        return 0
