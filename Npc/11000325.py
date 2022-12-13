""" 11000325: Gordon """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180407001316$
        # - I'm here to help you find the perfect car for your style and needs. What kind of car do you like?
        if pick == 0:
            # $script:0831180407001317$
            # - Rugged 4-wheel-drives.
            # TODO: goto 33, 37
            # TODO: gotoFail 34
            return 34
        elif pick == 1:
            # $script:0831180407001318$
            # - Luxurious sports cars.
            return 35
        elif pick == 2:
            # $script:0831180407001319$
            # - No cage for me! I want a bike.
            return 36
        return -1

    def __33(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=1 
            # $script:0831180407001320$
            # - Ooh, you've got excellent taste! 4-wheel-drive vehicles are designed to handle a wider variety of terrain, including fields, swamps, sand, slopes, and so on.
            return 33
        elif index == 1:
            # openTalkReward=True 
            # $script:0831180407001321$
            # - Lucky for you, I've got one 4-wheel-drive model brochure left. Would you like to take a look?
            return -1
        return -1

