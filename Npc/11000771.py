""" 11000771: Moma """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509002121$
        # - $OwnerName$, welcome home. Huh? N-no, I wasn't waiting for you or anything...
        if pick == 0:
            # $script:0831180509002122$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002123$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002124$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509002125$
        # - I'm busy. If you have something to say, just say it.
        if pick == 0:
            # $script:0831180509002126$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002127$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002128$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509002129$
        # - You're such a handful.
        if pick == 0:
            # $script:0831180509002130$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002131$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002132$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509002133$
        # - $OwnerName$, welcome home. Huh? N-no, I wasn't waiting for you or anything...
        if pick == 0:
            # $script:0831180509002134$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002135$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002136$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002137$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509002138$
        # - I'm busy. If you have something to say, just say it.
        if pick == 0:
            # $script:0831180509002139$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002140$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002141$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002142$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509002143$
        # - You're such a handful.
        if pick == 0:
            # $script:0831180509002144$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002145$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002146$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002147$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509002148$
        # - Huh? Do you want to give me my paycheck?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509002149$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002150$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002151$
        # - I hope you're not expecting me to thank you. I earned this. But it does motivate me to work harder...
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002152$
        # - Okay, fine, thank you. But let me make one thing clear: I'm not doing this because I like you, $OwnerName$.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002153$
        # - <font color="#909090">(Her eyes get misty.)</font>
        #   Oh! How...? I'm not crying, you idiot. I've just got something in my eye!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002154$
        # - Sheesh, took you long enough! Make sure it doesn't happen again! It... makes me so worried.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002155$
        # - Hey, our contract expires soon. You wouldn't want to forget and for me to go away, would you? Right??
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002156$
        # - Ugh, $OwnerName$... You're so dense...
        if pick == 0:
            # $script:0831180509002157$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002158$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002159$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002160$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509002161$
        # - Was there something else you needed?
        if pick == 0:
            # $script:0831180509002162$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002163$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002164$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002165$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509002166$
        # - If you're bored, why don't you help around the house?
        if pick == 0:
            # $script:0831180509002167$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002168$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002169$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002170$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509002171$
        # - There's a really good fish market in $map:02000111$. Maybe you should check it out.
        if pick == 0:
            # $script:0831180509002172$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002173$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002174$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002175$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509002177$
        # - Can't you even keep track of your own expenses, $OwnerName$? You've already paid me this month! Sheesh!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509002180$
        # - ...You can ask all you want, but I'm not going to craft anything for you right now.
        if pick == 0:
            # $script:0831180509002181$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002182$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002183$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509002184$
        # - I've got nothing to do. Maybe I should go visit $npcName:11000406[gender:0]$...
        if pick == 0:
            # $script:0831180509002185$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002186$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002187$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509002188$
        # - Did you just ask if I'm okay? You dummy, you know I'm not!
        if pick == 0:
            # $script:0831180509002189$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002190$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002191$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002193$
        # - Stop trying to change the subject! Our contract has expired. I warned you so many times, but you didn't listen! How are you still alive?!
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002194$
        # - It's been $MaidPassedDay$ since I was supposed to be paid. Any good news?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002195$
        # - Ugh, why do I even bother to ask?
        if pick == 0:
            # $script:0831180509002196$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002197$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002198$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509002199$
        # - $OwnerName$, I really don't know what you're thinking.
        if pick == 0:
            # $script:0831180509002200$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002201$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002202$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509002203$
        # - Maybe it's time we go our separate ways. I can't wait for you like this forever, you know. Maybe I should just go back to mom and help her with her business...
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509002204$
        # - We should've opened a bed and breakfast like I suggested. I can't believe things have gotten so bad that you can't even pay me.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509002205$
        # - Am I worried about you? N-no, why would I be? S-stop being delusional. A-and stop looking at me with those doe eyes!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002206$
        # - Sure, you've come to the best.
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002207$
        # - Maybe I should do this for a living.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002208$
        # - Wh-why are you staring at me like that?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002209$
        # - Was there something else you needed?
        if pick == 0:
            # $script:0831180509002210$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002211$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002212$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509002213$
        # - Was there something else you needed?
        if pick == 0:
            # $script:0831180509002214$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002215$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002216$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002217$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509002218$
        # - I wonder how my mom's shop is doing...
        if pick == 0:
            # $script:0831180509002219$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509002220$
            # - Tell me about $map:02000100$.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509002221$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509002222$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509002223$
        # - I know I'm here to help, but you can pick up your clothes at least!
        if pick == 0:
            # $script:0831180509002224$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509002225$
            # - Tell me about $map:02000100$.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509002226$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509002227$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509002228$
        # - I hate lazy people.
        if pick == 0:
            # $script:0831180509002229$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509002230$
            # - Tell me about $map:02000100$.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509002231$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509002232$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509002233$
        # - Was there something else you needed?
        if pick == 0:
            # $script:0831180509002234$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002235$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002236$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509002237$
        # - If you're bored, why don't you help around the house?
        if pick == 0:
            # $script:0831180509002238$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002239$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002240$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509002241$
        # - There's a really good fish market in $map:02000111$. Maybe you should check it out.
        if pick == 0:
            # $script:0831180509002242$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002243$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002244$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002245$
            # - I want to ask you something. I don't know if you know this, but my mom has a fish market in $map:02000111$.
            return 1000
        elif index == 1:
            # $script:0831180509002246$
            # - I've helped her with her business since I was young. Then suddenly, she says I should stop helping her and start doing what I want to do.
            return 1000
        elif index == 2:
            # $script:0831180509002247$
            # - But her shop hasn't been doing well, and she has no one else to help her. What do you think I should do, $OwnerName$?
            if pick == 0:
                # $script:0831180509002248$
                # - I really don't care.
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509002249$
                # - Listen to your mama and follow your heart.
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002250$
        # - Wh-what? You're such a jerk!
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002251$
        # - How can you treat me this way?!
        return -1

    def __1011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002252$
        # - You think so? I guess you're not useless after all, $OwnerName$. Hmm...
        return -1

    def __1012(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002253$
        # - I see. Thank you for your input.
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002254$
            # - Ugh, you're so helpless.
            return 1100
        elif index == 1:
            # $script:0831180509002255$
            # - Have you been to $map:02000137$? I run errands there for my mom. Recently the whole place has been turned upside down because of someone named $npcName:11000406[gender:0]$.
            return 1100
        elif index == 2:
            # $script:0831180509002256$
            # - I asked someone who $npcName:11000406[gender:0]$ was, and she rolled her eyes and told me I was an idiot. But I think she's the idiot. She cried and fainted when he showed up.
            if pick == 0:
                # $script:0831180509002257$
                # - You're totally right.
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509002258$
                # - It takes a lot of passion to care that much.
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002259$
        # - But maybe I shouldn't have called her an idiot to her face. That wasn't nice.
        return -1

    def __1102(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002260$
        # - I've got to admit, though, he was pretty handsome. Those eyes... That hair... Hmm, maybe I've got a thing for $npcName:11000406[gender:0]$ too...
        return -1

    def __1111(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002261$
        # - You have a point. Maybe I should try to understand what makes $npcName:11000406[gender:0]$ so popular.
        return -1

    def __1112(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509002262$
        # - Hmmm. I didn't think about it that way. Why do you think $npcName:11000406[gender:0]$ is so popular? It's really... kind of intriguing... Hmm...
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002263$
            # - Don't you think this house is too big for just two of us?
            return 2000
        elif index == 1:
            # $script:0831180509002264$
            # - How about we turn it into a bed and breakfast? $OwnerName$, you're almost never home, anyway. This will let us make extra money and meet new people!
            return 2000
        elif index == 2:
            # $script:0831180509002265$
            # - I'm not really asking for approval. I already posted an ad on a display in $map:02000100$. Teehee!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002266$
            # - Nothing really happened, but... $OwnerName$, what's this gash on your arm? Did a monster hurt you?
            return 2100
        elif index == 1:
            # $script:0831180509002267$
            # - ...Wh-what? Why are you staring at me like that? D-don't think I asked because I was worried about you!
            return 2100
        elif index == 2:
            # $script:0831180509002268$
            # - You're the one who pays me. Of course, I don't want you to get hurt. G-get it?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __3000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002269$
            # - I went to $map:02000100$ and saw a masked man. He was tall, had red eyes, and was clad in black from head to toe. $npcName:11000233[gender:1]$ said he might be the famous $npcName:11000529[gender:0]$.
            return 3000
        elif index == 1:
            # $script:0831180509002270$
            # - $OwnerName$, have you heard of $npcName:11000529[gender:0]$? No? Well, he just looked so different from everyone else. I want to know if the rumors about him are true!
            return 3000
        elif index == 2:
            # functionID=1 openTalkReward=True
            # $script:0831180509002271$
            # - Huh? You haven't heard the rumors? If you're so curious, then why don't you go to $map:02000100$ and find out yourself?
            return -1
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002272$
            # - Have you been to $map:02000153$? It's the stronghold of Dark Wind, an organization led by $npcName:11000044[gender:0]$.
            return 3100
        elif index == 1:
            # $script:0831180509002273$
            # - The organizations claims to protect the peace of $map:02000100$, but not everyone seems to agree.
            return 3100
        elif index == 2:
            # $script:0831180509002274$
            # - $npcName:11000233[gender:1]$ said things were much better when Dark Wind was led by its former captain. Mm, what was his name? Winn Stilton, I think?
            return 3100
        elif index == 3:
            # functionID=1 openTalkReward=True
            # $script:0831180509002275$
            # - What happened to him? I don't know exactly. I heard he died in an accident.
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002276$
            # - You'd know if you visited $map:02000100$ how rotten the whole city is.
            return 4000
        elif index == 1:
            # $script:0831180509002277$
            # - And that's not going to change until Goldus Group stops being so greedy. I have no faith in Dark Wind or the mayor.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002278$
            # - Have you been to $map:02000092$? The water there is no longer drinkable because of $map:02000084$.
            return 4100
        elif index == 1:
            # $script:0831180509002279$
            # - That's not the only problem. $map:02000111$ is infested with angry giant turtles who have been forced from their homes due to the contamination.
            return 4100
        elif index == 2:
            # $script:0831180509002280$
            # - Worse still, $map:02000138$ is a slum now. What's the mayor doing? He says he's making the city better, but why are people becoming poorer?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002281$
            # - Ugh! This guy named $npcName:11000362[gender:0]$ set up a stall right next to Mom's shop!
            return 5000
        elif index == 1:
            # $script:0831180509002282$
            # - He sells $itemPlural:30000140$, and it's totally affecting Mom's business!
            return 5000
        elif index == 2:
            # $script:0831180509002283$
            # - He could've bought some fish from Mom to put in his corn dogs, but nooooo. He doesn't care about anyone but himself!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002284$
            # - I wonder how Mrs. $npc:11000424[gender:1]$ is doing. If you go to $map:02000100$, could you send her my regards?
            return 5100
        elif index == 1:
            # $script:0831180509002285$
            # - Her only granddaughter is missing. I can't imagine how devastating it must be to her.
            return 5100
        elif index == 2:
            # $script:0831180509002286$
            # - Her name is Maggie, and she's a friend of mine. She was being treated in $map:02000071$ when she suddenly disappeared.
            return 5100
        elif index == 3:
            # $script:0831180509002287$
            # - Some time ago, I heard a strange rumor. Maggie had a doll that she loved, and a monster that looks just like her doll has shown up.
            return 5100
        elif index == 4:
            # $script:0831180509002288$
            # - A monster that resembles her doll... What do you think happened to Maggie?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002289$
            # - Right now, Mom and I are living in $map:02000111$. It was less than two years ago when we moved to where we are now, near $map:02000100$.
            return 6000
        elif index == 1:
            # $script:0831180509002290$
            # - We used to live in $map:02000062$. Mom said she decided to move to the big city for her business, but I know the truth: it was for my future.
            return 6000
        elif index == 2:
            # $script:0831180509002291$
            # - But I can't seem to get used to the dreary city life. The rich get richer and the poor get poorer. Everyone's too busy with their lives to care about anyone else. Sometimes, I miss the days when I lived in $map:02000062$.
            return 6000
        elif index == 3:
            # $script:0831180509002292$
            # - ...Gosh, wh-why am I even telling you this? Forget I said anything.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002293$
            # - This is embarrassing, but I haven't found my passion. I don't know what I want to do for the rest of my life.
            return 7000
        elif index == 1:
            # $script:0831180509002294$
            # - $npcName:11000788[gender:0]$ may be a big mouth, but he has a dream and that's to become an adventurer. $npc:11000406[gender:0]$ seems to have achieved his dream, which I guess is to become every girl's dream.
            return 7000
        elif index == 2:
            # $script:0831180509002295$
            # - As for me, I still don't know what I want to do or what I'm good at.
            return 7000
        elif index == 3:
            # $script:0831180509002296$
            # - I like helping my mom, but it doesn't fill the void inside me. And sometimes I envy others my age when I look at them.
            return 7000
        elif index == 4:
            # $script:0831180509002297$
            # - $OwnerName$, I never thought I'd talk to you like this. I feel better now that I got that off my chest.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509002298$
        # - Hello! Looking for a place to stay?
        if pick == 0:
            # $script:0831180509002299$
            # - Yep!
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509002300$
            # - Nope!
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509002301$
            # - What do you mean?
            # TODO: goto 105, 106
            return -1
        return -1
