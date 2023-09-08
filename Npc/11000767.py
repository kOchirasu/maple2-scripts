""" 11000767: Terry """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])


    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509001136$
        # - How was your day today?
        if pick == 0:
            # $script:0831180509001137$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001138$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001139$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509001140$
        # - You're home early today.
        if pick == 0:
            # $script:0831180509001141$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001142$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001143$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509001144$
        # - Hey, you're home.
        if pick == 0:
            # $script:0831180509001145$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001146$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001147$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509001148$
        # - How was your day today?
        if pick == 0:
            # $script:0831180509001149$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001150$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001151$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001152$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509001153$
        # - You're home early today.
        if pick == 0:
            # $script:0831180509001154$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001155$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001156$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001157$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509001158$
        # - Hey, you're home.
        if pick == 0:
            # $script:0831180509001159$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001160$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001161$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001162$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509001163$
        # - Oh, you're giving me my paycheck.
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509001164$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001165$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001166$
        # - Hah hah, thanks! I'm happy to work for you for this month!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001167$
        # - Has it been so long already? Thanks for asking me before I had to ask. I hate asking for money.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001168$
        # - Ah! You don't know how long I've been waiting for this! Finally, I've got some money to spend. Hah hah!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001169$
        # - Whew, I was debating whether I should cancel my savings account because I'd have nothing to put in it. Thank goodness I won't have to!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001170$
        # - $OwnerName$, I was looking at the calender today and saw that our contract is expiring soon. Just wanted to let you know. No pressure or anything!
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001171$
        # - Then again, maybe I'm worring for nothing. Hah hah.
        if pick == 0:
            # $script:0831180509001172$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001173$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001174$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001175$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509001176$
        # - Is there anything I can do for you? 
        if pick == 0:
            # $script:0831180509001177$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001178$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001179$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001180$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509001181$
        # - I want to do something fun. Any suggestions?
        if pick == 0:
            # $script:0831180509001182$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001183$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001184$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001185$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509001186$
        # - I've got too much energy. Maybe I should work out.
        if pick == 0:
            # $script:0831180509001187$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001188$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001189$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001190$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509001192$
        # - A paycheck, again? You already paid me for this month. Hm, maybe I should take it as a bonus... Hah hah hah!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509001195$
        # - I wonder what the fines are for canceling a bond before it matures... 
        if pick == 0:
            # $script:0831180509001196$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001197$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001198$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509001199$
        # - Anything happen today, like winning a lottery or inheriting a massive fortune? 
        if pick == 0:
            # $script:0831180509001200$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001201$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001202$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509001203$
        # - Huh? What?
        if pick == 0:
            # $script:0831180509001204$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001205$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001206$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001209$
        # - The paycheck I get from $map:02000068$ barely covers my living expenses. 
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001210$
        # - $OwnerName$! How are you doing?
        if pick == 0:
            # $script:0831180509001211$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001212$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001213$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509001214$
        # - Do you have something more to say? 
        if pick == 0:
            # $script:0831180509001215$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001216$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001217$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509001218$
        # - I don't know what to say. I opened a CD account with Goldus Bank to save money for a ship, but at this rate, I might have to cancel it before it matures. 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509001219$
        # - I thought being a butler was a stable job. I'm starting to think I was wrong. Guess nothing in life is certain... 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509001220$
        # - Do you even have enough money to feed yourself? I also get money from $map:02000068$, so I'm not completely broke. At least I can feed myself. I'm worried that you can't.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001221$
        # - Oh, a drink? Sure, what kind were ya thinking?
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001222$
        # - Let me know what you need!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001223$
        # - About me? Sure, what do you want to know?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001224$
        # - Ask me anything.
        if pick == 0:
            # $script:0831180509001225$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001226$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001227$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001228$
        # - Ask me anything.
        if pick == 0:
            # $script:0831180509001229$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001230$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001231$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001232$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509001233$
        # - What do you want me to tell you? 
        if pick == 0:
            # $script:0831180509001234$
            # - Did anything interesting happen today? 
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509001235$
            # - Let's talk about adventures!
            # TODO: goto 3000, 3100, 3200, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509001236$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509001237$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509001238$
        # - Sure, I can tell you whatever you wanna know.
        if pick == 0:
            # $script:0831180509001239$
            # - Did anything interesting happen today? 
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509001240$
            # - Let's talk about adventures!
            # TODO: goto 3000, 3100, 3200, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509001241$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509001242$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509001243$
        # - $OwnerName$, you don't look well. Are you sure you don't need to rest?
        if pick == 0:
            # $script:0831180509001244$
            # - Did anything interesting happen today? 
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509001245$
            # - Let's talk about adventures!
            # TODO: goto 3000, 3100, 3200, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509001246$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509001247$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509001248$
        # - Is there anything I can do for you? 
        if pick == 0:
            # $script:0831180509001249$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001250$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001251$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509001252$
        # - I want to do something fun. Any suggestions?
        if pick == 0:
            # $script:0831180509001253$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001254$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001255$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509001256$
        # - I've got too much energy. Maybe I should work out.
        if pick == 0:
            # $script:0831180509001257$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001258$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001259$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001260$
            # - Did you eat? Here, eat this. Wait. Why is your face so gaunt? 
            return 1000
        elif index == 1:
            # $script:0831180509001261$
            # - Have you lost weight? This is why you shouldn't skip meals! Here, eat this.
            if pick == 0:
                # $script:0831180509001262$
                # - You cooked this?
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509001263$
                # - It's delicious!
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001269$
            # - You hungry, $OwnerName$? How about a snack?
            return 1100
        elif index == 1:
            # $script:0831180509001270$
            # - Ah, I cooked this. I had some time to kill since today was my day off. I don't know if it tastes good.
            if pick == 0:
                # $script:0831180509001271$
                # - It... doesn't taste good.
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509001272$
                # - It tastes okay.
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __1200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001278$
            # - I don't know if I'm exhausted or have a cold. Either way, I really don't feel good. Take this. I picked it up on my way here from $map:02000068$. I brought you one because I don't want you to catch what I have.
            return 1200
        elif index == 1:
            # $script:0831180509001279$
            # - It's good for your health.  If you don't want to take it now, you can take it later.
            if pick == 0:
                # $script:0831180509001280$
                # - How are you feeling?
                # TODO: goto 1211, 1212
                return -1
            elif pick == 1:
                # $script:0831180509001281$
                # - Thank you.
                # TODO: goto 1201, 1202
                return -1
            return -1
        return -1

    def __1300(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001286$
            # - I picked up some food on my way here from $map:02000069$. I was so hungry when I got off my other job, I just had to eat, so I ate mine there.
            return 1300
        elif index == 1:
            # $script:0831180509001287$
            # - Mrs. $npc:11000453[gender:1]$ is the best cook I know. The dish I tried was so good, I had to bring you some, too! 
            if pick == 0:
                # $script:0831180509001288$
                # - Thanks.
                # TODO: goto 1311, 1312
                return -1
            elif pick == 1:
                # $script:0831180509001289$
                # - I'm not really hungry.
                # TODO: goto 1301, 1302
                return -1
            return -1
        return -1

    def __1400(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001294$
            # - Hah hah! Do you know what this is? It's a prize I won in an event! It pays off to be strong, ya know!
            return 1400
        elif index == 1:
            # $script:0831180509001295$
            # - I've participated in so many events that I know exactly what to do to win them.
            if pick == 0:
                # $script:0831180509001296$
                # - Can I have your prize?
                # TODO: goto 1401, 1402
                return -1
            elif pick == 1:
                # $script:0831180509001297$
                # - What kind of event did you win?
                # TODO: goto 1411, 1412
                return -1
            return -1
        return -1

    def __1500(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001303$
            # - Our upstairs neighbor moved out today. He's been a pretty good neighbor, so I helped him move his furniture.
            return 1500
        elif index == 1:
            # $script:0831180509001304$
            # - He left a lot of things behind. Some of it looked pretty good, so I brought this with me. What do you think? 
            if pick == 0:
                # $script:0831180509001305$
                # - Why did you bring home trash?
                # TODO: goto 1501, 1502
                return -1
            elif pick == 1:
                # $script:0831180509001306$
                # - Nice find! Good work!
                # TODO: goto 1511, 1512
                return -1
            return -1
        return -1

    def __1600(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001311$
            # - Hey, I picked up this $item:90000001$ on my way here from $map:02000068$. You can have it. I know it's not much.
            return 1600
        elif index == 1:
            # $script:0831180509001312$
            # - I live here, too, you know. And I don't pay rent, so...
            if pick == 0:
                # $script:0831180509001313$
                # - Thanks.
                # TODO: goto 1611, 1612
                return -1
            elif pick == 1:
                # $script:0831180509001314$
                # - You have any more?
                # TODO: goto 1601, 1602
                return -1
            return -1
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001319$
            # - Welcome. Nothing much happened today. How are you? If you're tired, go get some rest. I'll take care of the housework.
            return 2000
        elif index == 1:
            # $script:0831180509001320$
            # - Oh, I found some torn clothes while folding laundry. What did you do that shredded your clothes like that? Are you sure you're not bleeding somewhere?
            return 2000
        elif index == 2:
            # $script:0831180509001321$
            # - If you're hurt, don't try to hide it. Just go to the hospital. You shouldn't worry about money when you're sick. All right?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001322$
            # - Well, I cleaned the house and worked out as usual. I feel off if I don't work out every day. 
            return 2100
        elif index == 1:
            # $script:0831180509001323$
            # - Being the captain of a ship is not easy. I have to build up my strength to sail out to sea. Things will be especially tough when the waves are high.
            return 2100
        elif index == 2:
            # $script:0831180509001324$
            # - Speaking of which, $OwnerName$, how'd you like to work out with me? Health is the most important thing, after all!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001325$
            # - You want something to drink? Sure, I was just working out.
            return 2200
        elif index == 1:
            # $script:0831180509001326$
            # - Huh? Do I smell? Sorry. I'll take a shower after you leave.
            return 2200
        elif index == 2:
            # $script:0831180509001327$
            # - We're friends, but... I don't know, I don't want to make you uncomfortable.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001339$
            # - Sigh... I can't think about adventures right now. $OwnerName$, today...
            return 4000
        elif index == 1:
            # $script:0831180509001340$
            # - I had just gotten out of the shower and was wearing nothing except a towel around my waist, when someone opened the door and barged in. 
            return 4000
        elif index == 2:
            # $script:0831180509001341$
            # - At first, I thought it was you, but it was actually the lady from next door. Something is not right with her. I'm grateful for the food she give me sometimes, but... 
            return 4000
        elif index == 3:
            # $script:0831180509001342$
            # - The way she looks at me makes my hair stand on end. $OwnerName$, can we move?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001343$
            # - I expected this, but working two jobs is not easy. I like that I have enough money to save to buy a ship, but I'm so busy that I don't have time to actually plan the adventure. There's no end to the housework.
            return 4100
        elif index == 1:
            # $script:0831180509001344$
            # - I washed the comforters today. Not with a washing machine, though. I just throw them into the bathtub and press them by foot.
            return 4100
        elif index == 2:
            # $script:0831180509001345$
            # - It's a ton of fun, and also good exercise. $OwnerName$, you should try it with me next time.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001346$
            # - I was reluctant about being a male housekeeper, but it turned out I'm really good at it. I mean it.
            return 5000
        elif index == 1:
            # $script:0831180509001347$
            # - When you mop, you have to put a some real effort into it to get the floor sparkling clean, or else you're just spreading water around. Same with ironing. You have to press the iron hard to smooth all the wrinkles at once.
            return 5000
        elif index == 2:
            # $script:0831180509001348$
            # - Cooking also requires the constant kneading of flour, and kneading is tough, even for strong men. That's why tough men are better at housework.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001349$
            # - One day, I'm going to buy a ship and sail out to sea. Of course, I'll have a crew, too!
            return 5100
        elif index == 1:
            # $script:0831180509001350$
            # - I'll be Captain $MaidName$. Doesn't that roll off the tongue nicely? Hah hah hah! I can't wait to go on an adventure like $npcName:11000444[gender:0]$!
            return 5100
        elif index == 2:
            # $script:0831180509001351$
            # - Did you know there are many small islands around Victoria Island? Some are uninhabited, and who knows? Maybe they have treasures hidden on them!
            return 5100
        elif index == 3:
            # $script:0831180509001352$
            # - If I find enough treasure, I can buy a bigger ship and have a bigger crew. Then I'll be able to sail farther out to the sea and experience all the wonderful things I read in "Colombo's Travels."
            return 5100
        elif index == 4:
            # $script:0831180509001353$
            # - Merfolk are real, did you know that? Ooh, so are ghost ships hidden deep amidst heavy fog! And squid as tall as buildings! Those are real, too!
            return 5100
        elif index == 5:
            # $script:0831180509001354$
            # - When I'm out on my adventures, I might discover a new continent. Then I'd have to name it. Oh, hmm, I'd better start thinking about names... 
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001355$
            # - I don't have a hometown. It sounds strange, but I really don't, because I was born at sea.
            return 6000
        elif index == 1:
            # $script:0831180509001356$
            # - My parents were international traders. They sailed to many different countries. I was born while they were sailing. That's why I don't have a hometown. 
            return 6000
        elif index == 2:
            # $script:0831180509001357$
            # - So I have no place to return to. I didn't feel like I belonged anywhere, until... 
            return 6000
        elif index == 3:
            # $script:0831180509001358$
            # - Until I came to live with you in this house. It's kind of nice having a place to call home. Just saying.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001359$
            # - Since birth, I'd traveled the world with my parents. A few years ago, I decided to strike out on my own. Why? Because I was an adult!
            return 7000
        elif index == 1:
            # $script:0831180509001360$
            # - I said goodbye and left them at the Victoria Island dock. I was itching to go on an adventure of my own, but I didn't have enough money to buy a ship. 
            return 7000
        elif index == 2:
            # $script:0831180509001361$
            # - Then I got to know about Helping Hands, so I took a training course. I took the guide course, and since I have experience in sailing, I was able to get a job with $map:02000068$ in $map:02000062$.
            return 7000
        elif index == 3:
            # $script:0831180509001362$
            # - Lately, the sea has been so rough. Not many ships are coming to $map:02000062$ and that slowed down my job considerably. That doesn't mean I get paid less, but still.
            return 7000
        elif index == 4:
            # $script:0831180509001363$
            # - Since I had more time than before, I decided to take on another job. I needed money. Didn't I tell you? Ships are not cheap. 
            return 7000
        elif index == 5:
            # $script:0831180509001364$
            # - I thought housekeeping was something I could do. Although I didn't take the housekeeping course at Helping Hands, I was a graduate, so the company helped me get a job. The result? I couldn't ask for more!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509001365$
        # - Mm? Who are you? Are you here to see $OwnerName$?
        if pick == 0:
            # $script:0831180509001366$
            # - Yep!
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509001367$
            # - Nope!
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509001368$
            # - Who are you?
            # TODO: goto 105, 106
            return -1
        return -1

    def exit_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        return

    def enter_state(self, functionId: int):
        if functionId == 1:
            # TODO: functionID 1
            return
        return
