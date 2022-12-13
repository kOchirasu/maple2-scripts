""" 11000759: Michael """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509000706$
        # - $OwnerName$, what is it this time?
        if pick == 0:
            # $script:0831180509000707$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000708$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000709$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509000710$
        # - Very well. I was just taking a break.
        if pick == 0:
            # $script:0831180509000711$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000712$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000713$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509000714$
        # - Oh, I didn't see you there. I was just... thinking. What can I do for you?
        if pick == 0:
            # $script:0831180509000715$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000716$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000717$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509000718$
        # - $OwnerName$, what is it this time?
        if pick == 0:
            # $script:0831180509000719$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000720$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000721$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000722$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509000723$
        # - Very well. I was just taking a break.
        if pick == 0:
            # $script:0831180509000724$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000725$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000726$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000727$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509000728$
        # - Oh, I didn't see you there. I was just... thinking. What can I do for you?
        if pick == 0:
            # $script:0831180509000729$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000730$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000731$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000732$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509000733$
        # - Hm, my paycheck, huh?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509000734$
            # - Never mind.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000735$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000736$
        # - You're paying me early. $OwnerName$, you like to get things done efficiently, don't you. You're my favorite kind of boss.
        #   <font color="#909090">(He chuckles softly.)</font>
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000737$
        # - Here I was, thinking our time together was about to come to an end. I guess not.
        #   <font color="#909090">(He chuckles.)</font>
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000738$
        # - I thought our contract had expired, though I suppose if you're that desperate to keep me, I can serve you for a little longer.
        #   <font color="#909090">(He chuckles.)</font>
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000739$
        # - <font color="#909090">(He chuckles.)</font>
        #   You've changed your mind? I won't say I'm happy, but I will agree to renew our contract. My own plans will be put on hold for a little longer.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000740$
        # - It doesn't matter to me, but our contract expires soon. I just want you to know you'll have to pay me if you want me to continue working for you.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000741$
        # - Our relationship is strictly business. We don't have to get emotional.
        if pick == 0:
            # $script:0831180509000742$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000743$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000744$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000745$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509000746$
        # - Sigh... What is it now?
        if pick == 0:
            # $script:0831180509000747$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000748$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000749$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000750$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509000751$
        # - Keep bothering me, and I might just tie you to a pole.
        if pick == 0:
            # $script:0831180509000752$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000753$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000754$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000755$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509000756$
        # - Why, aren't you mischievous, $OwnerName$!
        #   <font color="#909090">(He chuckles softly.)</font>
        if pick == 0:
            # $script:0831180509000757$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000758$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000759$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000760$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509000762$
        # - Tsk, $OwnerName$. You've already paid me for the month. Perhaps I should've just accepted the mesos. It would have been delightful to see you in tears later. 
        #   <font color="#909090">(He chuckles softly.)</font>
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509000765$
        # - What are you doing? Don't you know that our contract has expired?
        if pick == 0:
            # $script:0831180509000766$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000767$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000768$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509000769$
        # - I have no more business with you.
        if pick == 0:
            # $script:0831180509000770$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000771$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000772$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509000773$
        # - Hm... You're bothering me.
        if pick == 0:
            # $script:0831180509000774$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000775$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000776$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000778$
        # - We had a business arrangement. That does not make us friends. Our contract has expired. Get it? Then leave me alone.
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000779$
        # - You're a pest.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000780$
        # - I'd prefer not to share personal details of my life with you.
        if pick == 0:
            # $script:0831180509000781$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000782$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000783$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509000784$
        # - You're quite thick-headed sometimes, aren't you?
        if pick == 0:
            # $script:0831180509000785$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000786$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000787$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509000788$
        # - If you don't wish to employ me, why keep me around in your house? What are you up to?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509000789$
        # - I'm not sure what you're thinking, but our contract has expired. Or... was there something besides your house that you wanted me to take care of? If so, I don't think you can handle it.
        #   <font color="#909090">(He chuckles.)</font>
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509000790$
        # - Now that our contract has expired, I'm no longer obligated to chat with you. Well, well. It's been a long time since someone has thrown me such a dirty look. 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000791$
        # - Is there something you need?
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000792$
        # - Simple.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000793$
        # - Knowing more about me won't change anything between us.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000794$
        # - Please let me focus on my work.
        if pick == 0:
            # $script:0831180509000795$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000796$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000797$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000798$
        # - Please let me focus on my work.
        if pick == 0:
            # $script:0831180509000799$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000800$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000801$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000802$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509000803$
        # - Tell me. I'm at your service... for now.
        if pick == 0:
            # $script:0831180509000804$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509000805$
            # - I don't feel so good. I'm sick.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509000806$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509000807$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509000808$
        # - I wasn't aware chit chat was part of my job description.
        if pick == 0:
            # $script:0831180509000809$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509000810$
            # - I don't feel so good. I'm sick.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509000811$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509000812$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509000813$
        # - Shouldn't you be talking to someone who actually cares?
        if pick == 0:
            # $script:0831180509000814$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509000815$
            # - I don't feel so good. I'm sick.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509000816$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509000817$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509000818$
        # - Sigh... What is it now?
        if pick == 0:
            # $script:0831180509000819$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000820$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000821$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509000822$
        # - Keep bothering me, and I might just tie you to a pole.
        if pick == 0:
            # $script:0831180509000823$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000824$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000825$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509000826$
        # - Why, aren't you mischievous, $OwnerName$!
        #   <font color="#909090">(He chuckles softly.)</font>
        if pick == 0:
            # $script:0831180509000827$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000828$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000829$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000830$
            # - A servant is here to take care of your house, not to be your personal slave.
            return 1000
        elif index == 1:
            # $script:0831180509000831$
            # - Why are you giving me that look? It's all written clearly in the contract.
            if pick == 0:
                # $script:0831180509000832$
                # - What did I do that was so bad?
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509000833$
                # - I'm sorry. I'll stop. I promise.
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000834$
        # - You forgot your potions when you left the house last week and made me deliver them. All the way to $map:02000216$, no less!
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000835$
        # - Don't feign ignorance. You're not that dumb. Now, I have work the requires my complete focus, so please don't speak to me.
        return -1

    def __1011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000836$
        # - That sheepish expression you're making right now... Surprisingly, I don't despise it.
        #   <font color="#909090">(He gives a soft chuckle.)</font>
        return -1

    def __1012(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000837$
        # - Hmm. A surprisingly sensible response. I didn't expect that from you.
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000838$
            # - Why are you furrowing your brows at me? Do you think I'm going to steal something?
            return 1100
        elif index == 1:
            # $script:0831180509000839$
            # - That's something all my previous employers had in common. They always wanted to know what I was up to.
            return 1100
        elif index == 2:
            # $script:0831180509000840$
            # - What about you, $OwnerName$? Do you think I'm hiding something?
            if pick == 0:
                # $script:0831180509000841$
                # - You have to admit you give off a suspicious aura.
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509000842$
                # - Nah, none of my business.
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000843$
        # - You're no better than the rest of them. If you don't trust me, you don't need to employ me.
        return -1

    def __1102(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000844$
        # - Heh, but you'll never unravel the truth, no matter how much you try.
        return -1

    def __1111(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000845$
        # - You sure about that? I doubt you'd say that if you knew who I really am...
        return -1

    def __1112(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000846$
        # - You say that, yet I see the doubt in your eyes. Speaking of which, $OwnerName$, I never knew your eyes had such sparkle. Oops, almost said something I'd regret later.
        #   <font color="#909090">(He chuckles softly.)</font>
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000847$
            # - Strangers barge into your home several times a day. It doesn't feel safe. We should install locks on the doors.
            return 2000
        elif index == 1:
            # $script:0831180509000848$
            # - Don't give me that look, $OwnerName$. I'm not trying to do anything unsightly behind locked doors.
            return 2000
        elif index == 2:
            # $script:0831180509000849$
            # - There's just... something I want to study in peace and quiet. It doesn't concern you.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000850$
            # - We need some music to liven things up around here. What? I like listening to music, just like everyone else.
            return 2100
        elif index == 1:
            # $script:0831180509000851$
            # - Let's see... Judging by how you've decorated your home, it seems you have quite elegant taste, $OwnerName$. Let's play some jazz.
            return 2100
        elif index == 2:
            # $script:0831180509000852$
            # - That's also my favorite genre of music. Which reminds me, there's a pretty famous musician who hangs out in $map:02000076$. Maybe I should ask for an autograph.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __3000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000853$
            # - You're sick? With what? ...You have no fever. Your heart rate is normal.
            return 3000
        elif index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509000854$
            # - Ah, you're pretending, aren't you? All right, I'll feign ignorance just this once. Come over here and lie down.
            return -1
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000855$
            # - You were bitten by a $npcName:21000023$? Come here. Let me take a look...
            return 3100
        elif index == 1:
            # $script:0831180509000856$
            # - Ah, this is bad. It's hard to treat rabies. I'm sorry, but there's nothing I can do that will make a difference  at this point.
            return 3100
        elif index == 2:
            # $script:0831180509000857$
            # - <font color="#909090">(He chuckles.)</font>
            #   Look at you, about to burst into tears.
            return 3100
        elif index == 3:
            # functionID=1 openTalkReward=True 
            # $script:0831180509000858$
            # - I was joking. Now, come over here. A little bit of iodine, and you'll be as good as new.
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000859$
            # - Where does it hurt? Show me.
            return 4000
        elif index == 1:
            # $script:0831180509000860$
            # - ...Why would you lie about being sick? $OwnerName$, you're hopeless.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000861$
            # - ...Again? Please stop acting like a child.
            return 4100
        elif index == 1:
            # $script:0831180509000862$
            # - You shouldn't make things up and make others worry about you. It's not kind.
            return 4100
        elif index == 2:
            # $script:0831180509000863$
            # - Am I going to have to scold you? Because if you pull this again, I will.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000864$
            # - I don't like talking about myself. It's not a problem, because I have no friend to talk to anyway.
            return 5000
        elif index == 1:
            # $script:0831180509000865$
            # - At least, not any more. My only friend passed away a long time ago.
            return 5000
        elif index == 2:
            # $script:0831180509000866$
            # - He got into an accident... Actually, it's not of your business, really.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000867$
            # - The story of how I learned alchemy is quite uninteresting.
            return 5100
        elif index == 1:
            # $script:0831180509000868$
            # - I met a grungy old beggar in $map:02000051$. He was rather fastidious and pompous for a beggar.
            return 5100
        elif index == 2:
            # $script:0831180509000869$
            # - But something about him seemed... powerful.
            return 5100
        elif index == 3:
            # $script:0831180509000870$
            # - When there's something I want, nothing can get in my way. I told him I wanted to learn how to beg, and he taught me. In the meantime, I stood at his side and learned his alchemy secrets over his shoulder.
            return 5100
        elif index == 4:
            # $script:0831180509000871$
            # - And look at me now. I'm as good an alchemist as he is.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000872$
            # - Do you know what I fear the most? Death.
            return 6000
        elif index == 1:
            # $script:0831180509000873$
            # - Everyone fears death, and just about everyone succumbs to death eventually.
            return 6000
        elif index == 2:
            # $script:0831180509000874$
            # - But not me. I'm going to beat death, just like I've beaten everything else...
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000875$
            # - You've heard me mention my friend, have you not? He was the only person I could really talk to.
            return 7000
        elif index == 1:
            # $script:0831180509000876$
            # - He's no longer here. He may not actually be dead. Instead, he's... in another world.
            return 7000
        elif index == 2:
            # $script:0831180509000877$
            # - He and I ventured in the Shadow World when we were young. We got separated after a while.
            return 7000
        elif index == 3:
            # $script:0831180509000878$
            # - We shouldn't have been there at all, but we were dumb and reckless. When I came to, he was gone. I wouldn't had made it at all if I hadn't met those merchants...
            return 7000
        elif index == 4:
            # $script:0831180509000879$
            # - I may not be able to do much, but once in a while, I venture into the Shadow World to search for him. But I haven't heard a word, not even a rumor. Perhaps it's time to just let him go...
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509000880$
        # - Who are you? You should leave while I'm still in a pleasant mood.
        if pick == 0:
            # $script:0831180509000881$
            # - Yeah, okay, I'm out of here.
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509000882$
            # - Oh, yeah? What happens when you're unpleasant?
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509000883$
            # - What's your sign? Can I get your number?
            # TODO: goto 105, 106
            return -1
        return -1

