""" 11000043: Trini """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        x = self.job()//10
        if self.level() >= 10 and x == 1:
            return 1
        if x == 40:
            return 20
        if x < 50:
            return x + 20
        return x + 10

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180610000150$
            # - The recent earthquake has struck fear into the hearts of many. We restore the people's hope by spreading the goddess's teachings. Would you join us on our holy mission? You seem more than qualified to serve the goddess.
            return 1
        elif index == 1:
            # functionID=1
            # $script:0831180610000151$
            # - Illuminate this world with your good heart and unshakable faith.
            #   The goddess awaits with open arms all who you will shepherd into the light.
            return -1
        return -1
