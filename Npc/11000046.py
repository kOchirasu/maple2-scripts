""" 11000046: Jenna """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180610000235$
            # - Everyone's so on edge right now, but not me... In fact, I can't wait to show the rest of the world what I can do! How about we forget about everything and go blow some stuff up? I'll even help you pick out your own cannon.
            return 1
        elif index == 1:
            # functionID=1
            # $script:0831180610000236$
            # - I'm not afraid of anything as long as I've got my giant cannon with me. Unlike people, it'll never disappoint me. What do you say, want to become a Heavy Gunner?
            return -1
        return -1
