""" 11000789: Arita """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])


    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509004783$
        # - Please! One moment, I'm talking to this zelkova.
        if pick == 0:
            # $script:0831180509004784$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004785$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004786$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509004787$
        # - Isn't it a wonderful day?
        if pick == 0:
            # $script:0831180509004788$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004789$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004790$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509004791$
        # - Please be careful not to tread on grass or flowers when you walk.
        if pick == 0:
            # $script:0831180509004792$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004793$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004794$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509004795$
        # - Please! One moment, I'm talking to this zelkova.
        if pick == 0:
            # $script:0831180509004796$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004797$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004798$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004799$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509004800$
        # - Isn't it a wonderful day?
        if pick == 0:
            # $script:0831180509004801$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004802$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004803$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004804$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509004805$
        # - Please be careful not to tread on grass or flowers when you walk.
        if pick == 0:
            # $script:0831180509004806$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004807$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004808$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004809$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509004810$
        # - Did you just say you're going to pay me?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509004811$
            # - Never mind.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004812$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004813$
        # - Aha, our contract renews every time you pay me, right? That's how human contracts work? I feel like I've learned something new and fascinating about human culture, and that makes me happy!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004814$
        # - Ah, I know. Accepting this means I accept the extension of our contract. I'm learning so much about you unusual creatures, thanks to you!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004815$
        # - Keeping a promise made to a human is tough, but I saw it through, didn't I? I feel like I've really accomplished something great. Thanks for the experience!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004816$
        # - Really? Hehe. I had no idea how difficult it was to be idle all day. Thank you for helping me keep my promise, $OwnerName$!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004817$
        # - $OwnerName$, did you know our employment agreement expires soon?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004818$
        # - Why are humans so high maintenance?
        if pick == 0:
            # $script:0831180509004819$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004820$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004821$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004822$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509004823$
        # - Mm? Do you have something else to tell me?
        if pick == 0:
            # $script:0831180509004824$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004825$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004826$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004827$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509004828$
        # - Please! One moment, I'm talking to this zelkova.
        if pick == 0:
            # $script:0831180509004829$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004830$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004831$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004832$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509004833$
        # - Please be careful not to tread on grass or flowers when you walk.
        if pick == 0:
            # $script:0831180509004834$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004835$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004836$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004837$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509004839$
        # - Hehe, you already paid me this month, $OwnerName$!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509004842$
        # - There are some things I just can't do, no matter how hard I try.
        if pick == 0:
            # $script:0831180509004843$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004844$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004845$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509004846$
        # - Is something wrong?
        if pick == 0:
            # $script:0831180509004847$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004848$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004849$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509004850$
        # - I want to plant more flowers! You're not interested in that, are you?
        if pick == 0:
            # $script:0831180509004851$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004852$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004853$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004856$
        # - It's been $MaidPassedDay$ since our contract expired. I may live a long, long life, $OwnerName$, but I want our time together to be meaningful.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004857$
        # - Time never stops, and it never waits for anyone.
        if pick == 0:
            # $script:0831180509004858$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004859$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004860$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509004861$
        # - Mm... Okay.
        if pick == 0:
            # $script:0831180509004862$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004863$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004864$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509004865$
        # - $OwnerName$! What happened? Won't you tell me? I know something happened... I thought we were closer than that...
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004866$
            # - Did you know fairies make contracts to use magic and spells? To us, contracts are promises we make in exchange for power. Humans, it seems, mainly use contracts for things involving time and money. When I signed on with Helping Hands, I made a promise to the company about accepting a certain wage.
            return 9031
        elif index == 1:
            # $script:0831180509004867$
            # - I would love to do you a favor without anything in return, but that would mean breaking my promise... I made a promise to Helping Hands in exchange for an opportunity to learn more about humans. I hope you can understand that, $OwnerName$.
            # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
            return -1
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509004868$
        # - $OwnerName$, you haven't talked to me lately. You didn't use to be like this. Oh, never mind. For a moment, I forgot you were human, hehe!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004869$
        # - Mama taught me this! I'm good at it, hehe.
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004870$
        # - Sure! Anytime.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004871$
        # - $OwnerName$, you're the first human I've shared so much with...
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004872$
        # - Isn't it a wonderful day?
        if pick == 0:
            # $script:0831180509004873$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004874$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004875$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004876$
        # - Isn't it a wonderful day?
        if pick == 0:
            # $script:0831180509004877$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004878$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004879$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004880$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509004881$
        # - Fairies are good at keeping secrets. You can tell me anything!
        if pick == 0:
            # $script:0831180509004882$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509004883$
            # - Tell me something about fairies.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509004884$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509004885$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509004886$
        # - You look like you have something to say.
        if pick == 0:
            # $script:0831180509004887$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509004888$
            # - Tell me something about fairies.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509004889$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509004890$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509004891$
        # - Sometimes, I wonder how things are back in $map:2000023$.
        if pick == 0:
            # $script:0831180509004892$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509004893$
            # - Tell me something about fairies.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509004894$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509004895$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509004896$
        # - Mm? Do you have something else to tell me?
        if pick == 0:
            # $script:0831180509004897$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004898$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004899$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509004900$
        # - Please! One moment, I'm talking to this zelkova.
        if pick == 0:
            # $script:0831180509004901$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004902$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004903$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509004904$
        # - Please be careful not to tread on grass or flowers when you walk.
        if pick == 0:
            # $script:0831180509004905$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004906$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004907$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004908$
            # - I can't help it. I just don't trust humans.
            return 1000
        elif index == 1:
            # $script:0831180509004909$
            # - I know you're not like the others, $OwnerName$. But... we're just so different.
            return 1000
        elif index == 2:
            # $script:0831180509004910$
            # - I know we should all just accept one another, but I can't get used to your kind's disregard for nature or penchant for violence. Am I wrong to feel this way?
            if pick == 0:
                # $script:0831180509004911$
                # - Nah.
                # TODO: goto 1011, 1012
                return -1
            elif pick == 1:
                # $script:0831180509004912$
                # - Yeah.
                # TODO: goto 1001, 1002
                return -1
            return -1
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004917$
            # - $OwnerName$, I want to ask you something.
            return 1100
        elif index == 1:
            # $script:0831180509004918$
            # - I've mentioned a few times that fairies aren't fond of humans.
            return 1100
        elif index == 2:
            # $script:0831180509004919$
            # - But what's your opinion, $OwnerName$? Do you like fairies?
            if pick == 0:
                # $script:0831180509004920$
                # - Of course.
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509004921$
                # - I want to learn more about your species, honestly.
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004926$
            # - I made this pendant with a stone I found in my forest. Pretty, isn't it?
            return 2000
        elif index == 1:
            # $script:0831180509004927$
            # - Heh heh, surprised? My mom taught me when I was young. She's a famous craftswoman in $map:02000023$.
            return 2000
        elif index == 2:
            # $script:0831180509004928$
            # - But I don't think this is just some ordinary stone. It gives off a strange vibe, like... magic.
            return 2000
        elif index == 3:
            # $script:0831180509004929$
            # - I want to know more! I'm going to show it to $npcName:11000031[gender:0]$ tomorrow.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004930$
            # - Yesterday $npcName:11000034[gender:0]$ stopped by. He must have been worried that I'm staying with a human.
            return 2100
        elif index == 1:
            # $script:0831180509004931$
            # - He kept urging me to return to the forest, but I told him I can better relate to you than I can to other humans. And it's true. Hehe.
            return 2100
        elif index == 2:
            # $script:0831180509004932$
            # - $npcName:11000034[gender:0]$ would agree if he met you. If you ever have business in $map:02000023$, would you give my regards to $npcName:11000034[gender:0]$?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004933$
            # - I prepare food for you every day, but do you really have to eat animals and plants?
            return 2200
        elif index == 1:
            # $script:0831180509004934$
            # - Fairies only need one glass of honey milk in the morning and one in the afternoon. Animals and plants are my friends, and I shouldn't eat my friends, right?
            return 2200
        elif index == 2:
            # $script:0831180509004935$
            # - You don't need to look so guilty. I know you can't live on just milk like I can.
            return 2200
        elif index == 3:
            # $script:0831180509004936$
            # - "Nature makes us what we are." That's what $npcName:11000031[gender:0]$ says. Eat up!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004944$
            # - Have you ever wondered why I don't have wings?
            return 4000
        elif index == 1:
            # $script:0831180509004945$
            # - It's because there are all different types of fairies... Tree tree fairies, flower fairies, river fairies, and all sorts of others.
            return 4000
        elif index == 2:
            # $script:0831180509004946$
            # - Some have wings, some don't... and some just have one wing... 
            return 4000
        elif index == 3:
            # $script:0831180509004947$
            # - Never mind that. My point is, if you ever visit $map:02000023$, make sure you don't ask such a silly question or everyone will laugh at you.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004948$
            # - $npcName:11000284[gender:1]$... She's lost her shoes again. How disgraceful!
            return 4100
        elif index == 1:
            # $script:0831180509004949$
            # - I've told her so many times! If she truly loves her shoes, then don't wear them outside of the forest!
            return 4100
        elif index == 2:
            # $script:0831180509004950$
            # - Unbelievable! I hope no one helps her this time, so she learns her lesson.
            return 4100
        elif index == 3:
            # $script:0831180509004951$
            # - ...But that's wishful thinking. Humans can't resist helping her when she cries, and she knows that.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004952$
            # - Yesterday, the wind told me that trees and flowers are disappearing on the west side of Victoria Island.
            return 5000
        elif index == 1:
            # $script:0831180509004953$
            # - I'm guessing it must the area around $map:02000100$. I've never been there, and I'm glad! I couldn't survive even a single day in such a sad place.
            return 5000
        elif index == 2:
            # $script:0831180509004954$
            # - Why do humans love to dig? Why do you love tall buildings so much?
            return 5000
        elif index == 3:
            # $script:0831180509004955$
            # - You're building homes for yourselves but destroying ours.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004956$
            # - I don't hate all humans. I have great respect for $npc:11000075[gender:1]$ and for $npcName:11000039[gender:1]$.
            return 5100
        elif index == 1:
            # $script:0831180509004957$
            # - I have many things I can learn from $npcName:11000042[gender:1]$. I think there are only a handful of fairies who possess more ancient knowledge than he does.
            return 5100
        elif index == 2:
            # $script:0831180509004958$
            # - Humans and fairies are so different. I'm having a hard time getting used to you. We haven't interacted with each other for a long time. You can't expect for us to become friends overnight.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004959$
            # - Soon it'll be my birthday. Let's celebrate together. And don't even think to ask how many candles we'll need...
            return 6000
        elif index == 1:
            # $script:0831180509004960$
            # - Oh, fine, since you're my friend, I'll give you a hint.
            return 6000
        elif index == 2:
            # $script:0831180509004961$
            # - I just want one candle. I'm not even a hundred yet! I'm pretty young for the fairfolk.
            return 6000
        elif index == 3:
            # $script:0831180509004962$
            # - Fairies live a lot longer than humans, you know.
            return 6000
        elif index == 4:
            # $script:0831180509004963$
            # - You'd be shocked if you knew how old $npcName:11000033[gender:0]$ or $npcName:11000031[gender:0]$ are. You really just can't think of our ages in human years.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004964$
            # - Lately $npcName:11000032[gender:0]$ hasn't looked so good. I'm worried something happened to him.
            return 7000
        elif index == 1:
            # $script:0831180509004965$
            # - I tried to ask, but he wouldn't answer. $npcName:11000031[gender:0]$ seemed to know something, but he wouldn't tell me either.
            return 7000
        elif index == 2:
            # $script:0831180509004966$
            # - Actually $npcName:11000032[gender:0]$ was the reason I got a job with Helping Hands. He left one day all of a sudden, and it dawned on me that I didn't know much about him.
            return 7000
        elif index == 3:
            # $script:0831180509004967$
            # - $npcName:11000032[gender:0]$ is half-human and half-fairy. It must have been hard growing up like that, but he never showed it. I would've been nicer if I'd known he'd leave so abruptly...
            return 7000
        elif index == 4:
            # $script:0831180509004968$
            # - That's why I wanted to learn more about humans. I'm glad I applied for this job. Staying here with you has been so informative!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509004969$
        # - Eeek! Human!! Sheesh, you scared me!
        if pick == 0:
            # $script:0831180509004970$
            # - Sorry for startling you.
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509004971$
            # - Ha! I'm gonna step on you!
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509004972$
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
