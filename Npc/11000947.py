""" 11000947: Theodore """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([10])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # $script:0831180610001102$
        # - You look a right mess! How about I treat you? It'll only be a measly $paneltyPrice$ mesos.
        #   Don't worry, I'm a real doctor!
        return -1

