""" 11000633: Caron """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 60])

    def select(self) -> int:
        return 0

    def __50(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180407002573$
        # - For more information about the prison, please refer to this brochure. Enjoy your tour.
        return -1
