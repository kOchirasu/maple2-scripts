""" 11000769: Manu """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])


    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509001630$
        # - Did you call me, $OwnerName$?
        if pick == 0:
            # $script:0831180509001631$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001632$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001633$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509001634$
        # - Have a great day, $OwnerName$!
        if pick == 0:
            # $script:0831180509001635$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001636$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001637$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509001638$
        # - Yes, $OwnerName$?
        if pick == 0:
            # $script:0831180509001639$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001640$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001641$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509001642$
        # - Did you call me, $OwnerName$?
        if pick == 0:
            # $script:0831180509001643$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001644$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001645$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001646$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509001647$
        # - Have a great day, $OwnerName$!
        if pick == 0:
            # $script:0831180509001648$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001649$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001650$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001651$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509001652$
        # - Yes, $OwnerName$?
        if pick == 0:
            # $script:0831180509001653$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001654$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001655$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001656$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509001657$
        # - Mm? Are you going to pay me?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509001658$
            # - Never mind.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001659$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001660$
        # - Oh, I'm so glad you found me useful. Thank you for extending our contract. I'm happy to stay with you for another month.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001661$
        # - Hah hah hah, it feels great to get paid for my work work. Thank you.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001662$
        # - Ah, this explains your cheerful mood. What's good for you is good for me, and vice versa. That's what friends are for, right? To share in each other's happiness.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001663$
        # - Ah, I know I said everything was fine, but it really wasn't. I didn't want to tell you the truth, because I knew it was harder on you than it was on me. I'm glad everything worked out! Hah hah!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001664$
        # - In case you've forgotten, our contract expires soon. I know it's not easy keeping track of everything going on in your life.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001665$
        # - But that's what I'm here for. Hah hah.
        if pick == 0:
            # $script:0831180509001666$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001667$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001668$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001669$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509001670$
        # - You can tell me anything.
        if pick == 0:
            # $script:0831180509001671$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001672$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001673$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001674$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509001675$
        # - Sometimes, I feel lonely when I'm by myself.
        if pick == 0:
            # $script:0831180509001676$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001677$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001678$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001679$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509001680$
        # - Yikes... My back's killing me today... 
        if pick == 0:
            # $script:0831180509001681$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001682$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001683$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001684$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509001686$
        # - You want to pay me? But you've already paid me for the month. You're as forgetful as I am sometimes.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509001689$
        # - Aww... Why do you look so exhausted? 
        if pick == 0:
            # $script:0831180509001690$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001691$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001692$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509001693$
        # - The older you get, the less food your body needs.
        if pick == 0:
            # $script:0831180509001694$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001695$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001696$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509001697$
        # - Having nothing to do is so dull. It's been $MaidPassedDay$ since I've had a job.
        if pick == 0:
            # $script:0831180509001698$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001699$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001700$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001703$
        # - I told you not to worry about me. Everything will work out eventually.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001704$
        # - The power of positive thinking, right? Hah hah. 
        if pick == 0:
            # $script:0831180509001705$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001706$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001707$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509001708$
        # - I don't think I can go for a walk today. My knees are aching... 
        if pick == 0:
            # $script:0831180509001709$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001710$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001711$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509001712$
        # - When the wind becomes overwhelming, mimic the reeds. Follow the wind without losing your footing. Hah hah hah, are you thinking I've finally lost my mind? I just thought you could use some encouragement.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509001713$
        # - I miss my wife. When things got tough for us, like they are for your now, Madelle helped me get through it. What I'm trying to say is, I may not be able to do much, but I'm here for you.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509001714$
        # - Everyone should experience poverty at least once. It gives you perspective. Once you've climbed a cliff, even the steepest hill is no longer intimidating.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001715$
        # - Ask me for anything. I'll make it for you if I can.
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001716$
        # - Don't worry about it. I'm doing this to pass time.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001717$
        # - Do you have questions for me?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001718$
        # - Hm, it's not easy to describe oneself in just a few words. 
        if pick == 0:
            # $script:0831180509001719$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001720$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001721$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001722$
        # - Hm, it's not easy to describe oneself in just a few words. 
        if pick == 0:
            # $script:0831180509001723$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001724$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001725$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001726$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509001727$
        # - I love talking to people.
        if pick == 0:
            # $script:0831180509001728$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509001729$
            # - Tell me a story!
            # TODO: goto 3000, 3100, 4000, 4100, 4200, 4300, 9011
            return -1
        elif pick == 2:
            # $script:0831180509001730$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509001731$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509001732$
        # - Oh, you want to keep this old man company?
        if pick == 0:
            # $script:0831180509001733$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509001734$
            # - Tell me a story!
            # TODO: goto 3000, 3100, 4000, 4100, 4200, 4300, 9011
            return -1
        elif pick == 2:
            # $script:0831180509001735$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509001736$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509001737$
        # - What kind of story? Is there something in particular you want to hear?
        if pick == 0:
            # $script:0831180509001738$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509001739$
            # - Tell me a story!
            # TODO: goto 3000, 3100, 4000, 4100, 4200, 4300, 9011
            return -1
        elif pick == 2:
            # $script:0831180509001740$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509001741$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509001742$
        # - You can tell me anything.
        if pick == 0:
            # $script:0831180509001743$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001744$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001745$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509001746$
        # - Sometimes, I feel lonely when I'm by myself.
        if pick == 0:
            # $script:0831180509001747$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001748$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001749$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509001750$
        # - Yikes... My back's killing me today... 
        if pick == 0:
            # $script:0831180509001751$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001752$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001753$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001754$
            # - Oh, I almost forgot.
            return 1000
        elif index == 1:
            # $script:0831180509001755$
            # - It felt so strange cooking for the first time in decades. Worse, everything was so blurry I could hardly tell the difference between sugar and salt.
            return 1000
        elif index == 2:
            # $script:0831180509001756$
            # - So I just used the first thing I grabbed. Turns out, it was the wrong one. But you looked hungry, so here it is!
            if pick == 0:
                # $script:0831180509001757$
                # - It's too salty.
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509001758$
                # - It's delicious.
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001763$
            # - Guess what I have in my hand...?
            return 1100
        elif index == 1:
            # $script:0831180509001764$
            # - Snacks! I thought you might be hungry.
            return 1100
        elif index == 2:
            # $script:0831180509001765$
            # - It tastes better than it looks. I hope.
            if pick == 0:
                # $script:0831180509001766$
                # - Great! I was feeling a little hungry!
                # TODO: goto 1111, 1112
                return -1
            elif pick == 1:
                # $script:0831180509001767$
                # - I'll pass. I'm, um, trying to lose weight. Yeah.
                # TODO: goto 1101, 1102
                return -1
            return -1
        return -1

    def __1200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001772$
            # - I was visiting the senior center today, and someone gave me this drink. I thought you might like it.
            return 1200
        elif index == 1:
            # $script:0831180509001773$
            # - When you get to be my age, you already know what you like and don't want to try new things.
            if pick == 0:
                # $script:0831180509001774$
                # - Aw, you should try it. You might like it.
                # TODO: goto 1201, 1202
                return -1
            elif pick == 1:
                # $script:0831180509001775$
                # - Hey, thanks!
                # TODO: goto 1211, 1212
                return -1
            return -1
        return -1

    def __1300(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001780$
            # - I cooked some food my wife used to make. I never watched her cook, though.
            return 1300
        elif index == 1:
            # $script:0831180509001781$
            # - It tastes like its missing something, but I can't quite put my finger on it... What do you think?
            if pick == 0:
                # $script:0831180509001782$
                # - Hmm, not bad, but could use a sprinkle of MSG.
                # TODO: goto 1301, 1302
                return -1
            elif pick == 1:
                # $script:0831180509001783$
                # - It's pretty delicious just the way it is.
                # TODO: goto 1311, 1312
                return -1
            return -1
        return -1

    def __1400(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001788$
            # - Tsk, you should be more careful. I found this by the front door on my way out.
            return 1400
        elif index == 1:
            # $script:0831180509001789$
            # - Usually, I can't see far enough to notice an item on the ground, but lucky for you, I had to adjust my shoes.
            if pick == 0:
                # $script:0831180509001790$
                # - Thanks for finding it.
                # TODO: goto 1411, 1412
                return -1
            elif pick == 1:
                # $script:0831180509001791$
                # - It's not mine.
                # TODO: goto 1401, 1402
                return -1
            return -1
        return -1

    def __1500(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001796$
            # - I ran into Choi the real estate agent on my way home today. One of his clients just moved to a smaller and gave him a bunch of furniture that wouldn't fit.
            return 1500
        elif index == 1:
            # $script:0831180509001797$
            # - It was way too much, but Choi didn't want to throw it out, either. He asked me to take whatever I wanted, so I grabbed this. It looked like the best of the bunch. It's all yours now!
            if pick == 0:
                # $script:0831180509001798$
                # - I don't really need it...
                # TODO: goto 1501, 1502
                return -1
            elif pick == 1:
                # $script:0831180509001799$
                # - Thanks!
                # TODO: goto 1511, 1512
                return -1
            return -1
        return -1

    def __1600(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001804$
            # - Do you know what happened today? I was out walking when I ran into an overturned wagon. I helped the owner move it back into place.
            return 1600
        elif index == 1:
            # $script:0831180509001805$
            # - And he gave me money for helping him. Hah hah hah! Here, take it. I've got no use for so much money. Think of it as an allowance from your grandpa.
            if pick == 0:
                # $script:0831180509001806$
                # - Hey, thanks!
                # TODO: goto 1611, 1612
                return -1
            elif pick == 1:
                # $script:0831180509001807$
                # - I can't take your money!
                # TODO: goto 1601, 1602
                return -1
            return -1
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001812$
            # - Not much. I worked around the house all day.
            return 2000
        elif index == 1:
            # $script:0831180509001813$
            # - A writer once said the people weren't born to work. If we were, it wouldn't make us so tired.
            return 2000
        elif index == 2:
            # $script:0831180509001814$
            # - I agree with him, now that I know how tiresome housework really is.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001815$
            # - I was thinking of my wife while I cleaned today. She used to hum when she did her chores.
            return 2100
        elif index == 1:
            # $script:0831180509001816$
            # - So I tried that today. It actually lifted my spirits and made the work less boring.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001817$
            # - Nothing happened to me or the house, but...
            return 2200
        elif index == 1:
            # $script:0831180509001818$
            # - I met Choi the real estate agent while taking a walk. He said he saw someone hanging onto a flying eagle.
            return 2200
        elif index == 2:
            # $script:0831180509001819$
            # - I don't know why he makes such absurd claims sometimes. It would've been more believable if he said he saw someone hanging onto a balloon. Hah hah.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001824$
            # - I'm not a funny person, and I don't know any funny stories. Hah hah hah. But I know how to keep people engaged in what I'm saying, and that's to tell them what I think of them.
            return 4000
        elif index == 1:
            # $script:0831180509001825$
            # - I can tell you what I think of you, if you want. Oh, your ears are already perking up! Hah hah!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001826$
            # - Once upon a time...
            #   ...
            #   ...
            return 4100
        elif index == 1:
            # $script:0831180509001827$
            # - Are you asleep?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001828$
            # - You want to ask me something personal?
            return 5000
        elif index == 1:
            # $script:0831180509001829$
            # - We all are like the moon: each one of us has a dark side that we don't want to show others.
            return 5000
        elif index == 2:
            # $script:0831180509001830$
            # - If you're asking about my dark side, I'd rather not talk about it. Let's talk about yours instead. I'm all ears.
            return 5000
        elif index == 3:
            # $script:0831180509001831$
            # - You've been all over Victoria Island. Which part do you like the most?
            return 5000
        elif index == 4:
            # $script:0831180509001832$
            # - I don't care if you go anywhere else, but please don't go to $map:2000124$.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001833$
            # - One morning I woke up to realize that all my desire for worldly wealth had vanished overnight. Everything here is fleeting.
            return 5100
        elif index == 1:
            # $script:0831180509001834$
            # - The realization that the years you have left are fewer than the years you've already lived does that to you.
            return 5100
        elif index == 2:
            # $script:0831180509001835$
            # - An old scholar once said man's purpose is to make meaningless things meaningful. I'd better live whatever life I have left to the fullest, so I can die without regrets.
            return 5100
        elif index == 3:
            # $script:0831180509001836$
            # - I really like this job. When my wife passed, I was so heartbroken that I didn't want to do anything for a long, long time.
            return 5100
        elif index == 4:
            # $script:0831180509001837$
            # - Then I realized living in the past was doing me more harm than good.
            return 5100
        elif index == 5:
            # $script:0831180509001838$
            # - So I decided to let the past go, enjoy the present, and wait for whatever the future brings.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001839$
            # - I started writing a while ago. But I'm not writing a novel.
            return 6000
        elif index == 1:
            # $script:0831180509001840$
            # - I'm not writing something to show others. It's just for myself.
            return 6000
        elif index == 2:
            # $script:0831180509001841$
            # - Someone once told me that writing helps you deal with difficult emotions and find happiness again.
            return 6000
        elif index == 3:
            # $script:0831180509001842$
            # - So I'm writing to be happy. Please don't be too nosy about what I'm writing.
            return 6000
        elif index == 4:
            # $script:0831180509001843$
            # - Does my writing include things about you? Well... You'll see for yourself if I decide to show you one day.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001844$
            # - You want to know about me and my wife? I can't think of anything special to say. Hah hah. 
            return 7000
        elif index == 1:
            # $script:0831180509001845$
            # - It was always just the two of us, me and Madelle. We couldn't have children... That was hard for both of us.
            return 7000
        elif index == 2:
            # $script:0831180509001846$
            # - In hindsight, maybe that made us even closer. It was a pain we shared together. 
            return 7000
        elif index == 3:
            # $script:0831180509001847$
            # - Am I sorry that I don't have children? No. But I miss the time I shared with my wife.
            return 7000
        elif index == 4:
            # $script:0831180509001848$
            # - Being with Madelle, I always felt warm and peaceful. We'd been together for so long that we could read each other's thoughts. But when I think about it now, I wish I had talked to her more often.
            return 7000
        elif index == 5:
            # $script:0831180509001849$
            # - Do you have someone you love? If not, I hope you find someone as good as my Madelle.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509001850$
        # - I didn't hear the bell ring. May I ask who you are? Are you here to see the owner of the house?
        if pick == 0:
            # $script:0831180509001851$
            # - Yep!
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509001852$
            # - Nope!
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509001853$
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
