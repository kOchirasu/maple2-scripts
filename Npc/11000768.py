""" 11000768: Growlie """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])


    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509001388$
        # - Don't make me work too hard.
        if pick == 0:
            # $script:0831180509001389$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001390$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001391$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509001392$
        # - What do you want?
        if pick == 0:
            # $script:0831180509001393$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001394$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001395$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509001396$
        # - Stop nagging me!
        if pick == 0:
            # $script:0831180509001397$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001398$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001399$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509001400$
        # - Don't make me work too hard.
        if pick == 0:
            # $script:0831180509001401$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001402$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001403$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001404$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509001405$
        # - What do you want?
        if pick == 0:
            # $script:0831180509001406$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001407$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001408$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001409$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509001410$
        # - Stop nagging me!
        if pick == 0:
            # $script:0831180509001411$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001412$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001413$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001414$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509001415$
        # - Huh? You want to pay me?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509001416$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001417$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001418$
        # - Paying your employees on time is a good practice. Keep up the good work.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001419$
        # - Now that I've been paid, I'm going to treat myself to a feast. I love to have food delivered to the house!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001420$
        # - Remember not to get behind on paying me. Ugh, I thought I was going to starve to death. Now that I have my paycheck, I'm going to order some pizza.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001421$
        # - I was going to leave if you didn't pay me by the end of the day. You're lucky you did.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001422$
        # - $OwnerName$, you should check the calendar sometimes. Our contract expires soon. You can't always be so busy that forget.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001423$
        # - Do I really have to remind you of this?
        if pick == 0:
            # $script:0831180509001424$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001425$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001426$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001427$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509001428$
        # - Aw man, that nap hit the spot.
        if pick == 0:
            # $script:0831180509001429$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001430$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001431$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001432$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509001433$
        # - Acting friendly isn't going to get you anything.
        if pick == 0:
            # $script:0831180509001434$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001435$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001436$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001437$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509001438$
        # - Don't talk to me. I don't want to do anything right now.
        if pick == 0:
            # $script:0831180509001439$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001440$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001441$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001442$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509001444$
        # - You already paid me for this month. And just because I look tough doesn't mean I'm a chat. Sheesh, $OwnerName$, who do you think I am?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509001447$
        # - What's up? 
        if pick == 0:
            # $script:0831180509001448$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001449$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001450$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509001451$
        # - I'm too hungry to talk.
        if pick == 0:
            # $script:0831180509001452$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001453$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001454$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509001455$
        # - I told you, I'm not going to work unless you pay me.
        if pick == 0:
            # $script:0831180509001456$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001457$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001458$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001461$
        # - I haven't eaten for $MaidPassedDay$! My clothes are practically falling off!
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001462$
        # - $OwnerName$, why are you doing this to me?
        if pick == 0:
            # $script:0831180509001463$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001464$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001465$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509001466$
        # - It's not like I'm asking for a raise... Ugh.
        if pick == 0:
            # $script:0831180509001467$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509001468$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001469$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509001470$
        # - I need a meal, a real meal. Not a snack, but a full on, three course meal!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509001471$
        # - Are you torturing me because I grumble sometimes? But I still clean and do everything you ask. Why aren't you paying me? If you don't pay me, why, I'll... I'll... I'll go on strike! I mean it!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509001472$
        # - You can't take home groceries until you've paid for them first, right? Same with my services. You have to pay for them first!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001473$
        # - Nobody compares to me when it comes to alchemy!
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001474$
        # - You just let old $MaidName$ handle your potion-making.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001475$
        # - Why are you asking so many personal questions?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001476$
        # - Stop asking the same questions over and over.
        if pick == 0:
            # $script:0831180509001477$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001478$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001479$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509001480$
        # - Stop asking the same questions over and over.
        if pick == 0:
            # $script:0831180509001481$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001482$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001483$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509001484$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509001485$
        # - When are you going to buy me some snacks?
        if pick == 0:
            # $script:0831180509001486$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509001487$
            # - (Scold.)
            # TODO: goto 3000, 3100, 4000, 4100, 4200, 4300, 9011
            return -1
        elif pick == 2:
            # $script:0831180509001488$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509001489$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509001490$
        # - Why? What? What happened?
        if pick == 0:
            # $script:0831180509001491$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509001492$
            # - (Scold.)
            # TODO: goto 3000, 3100, 4000, 4100, 4200, 4300, 9011
            return -1
        elif pick == 2:
            # $script:0831180509001493$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509001494$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509001495$
        # - $OwnerName$, what's the good news?
        if pick == 0:
            # $script:0831180509001496$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 1200, 1300, 1400, 1500, 1600, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509001497$
            # - (Scold.)
            # TODO: goto 3000, 3100, 4000, 4100, 4200, 4300, 9011
            return -1
        elif pick == 2:
            # $script:0831180509001498$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509001499$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509001500$
        # - Aw man, that nap hit the spot.
        if pick == 0:
            # $script:0831180509001501$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001502$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001503$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509001504$
        # - Acting friendly isn't going to get you anything.
        if pick == 0:
            # $script:0831180509001505$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001506$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001507$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509001508$
        # - Don't talk to me. I don't want to do anything right now.
        if pick == 0:
            # $script:0831180509001509$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001510$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001511$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001512$
            # - Hey, $OwnerName$.
            return 1000
        elif index == 1:
            # $script:0831180509001513$
            # - I just had this delivered, and I don't like it. You can eat it if you want. 
            return 1000
        elif index == 2:
            # $script:0831180509001514$
            # - It's a bit cold by now, though.
            if pick == 0:
                # $script:0831180509001515$
                # - Ugh, it's too cold!
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509001516$
                # - It's delicious!
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001521$
            # - It's exhausting taking care of you...
            return 1100
        elif index == 1:
            # $script:0831180509001522$
            # - $OwnerName$, I'd like to offer you my leftover snacks from yesterday. They're a bit stale, but you can eat them if you want.
            return 1100
        elif index == 2:
            # $script:0831180509001523$
            # - If you eat even a bite, I expect you to get me more delicious snacks in return.
            if pick == 0:
                # $script:0831180509001524$
                # - I bought you snacks yesterday!
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509001525$
                # - Sure.
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __1200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001530$
            # - Whew, it's hot in here. Take this cool drink to refresh yourself.
            return 1200
        elif index == 1:
            # $script:0831180509001531$
            # - Don't you think it's like an oven in here?
            if pick == 0:
                # $script:0831180509001532$
                # - Thanks for the drink! Just what I needed.
                # TODO: goto 1211, 1212
                return -1
            elif pick == 1:
                # $script:0831180509001533$
                # - Actually, I'm freezing...
                # TODO: goto 1201, 1202
                return -1
            return -1
        return -1

    def __1300(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001538$
            # - $npcName:11000002[gender:1]$ gave me some of food he cooked, but I don't think I like it. Taste it.
            return 1300
        elif index == 1:
            # $script:0831180509001539$
            # - How does it taste? Well? Well??
            if pick == 0:
                # $script:0831180509001540$
                # - It's delicious!
                # TODO: goto 1311, 1312
                return -1
            elif pick == 1:
                # $script:0831180509001541$
                # - Did you remember to thank $npcName:11000002[gender:1]$?
                # TODO: goto 1301, 1302
                return -1
            return -1
        return -1

    def __1400(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001546$
            # - $OwnerName$, I found this while napping inside the storage chest.
            return 1400
        elif index == 1:
            # $script:0831180509001547$
            # - Is it yours?
            if pick == 0:
                # $script:0831180509001548$
                # - Never seen it before. Nooo idea whose it could be...
                # TODO: goto 1401, 1402
                return -1
            elif pick == 1:
                # $script:0831180509001549$
                # - Yup, it's mine.
                # TODO: goto 1411, 1412
                return -1
            return -1
        return -1

    def __1500(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001554$
            # - I found this while playing in $map:2000001$. Your house is too empty. Use it to decorate a bit more.
            return 1500
        elif index == 1:
            # $script:0831180509001555$
            # - Make the house more comfortable for me, all right?
            if pick == 0:
                # $script:0831180509001556$
                # - Sure.
                # TODO: goto 1511, 1512
                return -1
            elif pick == 1:
                # $script:0831180509001557$
                # - I like the minimalist look.
                # TODO: goto 1501, 1502
                return -1
            return -1
        return -1

    def __1600(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001562$
            # - I found this between the sheets of your bed.
            return 1600
        elif index == 1:
            # $script:0831180509001563$
            # - Did you lose it?
            if pick == 0:
                # $script:0831180509001564$
                # - What were you doing on my bed?
                # TODO: goto 1601, 1602
                return -1
            elif pick == 1:
                # $script:0831180509001565$
                # - Thank you.
                # TODO: goto 1611, 1612
                return -1
            return -1
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001570$
            # - Stop trying to tell me how I do my job, and just go out there and... do whatever it is that you do!
            return 2000
        elif index == 1:
            # $script:0831180509001571$
            # - The house is so dusty because you keep tracking in dirt!
            return 2000
        elif index == 2:
            # $script:0831180509001572$
            # - I just don't understand why you're so dirty. Stop fooling around and take a shower!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001573$
            # - One of your friends stopped by but left without giving me a name.
            return 2100
        elif index == 1:
            # $script:0831180509001574$
            # - I didn't ask because... I didn't think of it, okay?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001575$
            # - I don't feel like doing anything today. If you insist that I pick something to do, I choose to lie down and rest.
            return 2200
        elif index == 1:
            # $script:0831180509001576$
            # - What do you mean resting isn't work? Of course it is! It involves thinking!
            return 2200
        elif index == 2:
            # $script:0831180509001577$
            # - I have to think real hard about what snacks I should eat today, tomorrow, the rest of the week... That stuff is really important to me!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001582$
            # - Stop harassing me or I'll quit, I mean it!
            return 4000
        elif index == 1:
            # $script:0831180509001583$
            # - If I quit, you won't have anyone to keep your house clean. It doesn't just clean itself, you know?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001584$
            # - Enough is enough!
            return 4100
        elif index == 1:
            # $script:0831180509001585$
            # - Argh! Why do you treat me like this? I just want to be happy and take naps. Is that too much to ask?
            return 4100
        elif index == 2:
            # $script:0831180509001586$
            # - Why can't you just let me be happy?! Don't you think I deserve it?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001587$
            # - I came to $map:2000001$ for $npc:11000075[gender:1]$'s event. I've always been in love with $npc:11000075[gender:1]$, ever since I was little. I even dream about her sometimes.
            return 5000
        elif index == 1:
            # $script:0831180509001588$
            # - I fell in love with the $npc:11000075[gender:1]$ because of a book. She was illustrated as a character in it, and the moment I saw the picture, that was it for me.
            return 5000
        elif index == 2:
            # $script:0831180509001589$
            # - I came to $map:2000001$ to see the love of my life, $npc:11000075[gender:1]$, but then the ceremony was canceled.
            return 5000
        elif index == 3:
            # $script:0831180509001590$
            # - I was so desperate to see her, I sprinted toward the palace. All I wanted was a glance. Instead, $npc:11000119[gender:0]$ appeared.
            return 5000
        elif index == 4:
            # $script:0831180509001591$
            # - I tried to shove past him, but he tripped me. Can you believe that? Who is he to stop me from seeing her?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001592$
            # - I accepted this job because it's the best! I get to live in someone else's house, eat their food, sleep in their bed, and I even get paid! All I have to do in return is a bit of cleaning.
            return 5100
        elif index == 1:
            # $script:0831180509001593$
            # - But the cleaning part isn't as easy as you'd think.
            return 5100
        elif index == 2:
            # $script:0831180509001594$
            # - Dust bunnies lurk in every corner. As soon as you sweep, the dust scatters.
            return 5100
        elif index == 3:
            # $script:0831180509001595$
            # - And where do you think that dust goes? Your bed! The bathroom sink! Between the cracks of the living room floor! And the it's back to square one for me.
            return 5100
        elif index == 4:
            # $script:0831180509001596$
            # - Now if I just leave the dust bunnies where they are, what do you think happens? They accumulate until they grow so big, you can just pluck them away. So you see, the less you clean, the better.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001597$
            # - Ever wonder why I complain so much? I wasn't always like this, you know. The world has made me what I am.
            return 6000
        elif index == 1:
            # $script:0831180509001598$
            # - Everyone I've met has been mean to me. I tried to be nice to them, but all I got back was bullying and name-calling.
            return 6000
        elif index == 2:
            # $script:0831180509001599$
            # - You don't have to be nice to others, $OwnerName$. They'll only hurt you, no matter how nice you are to them.
            return 6000
        elif index == 3:
            # $script:0831180509001600$
            # - Don't show the world your weaknesses. You'll always regret it.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509001601$
            # - Have you met $npcName:22000002[gender:0]$? I used to be good friends with him.
            return 7000
        elif index == 1:
            # $script:0831180509001602$
            # - He's not the sharpest, but he's stronger than anyone else I know. Let me tell you a story about him and $npcName:11000002[gender:1]$.
            return 7000
        elif index == 2:
            # $script:0831180509001603$
            # - $npcName:11000002[gender:1]$ has loved cooking since she was young. She was always searching for ingredients. One day, she went to $map:2000043$ even though the grownups told her not to. She was climbing a hill, when suddenly the ground shook and a big rock came rolling straight toward her!
            return 7000
        elif index == 3:
            # $script:0831180509001604$
            # - She was so scared that she fainted. $npcName:22000002[gender:0]$ saw what was happening, leapt over, and shattered the rock with a single punch! He saved $npcName:11000002[gender:1]$. That's how strong $npcName:22000002[gender:0]$ is.
            return 7000
        elif index == 4:
            # $script:0831180509001605$
            # - $npcName:11000002[gender:1]$ thinks $npcName:11000055[gender:0]$'s father saved her, but I saw it all. He used to be so nice when he was young. I don't know what changed him over the years.
            return 7000
        elif index == 5:
            # $script:0831180509001606$
            # - Huh? What was I doing in $map:2000043$? That's none of your business!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509001607$
        # - <font color="#909090">(He wipes crumbs away from his mouth.)</font>
        #   Who are you? You friends with my boss?
        if pick == 0:
            # $script:0831180509001608$
            # - Yep!
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509001609$
            # - Nope!
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509001610$
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
