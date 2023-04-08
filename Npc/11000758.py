""" 11000758: Rebecca """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509000472$
        # - Oh, you're back.
        if pick == 0:
            # $script:0831180509000473$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000474$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000475$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509000476$
        # - You got home later than usual.
        if pick == 0:
            # $script:0831180509000477$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000478$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000479$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509000480$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509000481$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000482$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000483$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509000484$
        # - Oh, you're back.
        if pick == 0:
            # $script:0831180509000485$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000486$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000487$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000488$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509000489$
        # - You got home later than usual.
        if pick == 0:
            # $script:0831180509000490$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000491$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000492$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000493$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509000494$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509000495$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000496$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000497$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000498$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509000499$
        # - Are you talking about my paycheck?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509000500$
            # - Never mind.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000501$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000502$
        # - Received. Thank you.
        #   <font color="#909090">(A fleeting smile appears on $MaidName$'s face.)</font>
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000503$
        # - It's been that long already, huh? ...Thank you.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000504$
        # - <font color="#909090">(She glances at the paycheck.)</font>
        #   I'm not quite sure what to say. Hmm... I'm glad this worked out.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000505$
        # - Then... I can go back to work, right? ...Good.
        #   <font color="#909090">(A small smile flashes quickly across $MaidName$'s face.)</font>
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000506$
        # - Our contract expires soon.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000507$
        # - You know that, right?
        if pick == 0:
            # $script:0831180509000508$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000509$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000510$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000511$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509000512$
        # - Is there anything else?
        if pick == 0:
            # $script:0831180509000513$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000514$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000515$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000516$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509000517$
        # - You look like you have something to tell me.
        if pick == 0:
            # $script:0831180509000518$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000519$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000520$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000521$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509000522$
        # - $OwnerName$, you're covered in dust.
        if pick == 0:
            # $script:0831180509000523$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000524$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000525$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000526$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509000528$
        # - You've already paid me for the month. Well, everyone forgets, now and then.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509000531$
        # - ... (She quietly stares at you.)
        if pick == 0:
            # $script:0831180509000532$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000533$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000534$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509000535$
        # - ... (She doesn't even look at you. Her eyes are closed.)
        if pick == 0:
            # $script:0831180509000536$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000537$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000538$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509000539$
        # - ... (She stares at the floor with a troubled look on her face.)
        if pick == 0:
            # $script:0831180509000540$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000541$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000542$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000544$
        # - $OwnerName$... My contract has expired. I... Oh, never mind.
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000545$
        # - <font color="#909090">(She refuses to meet your eyes as she mumbles.)</font>
        #   You're $MaidPassedDay$ behind on paying me.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000546$
        # - ...I don't have much to say.
        if pick == 0:
            # $script:0831180509000547$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000548$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000549$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509000550$
        # - ...I don't have much to say.
        if pick == 0:
            # $script:0831180509000551$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000552$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000553$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509000554$
        # - What do people usually say in a situation like this?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509000555$
        # - It's just that our contract has expired. You can renew it if you want.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509000556$
        # - <font color="#909090">($MaidName$ sighs, staring at the door. You can't tell what she's thinking.)</font>
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000557$
        # - That's not so tough.
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000558$
        # - Just let me know.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000559$
        # - You want to see my profile?
        #   <font color="#909090">(She smooths her apron, which is already perfectly smooth.)</font>
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000560$
        # - No big deal...
        #   <font color="#909090">(She avoids looking you in the eye.)</font>
        if pick == 0:
            # $script:0831180509000561$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000562$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000563$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000564$
        # - No big deal...
        #   <font color="#909090">(She avoids looking you in the eye.)</font>
        if pick == 0:
            # $script:0831180509000565$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000566$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000567$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000568$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509000569$
        # - As you wish.
        if pick == 0:
            # $script:0831180509000570$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509000571$
            # - (Ask about her interests.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509000572$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509000573$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509000574$
        # - Go ahead.
        if pick == 0:
            # $script:0831180509000575$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509000576$
            # - (Ask about her interests.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509000577$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509000578$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509000579$
        # - I'm listening.
        if pick == 0:
            # $script:0831180509000580$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509000581$
            # - (Ask about her interests.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509000582$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509000583$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509000584$
        # - Is there anything else?
        if pick == 0:
            # $script:0831180509000585$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000586$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000587$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509000588$
        # - You look like you have something to tell me.
        if pick == 0:
            # $script:0831180509000589$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000590$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000591$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509000592$
        # - $OwnerName$, you're covered in dust.
        if pick == 0:
            # $script:0831180509000593$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000594$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000595$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        # $script:0831180509000596$
        # - ($MaidName$ presents to you a small, lidded pot. She waits patiently for you to take it.)
        if pick == 0:
            # $script:0831180509000597$
            # - What's this?
            return 1003
        elif pick == 1:
            # $script:0831180509000598$
            # - (Take it.)
            # TODO: goto 1011, 1012
            return -1
        return -1

    def __1003(self, index: int, pick: int) -> int:
        # $script:0831180509000599$
        # - (She pushes it closer toward you, until it's practically in your hands.)
        if pick == 0:
            # $script:0831180509000600$
            # - I said, what is this?
            # TODO: goto 1001, 1002
            return -1
        elif pick == 1:
            # $script:0831180509000601$
            # - (Take it.)
            # TODO: goto 1011, 1012
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000602$
        # - Orange mushroom stew. I made it for you, but...
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000603$
        # - ...Just forget it.
        return -1

    def __1011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000604$
        # - Orange Mushroom stew. I made it for you.
        return -1

    def __1012(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000605$
        # - It's orange mushroom stew. Eat it before it gets cold. It's really yummy.
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000606$
            # - Um... I broke another plate. While cleaning up the mess, I kind of cut my finger.
            return 1100
        elif index == 1:
            # $script:0831180509000607$
            # - There was a lot of blood, but the cut wasn't very deep.
            if pick == 0:
                # $script:0831180509000608$
                # - (Grab her hand to check the cut.)
                # TODO: goto 1111, 1112
                return -1
            elif pick == 1:
                # $script:0831180509000609$
                # - Try to be more careful so you don't hurt yourself.
                # TODO: goto 1101, 1102
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000610$
        # - I will. At least you're not yelling at me for breaking another plate.
        return -1

    def __1102(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000611$
        # - Yes, you're right. I will.
        return -1

    def __1111(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000612$
        # - I'm okay! See? The bleeding has stopped!
        #   <font color="#909090">(She averts her eyes quickly. Is she... blushing?)</font>
        return -1

    def __1112(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000613$
        # - I'm grateful for your concern but... that's the wrong hand. It was just a cut. I'm okay.
        #   <font color="#909090">(A fleeting smile passes across her face.)</font>
        return -1

    def __1200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000614$
            # - My hands slipped while washing the dishes. I, um, broke another plate.
            return 1200
        elif index == 1:
            # $script:0831180509000615$
            # - It's probably not a surprise, but I thought you should know.
            if pick == 0:
                # $script:0831180509000616$
                # - How many plates have you broken since starting this job?
                # TODO: goto 1201, 1202
                return -1
            elif pick == 1:
                # $script:0831180509000617$
                # - It's okay. I'm just glad you're not hurt.
                # TODO: goto 1211, 1212
                return -1
            return -1
        return -1

    def __1201(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000618$
        # - Hm, I usually break one every couple days, so that's... Hmmm... Just a few.
        return -1

    def __1202(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000619$
        # - I'm not sure... I've lost count, to be honest.
        return -1

    def __1211(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000620$
        # - <font color="#909090">(Her cheeks turn red.)</font>
        #   Oh. Um. Thank you for your concern.
        return -1

    def __1212(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000621$
        # - Thanks, $OwnerName$.
        #   <font color="#909090">(She gives you a tiny smile.)</font>
        return -1

    def __1300(self, index: int, pick: int) -> int:
        # $script:0831180509000622$
        # - Every time I see you, you're always smiling. Did you know that, $OwnerName$?
        if pick == 0:
            # $script:0831180509000623$
            # - I like you even if you don't smile much.
            # TODO: goto 1301, 1302
            return -1
        elif pick == 1:
            # $script:0831180509000624$
            # - Someday, I'd love to see your smile, $MaidName$.
            # TODO: goto 1311, 1312
            return -1
        return -1

    def __1301(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000625$
        # - ...Do you?
        return -1

    def __1302(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000626$
        # - ...Heh. I see.
        return -1

    def __1311(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000627$
        # - Like... like this?
        #   <font color="#909090">(She uses her fingers to lift the side of her lips upwards.)</font>
        return -1

    def __1312(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000628$
        # - <font color="#909090">(Her cheeks turn red.)</font>
        #   I'll try... someday.
        return -1

    def __1400(self, index: int, pick: int) -> int:
        # $script:0831180509000629$
        # - No matter how much I mop, the floor is always a muddy mess. I don't mind when it's your tracks, but who are those strangers barging into the house?
        if pick == 0:
            # $script:0831180509000630$
            # - I believe in you, $MaidName$!
            # TODO: goto 1411, 1412
            return -1
        elif pick == 1:
            # $script:0831180509000631$
            # - Sorry for always making a mess.
            # TODO: goto 1401, 1402
            return -1
        return -1

    def __1401(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000632$
        # - ...It's okay.
        return -1

    def __1402(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000633$
        # - <font color="#909090">(She stares at you for a while, and then closes her eyes.)</font>
        return -1

    def __1411(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000634$
        # - ...Okay. You can count on me.
        return -1

    def __1412(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000635$
        # - ...Okay.
        #   <font color="#909090">(She nods her head, looking away.)</font>
        return -1

    def __1503(self, index: int, pick: int) -> int:
        # $script:0831180509000638$
        # - I grabbed some spicy rice cakes from a food stall on the way back from the supermarket.
        if pick == 0:
            # $script:0831180509000639$
            # - Were they tasty?
            # TODO: goto 1501, 1502
            return -1
        elif pick == 1:
            # $script:0831180509000640$
            # - Yum, I want to try them!
            # TODO: goto 1511, 1512
            return -1
        return -1

    def __1501(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000641$
        # - They were... all right, I guess.
        return -1

    def __1502(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000642$
        # - Hmm. Well, they were cheap.
        return -1

    def __1511(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000643$
        # - Oh, you do? Here, let me give you directions. Um... Shoot, I should've written it down...
        return -1

    def __1512(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000644$
        # - Oh. Well, I don't mind. When do you want to go? I wonder if they're still open?
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000645$
            # - Take this.
            #   <font color="#909090">(She holds out the broom in her hand, her eyes boring into you.)</font>
            return 2000
        elif index == 1:
            # $script:0831180509000646$
            # - We should clean together sometimes.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000647$
            # - Nothing much.
            return 2100
        elif index == 1:
            # $script:0831180509000648$
            # - Except that you came home so late...
            return 2100
        elif index == 2:
            # $script:0831180509000649$
            # - Nothing. Never mind.
            return 2100
        elif index == 3:
            # $script:0831180509000650$
            # - <font color="#909090">(She quickly glances away.)</font>
            #   Nothing. I didn't say anything.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __3000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000651$
            # - You keep asking me what I like. What do you like, $OwnerName$?
            return 3000
        elif index == 1:
            # $script:0831180509000652$
            # - Just a moment.
            #   <font color="#909090">(She rummages through her pocket.)</font>
            return 3000
        elif index == 2:
            # functionID=1 openTalkReward=True
            # $script:0831180509000653$
            # - <font color="#909090">(She pulls out a pen and a memo pad.)</font>
            #   Okay, go ahead. I'm listening.
            return -1
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000654$
            # - I've purchased some Dutch coffee beans. Would you like to try?
            return 3100
        elif index == 1:
            # $script:0831180509000655$
            # - <font color="#909090">(She looks down at her feet.)</font>
            #   I really love Dutch coffee. That aroma...
            return 3100
        elif index == 2:
            # functionID=1 openTalkReward=True
            # $script:0831180509000656$
            # - Huh? I didn't say anything. You probably imagined it.
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000657$
            # - What I like isn't important.
            return 4000
        elif index == 1:
            # $script:0831180509000658$
            # - We can't always do what we like. There many things we don't like, but we still have to do them.
            return 4000
        elif index == 2:
            # $script:0831180509000659$
            # - Ah, don't get me wrong. I'm not saying I don't like this job.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000660$
            # - I just... I don't know what I like.
            return 4100
        elif index == 1:
            # $script:0831180509000661$
            # - I know what I don't like, though: sweets.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000662$
            # - I worked as a maid for a noble family before I met you.
            return 5000
        elif index == 1:
            # $script:0831180509000663$
            # - I was... let go. I'll tell you why when I'm ready. But I can never ever tell you which family it was.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000664$
            # - My task at my last job was cooking. I wasn't very good, but having to do it every day helped me improve.
            return 5100
        elif index == 1:
            # $script:0831180509000665$
            # - That's why I came to work for you as a cook. Do you like the food I make?
            return 5100
        elif index == 2:
            # $script:0831180509000666$
            # - No, don't answer that. I don't think I want to know. Anyway, I feel most at home when I'm in the kitchen.
            return 5100
        elif index == 3:
            # $script:0831180509000667$
            # - Especially yours, since most of your dishes are now shatter-resistant and easily replaceable.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000668$
            # - I'm not sloppy. I just... have a knack for breaking things.
            return 6000
        elif index == 1:
            # $script:0831180509000669$
            # - I got yelled at a lot by my previous employer because of it. It didn't upset me. I deserved it.
            return 6000
        elif index == 2:
            # $script:0831180509000670$
            # - One day, while I was dusting as punishment for breaking too many dishes, I broke a flower vase.
            return 6000
        elif index == 3:
            # $script:0831180509000671$
            # - It happened to be a gift from the royal family. That's why they fired me. But it's okay... I have a much better boss now.
            return 6000
        elif index == 4:
            # $script:0831180509000672$
            # - $OwnerName$, if there are items you treasure and don't want broken, please keep them out of my reach.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000673$
            # - Can I tell you something?
            #   <font color="#909090">(She stares at her shoes.)</font>
            return 7000
        elif index == 1:
            # $script:0831180509000674$
            # - I'm not friendly or outgoing. A lot of people think I'm aloof.
            return 7000
        elif index == 2:
            # $script:0831180509000675$
            # - But I'm just not good at expressing myself. I have a hard time looking people in the eye while talking to them.
            return 7000
        elif index == 3:
            # $script:0831180509000676$
            # - <font color="#909090">(She peeks up, to see you listening intently.)</font>
            return 7000
        elif index == 4:
            # $script:0831180509000677$
            # - <font color="#909090">(Her face turns red and she immediately looks back down at the ground.)</font>
            #   So, I just wanted to say...
            return 7000
        elif index == 5:
            # $script:0831180509000678$
            # - Thank you, $OwnerName$.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000679$
            # - Ah!
            #   <font color="#909090">(She drops the plate she was holding when she notices you.)</font>
            return 100
        elif index == 1:
            # $script:0831180509000680$
            # - There goes another plate... Who are you?
            if pick == 0:
                # $script:0831180509000681$
                # - I could ask you the same thing.
                # TODO: goto 101, 102
                return -1
            elif pick == 1:
                # $script:0831180509000682$
                # - I'm here to visit the person who lives here.
                # TODO: goto 103, 104
                return -1
            elif pick == 2:
                # $script:0831180509000683$
                # - Sorry about the plate. Let me reimburse you for it.
                # TODO: goto 105, 106
                return -1
            return -1
        return -1
