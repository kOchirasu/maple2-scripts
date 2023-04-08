""" 11000050: Char """
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
            # $script:0831180610000287$
            # - Justice is just an concept whose meaning no one can even agree on, so how important could it really be? Live free! Laws are for sheep. You've gotta take what you want, that's just the way the world works.
            return 1
        elif index == 1:
            # functionID=1
            # $script:0831180610000288$
            # - If you wanna win, you've gotta be strong. I can teach you how to be strong.
            return -1
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=70
        # $script:0831180610000299$
        # - Congratulations, $MyPCName$, and welcome to the seedy underbelly of society. Now it's time you learned our ways, from surprise attacks to poisoned blades.
        if pick == 0:
            # $script:0831180610000300$
            # - What should I do now?
            return 21
        return -1

    def __21(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=60
            # $script:0831180610000303$
            # - To take down your enemies you've gotta be fast and precise. For that, you'll need a sharp dagger. $npc:11000004[gender:0]$ should have all kinds of Thief gear. So go get yourself a shiny new blade and use it to carve your own path in life.
            return 21
        elif index == 1:
            # functionID=60
            # $script:0831180610000304$
            # - Stab enough things, and eventually you'll reach a new level, and that means you get to learn new skills. To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=60
            # $script:0831180610000305$
            # - When you're ready to <font color="#ffd200">upgrade a skill</font>, just press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve.
            return 22
        elif index == 1:
            # functionID=60
            # $script:0831180610000306$
            # - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
            return -1
        return -1

    def __23(self, index: int, pick: int) -> int:
        if index == 0:
            # functionID=60
            # $script:0831180610000307$
            # - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>.
            return 23
        elif index == 1:
            # functionID=60
            # $script:0831180610000308$
            # - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
            return 23
        elif index == 2:
            # functionID=60
            # $script:0831180610000309$
            # - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently. So yeah, getting hold of them is no easy feat.
            return 23
        elif index == 3:
            # functionID=60
            # $script:0831180610000310$
            # - And as for $itemPlural:40100022$—well, you can figure that out on your own time.
            return -1
        return -1

    def __30(self, index: int, pick: int) -> int:
        # functionID=10
        # $script:0831180610000311$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Knight here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000312$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000313$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __40(self, index: int, pick: int) -> int:
        # functionID=20
        # $script:0831180610000314$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Berserker here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000315$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000316$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __50(self, index: int, pick: int) -> int:
        # functionID=30
        # $script:0831180610000317$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Wizard here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000318$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000319$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __60(self, index: int, pick: int) -> int:
        # functionID=40
        # $script:0831180610000320$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Priest here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000321$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000322$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __70(self, index: int, pick: int) -> int:
        # functionID=50
        # $script:0831180610000323$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to an Archer here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000324$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000325$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __80(self, index: int, pick: int) -> int:
        # functionID=60
        # $script:0831180610000326$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Heavy Gunner here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000327$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000328$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __90(self, index: int, pick: int) -> int:
        # functionID=80
        # $script:0831180610000329$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to an Assassin here. Sure you've crossed some lines, but you're still just a cog in the machine. Just go on your merry way.
        if pick == 0:
            # $script:0831180610000330$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000331$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __100(self, index: int, pick: int) -> int:
        # functionID=90
        # $script:1216124310001337$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Runeblade here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:1216124310001338$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:1216124310001339$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __110(self, index: int, pick: int) -> int:
        # functionID=100
        # $script:0607163510001542$
        # - $MyPCName$, I can tell you how to get what you want. Oh, wait... I see now you're not a Thief. Well, then you wouldn't even know what freedom is. Just go along your merry way.
        if pick == 0:
            # $script:0607163510001543$
            # - Okay, try me. What's freedom?
            return 11
        elif pick == 1:
            # $script:0607163510001544$
            # - Oh yeah? How can I get anything I want?
            return 12
        elif pick == 2:
            # $script:0607163510001545$
            # - I don't want to talk about this anymore.
            return 13
        return -1

    def __120(self, index: int, pick: int) -> int:
        # functionID=110
        # $script:0806014810001669$
        # - $MyPCName$, I can tell you <font color="#ffd200">how to get what you want</font>.
        #   Oh, wait... I see now you're not a Thief. Well, then you wouldn't even know what <font color="#ffd200">freedom</font> is. Just go along your merry way.
        if pick == 0:
            # $script:0806014810001670$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0806014810001671$
            # - Oh yeah? How can I get anything I want?
            return 12
        elif pick == 2:
            # $script:0806014810001672$
            # - Talk to $npcName:11000050[gender:0]$ about a different subject.
            return 16
        return -1
