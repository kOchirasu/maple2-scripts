""" 11000994: Lotachi """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        return random.choice([40, 50, 60])

    def select(self) -> int:
        return 0

    # Job
    def __1(self, index: int, pick: int) -> int:
        # $script:0831180610001120$
        # - Civilian ships are prohibited from sailing the waters around $map:02000183$. But for the low, low price of <font color="#ffd200">4,000</font> mesos, I can smuggle you into the area. Do you want to cast off now?
        return -1

    def __61(self, index: int, pick: int) -> int:
        # $script:1209001710001310$
        # - All civilian ships are prohibited from sailing in that direction. Just a moment, I feel a cough coming on... no, false alarm. Okay, as I was saying, civilians are banned, but... if you really want to go, I could smuggle you in for a price—Hnrghh! Hurrgh! Ow, the cough's back... Hnrrgh! Hnrgh! Ahem! You see, I'm a master smuggler—hrrgh! Hurgh! Oh, who am I kidding? I can't sound like a smooth criminal with this cough. Look, it'll be 4,000 mesos to take you there. Please just pretend I said that with some gravitas.
        if pick == 0:
            # $script:1210013910001316$
            # - Don't worry, I'll get you what you need to wet your whistle.
            # TODO: goto 62
            # TODO: gotoFail 63
            return 63
        return -1

    def __64(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:1210233210001318$
        # - Okay. Argh, I can feel another coughing fit coming on! Leave me before you catch something!
        return -1
