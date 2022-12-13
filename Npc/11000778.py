""" 11000778: Mint """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509003230$
        # - Awww, you're here to see me.
        if pick == 0:
            # $script:0831180509003231$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003232$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003233$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509003234$
        # - I knew you couldn't stay away. Heehee!
        if pick == 0:
            # $script:0831180509003235$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003236$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003237$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509003238$
        # - Do you have something to say to little old me?
        if pick == 0:
            # $script:0831180509003239$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003240$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003241$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509003242$
        # - Awww, you're here to see me.
        if pick == 0:
            # $script:0831180509003243$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003244$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003245$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509003246$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509003247$
        # - I knew you couldn't stay away. Heehee!
        if pick == 0:
            # $script:0831180509003248$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003249$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003250$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509003251$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509003252$
        # - Do you have something to say to little old me?
        if pick == 0:
            # $script:0831180509003253$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003254$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003255$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509003256$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509003257$
        # - You're giving me a paycheck? Really?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509003258$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003259$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003260$
        # - Yippee! You kept your promise on time! I love people like you!!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003261$
        # - <font color="#909090">(She stares at you for a while, and then speaks in a sniffling voice.)</font>
        #   Th-thanks. I don't know why I'm getting so emotional. Maybe it's because I've earned this money.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003262$
        # - Yes, Yes! This is what I like! You can keep doing this, right? I'll be counting on you!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003263$
        # - I thought you were testing my patience. What's taking you so long? Don't let it happen again, all right?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003264$
        # - Now, this is important. Do you know what day it is today? Then you know what you've got to do, right?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003265$
        # - You'd better not forget it, or else!
        if pick == 0:
            # $script:0831180509003266$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003267$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003268$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509003269$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509003270$
        # - $OwnerName$, talking to you makes me feel good.
        if pick == 0:
            # $script:0831180509003271$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003272$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003273$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509003274$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509003275$
        # - Sometimes, I think we can get even closer.
        if pick == 0:
            # $script:0831180509003276$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003277$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003278$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509003279$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509003280$
        # - Hmm? What could you possibly have to ask little old me?
        if pick == 0:
            # $script:0831180509003281$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003282$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003283$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509003284$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509003286$
        # - Oh, did you forget? Or were you too busy stealing glances at me? You already paid me for this month!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509003289$
        # - I like that I don't have to work, but I don't like that you haven't paid me.
        if pick == 0:
            # $script:0831180509003290$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003291$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003292$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509003293$
        # - Are you really going to keep neglecting me?
        if pick == 0:
            # $script:0831180509003294$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003295$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003296$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509003297$
        # - I'm so disappointed. So, so disappointed in you.
        if pick == 0:
            # $script:0831180509003298$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003299$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003300$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003302$
        # - I'd like to think you won't treat me like this forever. I'd like to have faith in you.
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003303$
        # - You're still curious about me, aren't you?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003304$
        # - I wish I could turn back time...
        if pick == 0:
            # $script:0831180509003305$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003306$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003307$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509003308$
        # - I miss the good old days... When you cared...
        if pick == 0:
            # $script:0831180509003309$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003310$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003311$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509003312$
        # - Rules are merciless things. I'm sorry, but I can't do any work for you right now.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509003313$
        # - I believe in you! You can make things back the way they were!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509003314$
        # - I'm so tired of worrying about money, worrying about whether you care. But I have no choice but to wait for you to sort things out.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003315$
        # - What kind of potion do you need? Just say the word!
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003316$
        # - Let me know if I can help!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003317$
        # - What do you want to know about me? I'll tell you anything!
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003318$
        # - Heehee, happy?
        if pick == 0:
            # $script:0831180509003319$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003320$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003321$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003322$
        # - Heehee, happy?
        if pick == 0:
            # $script:0831180509003323$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003324$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003325$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509003326$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509003327$
        # - What do you want to talk about? I love interesting stories.
        if pick == 0:
            # $script:0831180509003328$
            # - You look happy, as always.
            # TODO: goto 1000, 1100, 1200, 1300, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509003329$
            # - Play with me.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509003330$
            # - Tell me about the Bunnies.
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509003331$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509003332$
        # - Is there something you want to ask me?
        if pick == 0:
            # $script:0831180509003333$
            # - You look happy, as always.
            # TODO: goto 1000, 1100, 1200, 1300, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509003334$
            # - Play with me.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509003335$
            # - Tell me about the Bunnies.
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509003336$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509003337$
        # - Sure, why not? I love chatting!
        if pick == 0:
            # $script:0831180509003338$
            # - You look happy, as always.
            # TODO: goto 1000, 1100, 1200, 1300, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509003339$
            # - Play with me.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509003340$
            # - Tell me about the Bunnies.
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509003341$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509003342$
        # - $OwnerName$, talking to you makes me feel good.
        if pick == 0:
            # $script:0831180509003343$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003344$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003345$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509003346$
        # - Sometimes, I think we can get even closer.
        if pick == 0:
            # $script:0831180509003347$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003348$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003349$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509003350$
        # - Hmm? What could you possibly have to ask little old me?
        if pick == 0:
            # $script:0831180509003351$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003352$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003353$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003354$
            # - That's because I am happy, silly. I'm only going to live once, might as well live happily. Don't you agree, $OwnerName$?
            return 1000
        elif index == 1:
            # $script:0831180509003355$
            # - Besides, something really great happened to me today. You wanna know? Hehe, what's it worth to you?
            return 1000
        elif index == 2:
            # $script:0831180509003356$
            # - Hehe, so, what happened today was... Hehehe, let's see, um... None of your business! Teehee!
            if pick == 0:
                # $script:0831180509003357$
                # - I don't care anyway.
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509003358$
                # - C'mon! Stop teasing me or I'll... I'll cut your pay!
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003359$
        # - Aww, $OwnerName$, are you upset? I was just messing with you. Hmph, now I'm upset, too.
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003360$
        # - Heehee, so what happened was... Wait. Did you just say you don't care?! What?! Now you've made me mad!
        return -1

    def __1011(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003361$
            # - Aw, $OwnerName$, you care that much? Hehe, don't cut my pay. I'll tell you!
            return 1011
        elif index == 1:
            # $script:0831180509003362$
            # - I was strolling through $map:02000001$ when I bumped into $npcName:11000764[gender:1]$. She was leaving the macaroon shop. It's insane how she eats so many sweets yet stays so tiny. Anyway...
            return 1011
        elif index == 2:
            # $script:0831180509003363$
            # - A guy approached us, gushing about he's a huge fan of the Bunnies, but then... he only asked me for an autograph! That proves it, right? I'm more popular than $npcName:11000764[gender:1]$! Teehee!
            return 1011
        elif index == 3:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003364$
            # - You should've seen the look on her face. It was priceless! Now you know what I'm so happy today, heehee.
            return -1
        return -1

    def __1012(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003365$
            # - Who's teasing who, huh? Cut my pay! Teehee! Yeah, right! You're so funny, $OwnerName$!
            return 1012
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003366$
            # - I had no idea you had such a playful side, $OwnerName$. I like it!!
            return -1
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003367$
            # - Actually, something incredible happened... But it's a secret. Don't tell a soul! Promise?
            return 1100
        elif index == 1:
            # $script:0831180509003368$
            # - <font color="#909090">(She leans in close and whispers.)</font>
            #   You know how Goldus started selling lottery tickets? The grand prize is a billion mesos! Well, I bought one and... I won!!
            return 1100
        elif index == 2:
            # $script:0831180509003369$
            # - Can you believe it?! I won fifth place! Isn't that incredible??
            if pick == 0:
                # $script:0831180509003370$
                # - What's the prize for fifth place?
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509003371$
                # - Congratulations!
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003372$
            # - I don't know! I mean, it's got to be a lot, right? Isn't it exciting? I've never gotten fifth in anything in my life, not even when I was in school!
            return 1101
        elif index == 1:
            # $script:0831180509003373$
            # - Anyway, the prize amount is, umm... it says here that it's 500 mesos. But that's how much the ticket cost...
            return 1101
        elif index == 2:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003374$
            # - Does that mean anyone can win fifth place? Ah, I knew it was too good to be true. But the last few days, I've been walking on a cloud, so I guess that counts for something.
            return -1
        return -1

    def __1102(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003375$
            # - Oh, I hadn't even checked. Do you want me to share some of my riches with you, heehee? Well, it says here the prize is...
            return 1102
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003376$
            # - Huh? 500 mesos? That's not even a fraction of what I hoped! Ugh... And here I was, planning how I would turn in my resignation... Huh? What? Forget I said anything!
            return -1
        return -1

    def __1111(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003377$
        # - Thank you, heehee! I'm so excited! There are so many things I want to buy. Oh, but what if I go overboard and it won't all fit in the house?
        return -1

    def __1112(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003378$
            # - Aren't you worried, $OwnerName$? Once I'm rich, I won't need a job, which means I can quit and leave you all by yourself!
            return 1112
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003379$
            # - But don't worry, I'm not going anywhere. I'll stay with you forever and always, $OwnerName$. Heehee.
            return -1
        return -1

    def __1200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003380$
            # - Ahhh, I feel great today! On a day like this, I can get all my dance moves perfect!
            return 1200
        elif index == 1:
            # $script:0831180509003381$
            # - I'm going to take advantage of that to put in some extra dance practice today. You wanna watch?
            if pick == 0:
                # $script:0831180509003382$
                # - Absolutely.
                # TODO: goto 1211, 1212
                return -1
            elif pick == 1:
                # $script:0831180509003383$
                # - Shouldn't you be dusting?
                # TODO: goto 1201, 1202
                return -1
            return -1
        return -1

    def __1201(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003384$
            # - Dusting? You have a chance to see my amazing dance skills and you're talking about dusting?
            return 1201
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003385$
            # - Wow! I don't think I've ever been so insulted in my life!
            return -1
        return -1

    def __1202(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003386$
            # - Mmm, this is a problem. I have to practice my moves, but you want me to dust...
            return 1202
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003387$
            # - I guess I have no choice. I have to do what you say, so I'll give up dance practice for today...
            return -1
        return -1

    def __1211(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003388$
            # - Aw, shucks. Do you mean it? Actually, people love watching me dance. They say it makes them happy.
            return 1211
        elif index == 1:
            # $script:0831180509003389$
            # - $OwnerName$, I haven't told this to anyone, but actually... I have a fan club! Surprised?
            return 1211
        elif index == 2:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003390$
            # - Actually, I changed my mind. I can't dance in front of you. I haven't practiced enough! But I promise you'll be the first to see when I can put on a perfect show!
            return -1
        return -1

    def __1212(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003391$
            # - $OwnerName$, now that you say you want to watch me dance... I don't want to! Does that make me a flirt? Heehee.
            return 1212
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003392$
            # - But thank you for saying that. It really made my day!
            return -1
        return -1

    def __1300(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003393$
            # - Today is amazing!! I can't believe it! I've hit the jackpot, $OwnerName$!
            return 1300
        elif index == 1:
            # $script:0831180509003394$
            # - I don't know if you remember, but I told you a while back that I'm collecting the stickers found inside Maple Bread and you laughed at me. Well...
            return 1300
        elif index == 2:
            # $script:0831180509003395$
            # - I've been trying and trying to get the $npcName:21000302$ sticker to complete my collection! I ate sooooo many bags of bread searching for it, and today I found it!!
            return 1300
        elif index == 3:
            # $script:0831180509003396$
            # - I'm so happy! Finally, my collection is complete!
            if pick == 0:
                # $script:0831180509003397$
                # - That's quite an achievement!
                # TODO: goto 1311, 1312
                return -1
            elif pick == 1:
                # $script:0831180509003398$
                # - Oh, that? I have like three duplicates of that one.
                # TODO: goto 1301, 1302
                return -1
            return -1
        return -1

    def __1301(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003399$
            # - What?!? $OwnerName$!!! Do you know how much bread I ate... how many pounds I gained... to try to find that sticker?! And you had it all along and didn't tell me?!
            return 1301
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003400$
            # - I hate you so much right now, $OwnerName$. You've totally ruined my mood.
            return -1
        return -1

    def __1302(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003401$
            # - What?! But you made fun of me when I told you I was collecting the stickers! And you were secretly collecting them, too?
            return 1302
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003402$
            # - What a hypocrite! I can't stand that kind of behavior!
            return -1
        return -1

    def __1311(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003403$
        # - I know! I can do anything when I put my mind to it. Heehee! What should I collect next?
        return -1

    def __1312(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003404$
            # - That's right! You should feel lucky to have a servant as great as me in your life, hee hee!
            return 1312
        elif index == 1:
            # $script:0831180509003405$
            # - Now, where should I hang my completed collection? Hmm, maybe here. I never liked that painting anyway, never mind that it cost a million mesos...
            return 1312
        elif index == 2:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003406$
            # - Or maybe here, so it's the first thing you see when you enter the front door. I'd just have to throw out that vase. Hmm...
            return -1
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003407$
            # - Of course I'm always happy! $OwnerName$, sing with me! It'll make you happy, too.
            return 2000
        elif index == 1:
            # $script:0831180509003408$
            # - You are my Maple leaf...
            #   My only Maple leaf!
            #   You make me happy...
            #   When skies are gray!
            return 2000
        elif index == 2:
            # $script:0831180509003409$
            # - <font color="#909090">(Wow, the girl is tone deaf! You can barely recognize the song, the way she sings it.)</font>
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003410$
            # - Whenever I feel even a tiny bit gloomy, I play rock paper scissors with myself. My right hand versus my left hand.
            return 2100
        elif index == 1:
            # $script:0831180509003411$
            # - That way, no matter what happens, I win! And then I feel happy. Perfectly simple, right?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __3000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003412$
        # - Yes! How did you know I didn't feel like working today, $OwnerName$? You know me so well!
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003413$
            # - I love how much you love playing with me, $OwnerName$! I love playing with you, too!
            return 3100
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003414$
            # - I'm so lucky to have such a great boss. It makes every day the best day, heehee!
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        # $script:0831180509003415$
        # - Nooooo! I wish I could, but I'm swamped! Drats, I could really use a break, but I can't...
        # TODO: gotoConditionTalkID 30, 31, 32, 9011
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003416$
            # - Ahh, I'm so busy, but maybe I can take a small break. How about a game of word chain?
            return 4100
        elif index == 1:
            # $script:0831180509003417$
            # - I'll go first... "Fix"! Can you think of a word that starts with "X"? Oops, too slow! So fun! Okay, break's over!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003418$
            # - The Bunnies are the most famous troupe in all of Maple World!
            return 5000
        elif index == 1:
            # $script:0831180509003419$
            # - We travel all around, and thousands of people come to our shows. I feel so lucky to be a part of them!
            return 5000
        elif index == 2:
            # $script:0831180509003420$
            # - I knew I wanted to be a Bunny since I was little. They just bring so much joy everywhere they go, and I wanted to be a part of that! It wasn't easy, but I found a way to make my dream come true, heehee.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003421$
            # - It's not easy to join the Bunnies. We're really exclusive.
            return 5100
        elif index == 1:
            # $script:0831180509003422$
            # - Hundreds of girls line up at our management offices each day, begging for the chance to participate in our trainee program.
            return 5100
        elif index == 2:
            # $script:0831180509003423$
            # - If they're accepted, they have to train hard to prove themselves, and if they pass all the tests, they finally become official Bunnies. Ah, I remember those days. I was the first in my program!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003424$
            # - Remember how I said I'd always wanted to be a Bunny? Well, I had to jump through a lot of hurdles to get to where I am today.
            return 6000
        elif index == 1:
            # $script:0831180509003425$
            # - You see, when I was little, I was sick a lot. I could barely stay in school because I was so fatigued, and I was severely underweight.
            return 6000
        elif index == 2:
            # $script:0831180509003426$
            # - The other kids used to make fun of me. They called me "grasshopper ghost" because my arms were so gangly and I was so pale. They would run away when they saw me, shrieking about how I was contagious.
            return 6000
        elif index == 3:
            # $script:0831180509003427$
            # - I was nowhere near strong enough to become a Bunny. It takes a lot of stamina to perform those dances, you know. But I never gave up. I talked to a trainer to learn how to build muscle strength and to a nutritionist to learn how to eat to make my body strong. I practiced every single day.
            return 6000
        elif index == 4:
            # $script:0831180509003428$
            # - I will never have a "perfect" body, but I have a strong body, and I've worked hard to get here. I've learned how to take of myself.
            return 6000
        elif index == 5:
            # $script:0831180509003429$
            # - Whenever I see kids making fun of each other for being too skinny or fat or tall or short, I tell them that nobody has the perfect body and that anyone can succeed if they set their mind to it. They listen to me, because I'm a Bunny.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509003430$
            # - There's something about my past that I haven't shared with you yet. Something that happened a long time ago...
            return 7000
        elif index == 1:
            # $script:0831180509003431$
            # - Remember how I told you I was sickly when I was younger? I found out that it wasn't natural. I had been cursed by a witch.
            return 7000
        elif index == 2:
            # $script:0831180509003432$
            # - To this day, I still don't know why. I almost died from that curse!
            return 7000
        elif index == 3:
            # $script:0831180509003433$
            # - But curse or no curse, I worked hard and overcame it! I'm so proud of myself for that! I heard later that maybe some hero had lifted the curse, but...
            return 7000
        elif index == 4:
            # $script:0831180509003434$
            # - Hero or no hero, I would've broke the curse myself eventually out of sheer determination. Still, I wouldn't mind meeting that hero someday.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509003435$
        # - Hello. Hi! Who are you? What brings you here?
        if pick == 0:
            # $script:0831180509003436$
            # - I'm here to see your master.
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509003437$
            # - I came to check out the house.
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509003438$
            # - Who are you?
            # TODO: goto 105, 106
            return -1
        return -1

