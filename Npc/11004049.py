""" 11004049: Carriage Tender """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0
