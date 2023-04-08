""" 11000585: Seamus """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        if self.has_mesos(1000):
            return 1
        return random.choice([40])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180610000844$
            # - Welcome to the $map:02000124$ cruise ship!
            return 1
        elif index == 1:
            # $script:0831180610000845$
            # - $map:02000124$ is where the worst criminals of all get locked up. We run tours to show the free, law-abiding citizens why they should stay law-abiding.
            return 1
        elif index == 2:
            # $script:0831180610000846$
            # - It's <font color="#ffd200">1,000 mesos</font> to take a tour of the prison.
            #   Are you interested?
            return -1
        return -1
