""" 11000788: Harry """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509004562$
        # - Mm? You itching for some action too?
        if pick == 0:
            # $script:0831180509004563$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004564$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004565$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509004566$
        # - Huh? Ah, $OwnerName$. It's you. I didn't know who it was for a second.
        if pick == 0:
            # $script:0831180509004567$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004568$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004569$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509004570$
        # - I want to do something fun.
        if pick == 0:
            # $script:0831180509004571$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004572$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004573$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509004574$
        # - Mm? You itching for some action too?
        if pick == 0:
            # $script:0831180509004575$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004576$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004577$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004578$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509004579$
        # - Huh? Ah, $OwnerName$. It's you. I didn't know who it was for a second.
        if pick == 0:
            # $script:0831180509004580$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004581$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004582$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004583$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509004584$
        # - I want to do something fun.
        if pick == 0:
            # $script:0831180509004585$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004586$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004587$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004588$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509004589$
        # - You want to pay me?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509004590$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004591$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004592$
        # - Oooh, you pay me ahead of schedule every month. Thanks! Adventurers are so capable. I want to become as great an adventurer as you, $OwnerName$!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004593$
        # - Hurrah, I got my paycheck!  Thanks for hiring me for this month again. Hah hah!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004594$
        # - Huh? I thought you didn't have enough money to pay me. Where did you get this? Ah, I guess this goes to show that I have to become a great adventurer like you!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004595$
        # - Oh yeah, I forgot that adventurers don't have a stable income. They can be completely broke one moment and filthy rich the next. I wasn't thinking clearly when I decided to give up my dream of becoming one. Heh!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004596$
        # - $OwnerName$, our employment contract expires soon. You know that, right? What? You didn't?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004597$
        # - Well, adventurers have a lot on their mind. I understand. 
        if pick == 0:
            # $script:0831180509004598$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004599$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004600$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004601$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509004602$
        # - Do you have business with me?
        if pick == 0:
            # $script:0831180509004603$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004604$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004605$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004606$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509004607$
        # - Wow, what nice weather!
        if pick == 0:
            # $script:0831180509004608$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004609$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004610$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004611$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509004612$
        # - What? What do you need?
        if pick == 0:
            # $script:0831180509004613$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004614$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004615$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004616$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509004618$
        # - ...Huh? But you paid me for this month already. Hah hah, you shouldn't be so forgetful. 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509004621$
        # - Ahh... Should I give up my dream? 
        if pick == 0:
            # $script:0831180509004622$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004623$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004624$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509004625$
        # - I've been thinking a lot lately... 
        if pick == 0:
            # $script:0831180509004626$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004627$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004628$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509004629$
        # - Should I get a different job?
        if pick == 0:
            # $script:0831180509004630$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004631$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004632$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004634$
        # - Oh, no! My contract expired! What am I doing? I don't have time for chitchat right now! 
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004635$
        # - It's been $MaidPassedDay$ already.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004636$
        # - I can't sleep no matter how hard I try. Maybe I should read a book...
        if pick == 0:
            # $script:0831180509004637$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004638$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004639$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509004640$
        # - I can't sleep no matter how hard I try. Maybe I should read a book...
        if pick == 0:
            # $script:0831180509004641$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004642$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004643$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509004644$
        # - This is really important to me. You know I've been saving to go on an adventure, right? Now that I have income, how can I carry out my plan?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509004645$
        # - If I give up my dream of becoming an adventurer, will I still be me? What do you think?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509004646$
        # - Zzz... Zzz... Zzz... Zzz... Mm...?
        #   <font color="#909090">(He must have fallen asleep while reading.)</font> 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004647$
        # - I have to know how to cook to stay alive at sea.
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004648$
        # - I can cook anything you want.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004649$
        # - Sure, ask away.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004650$
        # - What? What do you need?
        if pick == 0:
            # $script:0831180509004651$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004652$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004653$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004654$
        # - What? What do you need?
        if pick == 0:
            # $script:0831180509004655$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004656$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004657$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004658$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509004659$
        # - I want to go on an adventure!
        if pick == 0:
            # $script:0831180509004660$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509004661$
            # - Tell me a story about an adventure!
            # TODO: goto 3000, 3100, 3200, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509004662$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509004663$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509004664$
        # - Back when I was...
        if pick == 0:
            # $script:0831180509004665$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509004666$
            # - Tell me a story about an adventure!
            # TODO: goto 3000, 3100, 3200, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509004667$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509004668$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509004669$
        # - I can regale you with adventure stories all night long.
        if pick == 0:
            # $script:0831180509004670$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509004671$
            # - Tell me a story about an adventure!
            # TODO: goto 3000, 3100, 3200, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509004672$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509004673$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509004674$
        # - Do you have business with me?
        if pick == 0:
            # $script:0831180509004675$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004676$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004677$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509004678$
        # - Wow, what nice weather!
        if pick == 0:
            # $script:0831180509004679$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004680$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004681$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509004682$
        # - What? What do you need?
        if pick == 0:
            # $script:0831180509004683$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004684$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004685$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004686$
            # - Since you asked, I did see some guy clad head to toe in armor deep within the Ant Tunnel. He was all solemn and asked how I'd gotten that far. I had to stop myself from laughing. He was so pretentious!
            return 1000
        elif index == 1:
            # $script:0831180509004687$
            # - Then he said there was a legendary $npcName:23090005[gender:0]$ in the back of the cave!
            return 1000
        elif index == 2:
            # $script:0831180509004688$
            # - Now, I'm from $map:2000062$, so I've heard all sorts of adventure stories, but that was one of the biggest lies I've ever heard.
            if pick == 0:
                # $script:0831180509004689$
                # - Who knows? It could be true!
                # TODO: goto 1011, 1012
                return -1
            elif pick == 1:
                # $script:0831180509004690$
                # - Pssh, that guy was definitely a liar.
                # TODO: goto 1001, 1002
                return -1
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004691$
        # - I know, right? He's worse than I am. Uh... I mean... Ah hah hah hah!
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004692$
        # - Totally. $npcName:23090005[gender:0]$? Pssh! If such a thing really existed, don't you think it would've destroyed the world already? Hahaha.
        return -1

    def __1011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004693$
        # - Do you really think so? Does that mean the guy I talked to... is the knight from all the fables? 
        return -1

    def __1012(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004694$
        # - Come to think of it, there's no explanation for the quakes, either. Hm... Is there really something going on?
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004695$
            # - I've been thinking a lot lately.
            return 1100
        elif index == 1:
            # $script:0831180509004696$
            # - I've always wanted to be an adventurer, but I've never actually tried.
            return 1100
        elif index == 2:
            # $script:0831180509004697$
            # - Mom says I should just take over the store. Do you think I should give up on becoming an adventurer and join the family business?
            if pick == 0:
                # $script:0831180509004698$
                # - Mothers know best.
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509004699$
                # - You'd give up, just like that?
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004700$
        # - They do, don't they? Ah, maybe I should just give up on my dreams...
        return -1

    def __1102(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004701$
        # - I thought, of all people, you would encourage me to pursue my dreams! But I was wrong...
        return -1

    def __1111(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004702$
        # - What? N-no! I haven't given up. I swear!
        return -1

    def __1112(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004703$
        # - What am I saying? Of course I'm going to be the world's greatest adventurer!
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004704$
            # - I went to $map:02000031$ this afternoon to see if I could find books that contain clues to hidden treasure.
            return 2000
        elif index == 1:
            # $script:0831180509004705$
            # - But... it's pointless. I can't read a book for two minutes without falling right asleep.
            return 2000
        elif index == 2:
            # $script:0831180509004706$
            # - Every time I try, I fall asleep and wake up two hours later, totally disoriented.
            return 2000
        elif index == 3:
            # $script:0831180509004707$
            # - At this rate, I might waste away my life sleeping before I have the chance to go on an adventure! What's wrong with me?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004708$
            # - I was dusting the bookshelf today when I found this piece of paper. See that strange picture? Doesn't it look like a treasure map?
            return 2100
        elif index == 1:
            # $script:0831180509004709$
            # - See? Right here. That curvy, strange-looking pattern. It's almost like it was a quick sketch, right?
            return 2100
        elif index == 2:
            # $script:0831180509004710$
            # - Judging by the grime, it looks like a pretty old treasure map. And the shape of the picture resembles the northwest part of Victoria Island.
            return 2100
        elif index == 3:
            # $script:0831180509004711$
            # - ...Huh? This paper was just a doodle, and then used to wipe someone's nose? N-no way! You're wrong! Eek, take a closer look!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004712$
            # - Today I tried a new recipe, and I think I just made the best food I've ever tasted in my life.
            return 2200
        elif index == 1:
            # $script:0831180509004713$
            # - It smells good and tastes perfect. I'm thinking maybe I've discovered a new gift.
            return 2200
        elif index == 2:
            # $script:0831180509004714$
            # - This doesn't mean I'm no longer going to be an adventurer. It's the opposite, actually. Practicing cooking is part of my plan.
            return 2200
        elif index == 3:
            # $script:0831180509004715$
            # - You can't eat at restaurants when you're out at sea. I'm honing my cooking so I can survive any situation.
            return 2200
        elif index == 4:
            # $script:0831180509004716$
            # - Haven't you heard? The great adventurer $npcName:11000444[gender:0]$ is also known for his cooking skills! They say it rivals that of a royal chef!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __3000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004717$
            # - Everyone's trying to keep this hush hush, but I over heard. There's another world besides Maple World!
            return 3000
        elif index == 1:
            # $script:0831180509004718$
            # - Personally, I think it's related to the Shadow Doors scattered around the world. There's got to be a new world beyond those doors.
            return 3000
        elif index == 2:
            # $script:0831180509004719$
            # - Have I been through those doors? W-well... That's... Oh, right—the stove! I had a chance, but I couldn't because of the stove!
            return 3000
        elif index == 3:
            # functionID=1 openTalkReward=True 
            # $script:0831180509004720$
            # - I was just about to walk through one of those doors when I remembered I forgot to turn off the stove before I left the house. My forgetfulness stopped me from exploring a new world. What a shame!
            return -1
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004721$
            # - I heard something from sailors in $map:02000062$. They said if you travel south, you'll run into a dreadful sea monster.
            return 3100
        elif index == 1:
            # $script:0831180509004722$
            # - It's not a giant squid, like you'd think. Oh no.
            return 3100
        elif index == 2:
            # $script:0831180509004723$
            # - It's a creature with the head of a gorilla, wearing a skull mask. It has horns and flies around on giant bat wings.
            return 3100
        elif index == 3:
            # $script:0831180509004724$
            # - I can't even picture it. But here's the thing: everyone who says they saw the monster remembers it differently. So who can say if they're telling the truth or not.
            return 3100
        elif index == 4:
            # functionID=1 openTalkReward=True 
            # $script:0831180509004725$
            # - It sounds dangerous, but I'd love to see this creature with my own eyes one day. Hah hah!
            return -1
        return -1

    def __3200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004726$
            # - There are so many different types of adventures, but I grew up in a port village, so the type that calls to me are sea adventures!
            return 3200
        elif index == 1:
            # $script:0831180509004727$
            # - But that requires a ship and a crew, and ships are not cheap. I've been saving up for a long time, but I don't have enough to even buy the smallest boat! However, I've come up with an answer... 
            return 3200
        elif index == 2:
            # $script:0831180509004728$
            # - I'm going to form a party! $npcName:11000116[gender:0]$ and $npcName:11000024[gender:1]$ have already agreed to join me! And, between you and me, I can't stop thinking about $npcName:11000019[gender:0]$...
            return 3200
        elif index == 3:
            # $script:0831180509004729$
            # - I just so happened to overhear some folks in  $map:02000069$ mention that $npcName:11000019[gender:0]$ wants to buy a ship and set sail for adventure, too! He acts like he's soooo high above me because he works at $map:02000068$, but... he can be pretty charismatic and determined when he puts his mind to it.
            return 3200
        elif index == 4:
            # functionID=1 openTalkReward=True 
            # $script:0831180509004730$
            # - I can't decide if I want to ask him to join me or not. But you can't breathe a word of this to $npcName:11000019[gender:0]$, all right? You promise??
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004731$
            # - $OwnerName$, have you ever visited $map:02000068$ in $map:02000062$? Every wannabe adventurer has their heart set on joining that association.
            return 4000
        elif index == 1:
            # $script:0831180509004732$
            # - About a month ago, I went there to apply, and the guy who worked there said I had to pass an entrance exam.
            return 4000
        elif index == 2:
            # $script:0831180509004733$
            # - The exam is simple: just discover something no one else ever has. I built a raft right away and set sail from $map:02000062$.
            return 4000
        elif index == 3:
            # $script:0831180509004734$
            # - I must have been on the sea for two days. I was so hungry and exhausted that I was about to give up, when lo and behold, I saw a patch of land, just off the horizon.
            return 4000
        elif index == 4:
            # $script:0831180509004735$
            # - My heart raced! I thought I'd discovered a new land no one had ever set foot on before! But as I sailed closer, I realized... it was just $map:02000124$, which is really not all that far from $map:02000062$. 
            return 4000
        elif index == 5:
            # $script:0831180509004736$
            # - The warden intercepted my ship and held me there for a week before finally letting me return to $map:02000062$. Gosh, that's embarrassing. You're the first person I've ever told that story to, $OwnerName$.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004737$
            # - I heard a story the other day about a kid in some village who wanted to become a pirate.
            return 4100
        elif index == 1:
            # $script:0831180509004738$
            # - He ate some strange berries that gave him the power to stretch his body.
            return 4100
        elif index == 2:
            # $script:0831180509004739$
            # - And he used that ability to conquer the sea and become a pirate king! Hah hah!
            return 4100
        elif index == 3:
            # $script:0831180509004740$
            # - It's too crazy to be real, but you'd better believe I'll be poppin' every berry I see into my mouth for the rest of my life!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004741$
            # - $npcName:11000019[gender:0]$ thinks he's better than me because he works at $map:02000068$, but hello, sitting at a desk stamping docking permits is hardly the same thing as sailing for adventure.
            return 5000
        elif index == 1:
            # $script:0831180509004742$
            # - I don't need help from some stupid association to go on an adventure. Not when I have friends who think like I do!
            return 5000
        elif index == 2:
            # $script:0831180509004743$
            # - Already $npcName:11000116[gender:0]$ and $npcName:11000024[gender:1]$ have agreed to join me. $OwnerName$, what about you? I should probably also mention there's a 300,000 meso membership fee.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004744$
            # - The yearning to set sail for adventure eats away at my very core!! My ultimate dream is to be the very first to set foot on a brand new continent!
            return 5100
        elif index == 1:
            # $script:0831180509004745$
            # - I've already named my ship. Now, I just need to acquire her! Hah hah!
            return 5100
        elif index == 2:
            # $script:0831180509004746$
            # - I can tell you the name, if you're curious, but you can't tell a soul. Okay... I'm going to name her... the Nautilus!
            return 5100
        elif index == 3:
            # $script:0831180509004747$
            # - So until the day I meet my Nautilus, I'll work hard as your servant! Hah hah!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004748$
            # - I must have been around eight. We had a big ol' bookshelf at home, and one of the books on the bottom shelf changed my life forever.
            return 6000
        elif index == 1:
            # $script:0831180509004749$
            # - It was written by a great explorer, and his every word enraptured me. My heart fluttered, my eyes glazed over... I felt like I was exploring the world at his side!
            return 6000
        elif index == 2:
            # $script:0831180509004750$
            # - I knew then and there I had to become an adventurer. Ahhh. Such a great book. It was written by $npcName:11000444[gender:0]$. Have you read it?
            return 6000
        elif index == 3:
            # $script:0831180509004751$
            # - What?! You ran into $npcName:11000444[gender:0]$ in $map:02000062$?! Why didn't you tell me? I could've gone and gotten his autograph!
            return 6000
        elif index == 4:
            # $script:0831180509004752$
            # - Maybe it's not too late. I'm going to go look for him! Hey, I'm busy. Stop bothering me, will you?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004753$
            # - I'm pretty passionate about adventuring, but not as passionate as the guy in the Ant Tunnel.
            return 7000
        elif index == 1:
            # $script:0831180509004754$
            # - I think his name is $npcName:11000145[gender:0]$. He wears really weird clothes and says he's from the future.
            return 7000
        elif index == 2:
            # $script:0831180509004755$
            # - He did a good job with his costume... but I think he really truly believes he's from the future.
            return 7000
        elif index == 3:
            # $script:0831180509004756$
            # - Poor guy. I feel sorry for him. He's clearly not well.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509004757$
        # - Hello. It's a perfect day to go on an adventure, isn't it?
        if pick == 0:
            # $script:0831180509004758$
            # - Yep!
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509004759$
            # - I don't know...
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509004760$
            # - Who are you?
            # TODO: goto 105, 106
            return -1
        return -1

