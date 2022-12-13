""" 11001257: Moren """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([30])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # $script:1203001410001290$
        # - You said you wanted me to send you where $npcName:11001229[gender:0]$ went, right? Well, that would be an inn on Victoria Island, in the city of Tria. Would you like to go there now?
        return -1

