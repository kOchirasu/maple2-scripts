""" 11000774: Mino """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])


    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509002785$
        # - Hey, you're back.
        if pick == 0:
            # $script:0831180509002786$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002787$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002788$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509002789$
        # - On days like this, I love to chill with friendly folks on the street. You?
        if pick == 0:
            # $script:0831180509002790$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002791$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002792$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509002793$
        # - Welcome back, $OwnerName$. Things went well, I take it?
        if pick == 0:
            # $script:0831180509002794$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002795$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002796$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509002797$
        # - Hey, you're back.
        if pick == 0:
            # $script:0831180509002798$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002799$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002800$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002801$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509002802$
        # - On days like this, I love to chill with friendly folks on the street. You?
        if pick == 0:
            # $script:0831180509002803$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002804$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002805$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002806$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509002807$
        # - Welcome back, $OwnerName$. Things went well, I take it?
        if pick == 0:
            # $script:0831180509002808$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002809$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002810$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002811$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509002812$
        # - Is it time for my paycheck?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509002813$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002814$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002815$
        # - Nah, I'm happy to share your burden.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002816$
        # - My muse is knocking. I need to go answer.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002817$
        # - Nah, I'm happy to share your burden.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002818$
        # - My muse is knocking. I need to go answer.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002819$
        # - Our contract is up soon, $OwnerName$. 
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002820$
        # - Write it down or something, and free your mind to think about something else.
        if pick == 0:
            # $script:0831180509002821$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002822$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002823$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002824$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509002825$
        # - Is there something you want to say?
        if pick == 0:
            # $script:0831180509002826$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002827$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002828$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002829$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509002830$
        # - You wanna chat? Was there something you wanted to ask me?
        if pick == 0:
            # $script:0831180509002831$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002832$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002833$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002834$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509002835$
        # - Haven't we been talking this whole time? Or is my memory playing tricks on me again...
        if pick == 0:
            # $script:0831180509002836$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002837$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002838$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002839$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509002841$
        # - In your heart, can you feel it? Can you feel that you already paid me this month? It's like a poem, deep inside you.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509002844$
        # - Take responsibility, you know? Don't blame someone else.
        if pick == 0:
            # $script:0831180509002845$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002846$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002847$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509002848$
        # - Nothing in this world lasts forever.
        if pick == 0:
            # $script:0831180509002849$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002850$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002851$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509002852$
        # - Why do words float in the air after they leave my mouth?
        if pick == 0:
            # $script:0831180509002853$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002854$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002855$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002858$
        # - Just $MaidPassedDay$ ago, were sharing one vision. I wonder why that changed...
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002859$
        # - I wish you were more honest with me.
        if pick == 0:
            # $script:0831180509002860$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002861$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002862$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509002863$
        # - Are you really there? 
        if pick == 0:
            # $script:0831180509002864$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002865$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002866$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509002867$
        # - We grew apart $MaidPassedDay$ ago. It's nobody's fault. These things happen. But there just wasn't any closure, you know?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509002868$
        # - My soul can't be measured by something as materialistic as wages, but I made a pledge to Helping Hands. I can't serve without being paid. That was the price I had to pay to meet my soul mate: you. I thought we were on the same page with all that, but maybe I was wrong.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509002869$
        # - My muse stopped by today. I wanted to let her pour over me, but I couldn't. You get what I'm saying?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002870$
        # - The muse makes my heart float and sink at the same time. I have to let both of those feeling flow over me.
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002871$
        # - You don't really get what I'm saying, do you?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002872$
        # - Don't ask too many questions.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002873$
        # - I have to look in the mirror once in a while, or else I forget what I look like.
        if pick == 0:
            # $script:0831180509002874$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002875$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002876$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002877$
        # - I have to look in the mirror once in a while, or else I forget what I look like.
        if pick == 0:
            # $script:0831180509002878$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002879$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002880$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002881$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509002882$
        # - We can talk for as long as you want. I needed a break, anyway.
        if pick == 0:
            # $script:0831180509002883$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509002884$
            # - (Praise your servant.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509002885$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509002886$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509002887$
        # - Ah, good conversation is always welcome, and I always enjoy talking to you, $OwnerName$.
        if pick == 0:
            # $script:0831180509002888$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509002889$
            # - (Praise your servant.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509002890$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509002891$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509002892$
        # - The truth of the universe breathes inside every one of us.
        if pick == 0:
            # $script:0831180509002893$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509002894$
            # - (Praise your servant.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509002895$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509002896$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509002897$
        # - Is there something you want to say?
        if pick == 0:
            # $script:0831180509002898$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002899$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002900$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509002901$
        # - You wanna chat? Was there something you wanted to ask me? Or maybe... you're also drawn to the same mysterious power...
        if pick == 0:
            # $script:0831180509002902$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002903$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002904$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509002905$
        # - Haven't we been talking this whole time? Or is my memory playing tricks on me again...
        if pick == 0:
            # $script:0831180509002906$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002907$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002908$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002909$
            # - I've decided that today is the combination of sensitivity and specialty.
            return 1000
        elif index == 1:
            # $script:0831180509002910$
            # - More intense than yesterday, and more thrilling than tomorrow. Or just possible, the opposite.
            if pick == 0:
                # $script:0831180509002911$
                # - (Say that you feel the same way sometimes.)
                # TODO: goto 1011, 1012
                return -1
            elif pick == 1:
                # $script:0831180509002912$
                # - (Say nothing.)
                # TODO: goto 1001, 1002
                return -1
            return -1
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002917$
            # - I entrusted my soul to music a while back, in a desperate attempt to forget the anguish of life. 
            return 1100
        elif index == 1:
            # $script:0831180509002918$
            # - You should try to face your inner self sometimes. Here, take this earphone and put it in your ear.
            return 1100
        elif index == 2:
            # $script:0831180509002919$
            # - Now, close your eyes and get lost in the darkness. There! Our souls resonated with each other! Did you feel that?
            if pick == 0:
                # $script:0831180509002920$
                # - No...
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509002921$
                # - Yes!
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002926$
            # - This was such an amazing moment. Not sure if you'd agree...?
            return 2000
        elif index == 1:
            # $script:0831180509002927$
            # - Today it drizzled, just a bit, but it was enough to quench my heart's thirst.
            return 2000
        elif index == 2:
            # $script:0831180509002928$
            # - I haven't felt this way for a long time... Maybe I still have some warmth left in me. I feel... hopeful.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002929$
            # - I saw the guy next door come home in a helicopter, and that changed my whole perception of him. Interesting, huh?
            return 2100
        elif index == 1:
            # $script:0831180509002930$
            # - Sure, I'd love to ride in a helicopter someday. Maybe my tired soul can finally take a breath, hundreds of miles above the world.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002931$
            # - Today, I met a girl who lives in the neighborhood. She inspired me to pick up scissors for the first time in a long time. Not many folks "get" my art style, you know?
            return 2200
        elif index == 1:
            # $script:0831180509002932$
            # - I wonder if the tears I shed after that last snip were were of joy or yearning...
            return 2200
        elif index == 2:
            # $script:0831180509002933$
            # - That look on your face... Mm, you still don't understand me, do you? It's cool. An appreciation of true art isn't something that can be acquired. It's something you've got to be born with.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002938$
            # - I appreciate that, but you don't have to keep telling me. Sometimes words mean more when they're not spoken, you hear me?
            return 4000
        elif index == 1:
            # $script:0831180509002939$
            # - I get if you don't get it. I'm a deep guy with so many layers. Don't force yourself. We'll solve this puzzle together.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002940$
            # - I don't mind feeling this way. I assume this is how ordinary people feel all the time.
            return 4100
        elif index == 1:
            # $script:0831180509002941$
            # - But for me... Let's just say it'll take a while to get used to this.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002942$
            # - When it's sunny and there's not much to do, I go out for a walk. Not to take a break, but just to look normal, like everyone else.
            return 5000
        elif index == 1:
            # $script:0831180509002943$
            # - $OwnerName$, how does taking a walk make you feel? For me, let's just say it calms the darkness inside me.
            return 5000
        elif index == 2:
            # $script:0831180509002944$
            # - Don't take it personally, but... I don't want to take a walk with you. I've reserved that time to spend with me, you know? So I can't share it with anybody else.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002945$
            # - Why do I use left-handed scissors with my right hand? I'm surprised you even noticed.
            return 5100
        elif index == 1:
            # $script:0831180509002946$
            # - You may not understand this, but I'm not the one who chooses that. When I touch someone's hair, I get a feeling deep inside, and that feeling determines which hand I use to cut with.
            return 5100
        elif index == 2:
            # $script:0831180509002947$
            # - Come to think of it, I haven't held these scissors with my left hand for a long time. Only fate knows when I'll do that again. To be honest, right now, I'm just too tired to think about it.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002948$
            # - Sometimes, I just like wearing earphones, without listening to anything.
            return 6000
        elif index == 1:
            # $script:0831180509002949$
            # - I do it when I want to be left alone, so I can have some time with myself.
            return 6000
        elif index == 2:
            # $script:0831180509002950$
            # - You don't get it, do you, $OwnerName$? It's okay. I'm used to not being understood.
            return 6000
        elif index == 3:
            # $script:0831180509002951$
            # - Of course, I have my favorites when it comes to music. I'll play some for you when I have a chance. It'll help you understand where I get my inspiration.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002952$
            # - $OwnerName$, do you have any siblings? I've never told anyone but... I actually have an older brother.
            return 7000
        elif index == 1:
            # $script:0831180509002953$
            # - I left home when I was pretty young. He used to send me letters, but it's been a long, long time since the last one.
            return 7000
        elif index == 2:
            # $script:0831180509002954$
            # - I picked this place partly because it's bustling with activity and partly because my brother mailed his last letter from somewhere around here.
            return 7000
        elif index == 3:
            # $script:0831180509002955$
            # - Recently, I met an adventurer who I think traveled with my brother for a while. I couldn't be sure, though.
            return 7000
        elif index == 4:
            # $script:0831180509002956$
            # - According to him, my brother is doing fine. I don't know what happened to him, but I'm hoping to rn into here one day.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509002957$
        # - Weren't you just here yesterday? You looking for the owner?
        if pick == 0:
            # $script:0831180509002958$
            # - Yep!
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509002959$
            # - Nope!
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509002960$
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
