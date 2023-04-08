""" 11003784: Veliche """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])

    def select(self) -> int:
        return 0

    def __20(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0131125107009814$
            # - Need something?
            return 20
        elif index == 1:
            # $script:0131125107009815$
            # - It seems you came up to keep us supplied.
            #   There's no time to waste. Head to <font color="#ffd200">$map:52010063$</font> right away.
            return 20
        elif index == 2:
            # functionID=1
            # $script:0131125107009817$
            # - I'll arrange a transport for you.
            return -1
        return -1
