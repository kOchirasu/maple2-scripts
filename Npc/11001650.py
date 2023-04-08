""" 11001650: Junkyard Worker 1 """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return -1  # No dialogue

    def select(self) -> int:
        return 0
