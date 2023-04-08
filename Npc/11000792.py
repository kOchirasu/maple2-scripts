""" 11000792: Jorge """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509005428$
        # - You're back. What do you need?
        if pick == 0:
            # $script:0831180509005429$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005430$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005431$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509005432$
        # - What can I do for you this time?
        if pick == 0:
            # $script:0831180509005433$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005434$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005435$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509005436$
        # - What is it? Do you need help?
        if pick == 0:
            # $script:0831180509005437$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005438$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005439$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509005440$
        # - You're back. What do you need?
        if pick == 0:
            # $script:0831180509005441$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005442$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005443$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005444$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509005445$
        # - What can I do for you this time?
        if pick == 0:
            # $script:0831180509005446$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005447$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005448$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005449$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509005450$
        # - What is it? Do you need help?
        if pick == 0:
            # $script:0831180509005451$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005452$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005453$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005454$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509005455$
        # - Are you going to pay me?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509005456$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005457$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509005458$
        # - Oh, you're paying me ahead of schedule. I appreciate it. Do humans label this type of behavior diligent or impatient?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509005459$
        # - Most currencies are shiny, and fairies love shiny things. Maybe that's why I'm in such a good mood.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509005460$
        # - A-ha, has our contract been renewed? Good timing. I had just gotten adequate rest. Thank you for hiring me again.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509005461$
        # - Ah, is it time for me to play house again? Good, I was getting bored. Humans call fairies fickle, but I think humans are far worse. What do you think?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005462$
        # - Our contract will expire in a few days. Did you know that? Of course, $OwnerName$, you know your schedule better than I do, but I thought I'd give you a reminder.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005463$
        # - By the way, I appreciate your checking my profile.
        if pick == 0:
            # $script:0831180509005464$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005465$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005466$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005467$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509005468$
        # - Was there something else you wanted?
        if pick == 0:
            # $script:0831180509005469$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005470$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005471$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005472$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509005473$
        # - What can I do for you this time?
        if pick == 0:
            # $script:0831180509005474$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005475$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005476$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005477$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509005478$
        # - Do you need help again?
        if pick == 0:
            # $script:0831180509005479$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005480$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005481$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005482$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509005484$
        # - Hmm? What day is it? If memory serves, we have at least a month left on our current contract. Would you like to go verify that information?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509005487$
        # - I'll consider this time off as... a vacation?
        if pick == 0:
            # $script:0831180509005488$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005489$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005490$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509005491$
        # - Hm, what a strange point of view! Huh? Oh, I'm referring to the author of this book.
        if pick == 0:
            # $script:0831180509005492$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005493$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005494$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509005495$
        # - Hm... I can't believe this theory... Oh, sorry. Did you call me?
        if pick == 0:
            # $script:0831180509005496$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005497$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005498$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005500$
        # - Wait, we shouldn't talk about that right now. Did you know our contract expired? And I'm not only bringing that up to avoid talking to you.
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005501$
        # - Huh? You and your obsession with my profile. I told you, this profile cannot capture even a 0.0000000000...0001 of who I am.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005502$
        # - Ah... Let's not talk about this anymore. I don't want to argue.
        if pick == 0:
            # $script:0831180509005503$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005504$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005505$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509005506$
        # - I'd like to focus on what I'm reading. Please don't disturb me unless it's important.
        if pick == 0:
            # $script:0831180509005507$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005508$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005509$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005510$
            # - I've seen many humans try to change their destinies. Most drive themselves to ruin, blaming anyone but themselves on the way. No, no, I'm not calling you irresponsible, $OwnerName$.
            return 9030
        elif index == 1:
            # $script:0831180509005511$
            # - I'm trying to encourage to take control of your life and choices. You have such a short, short life, but it's still full of choices.
            # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
            return -1
        return -1

    def __9031(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005512$
            # - Why are you asking me about the contract renewal? If you want to do it, then do it. If not, don't. You are in control of that, because you're the one with the money.
            return 9031
        elif index == 1:
            # $script:0831180509005513$
            # - I remember how shocked I was when I first learned about Helping Hands. I couldn't believe someone came up with such a one-sided, unreasonable system.
            return 9031
        elif index == 2:
            # $script:0831180509005514$
            # - Why am I here despite my abhorrence of the system? Foremost, because I've met a human to whom I can relate and am interested in knowing. But initially, it was purely out of curiosity.
            return 9031
        elif index == 3:
            # $script:0831180509005515$
            # - Are you wondering if the human I'm referring to is you? No comment. The point is, the time I spend here is only a fraction of my lifespan, so you can do whatever you want, $OwnerName$.
            # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
            return -1
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509005516$
        # - Fairies have this impression that humans are high maintenence. It wasn't until after I started working here—no actually, it wasn't until after our contract expired and I was forced to rest—that I realized how true that is.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005517$
        # - Need a potion?
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005518$
        # - Just tell me what you need, and I'll do the best I can.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005519$
        # - My profile won't reveal how I've lived my life...
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005520$
        # - Curious about my past? But that has nothing to do with my job.
        if pick == 0:
            # $script:0831180509005521$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005522$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005523$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509005524$
        # - Curious about my past? But that has nothing to do with my job.
        if pick == 0:
            # $script:0831180509005525$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005526$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005527$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005528$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509005529$
        # - You want to talk to me. Sure, what do you want to talk about?
        if pick == 0:
            # $script:0831180509005530$
            # - (Ask a difficult question.)
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509005531$
            # - (Request an old story.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509005532$
            # - (Talk about a personal topic.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509005533$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509005534$
        # - I've been around a long time, $OwnerName$. Maybe my experience can help.
        if pick == 0:
            # $script:0831180509005535$
            # - (Ask a difficult question.)
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509005536$
            # - (Request an old story.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509005537$
            # - (Talk about a personal topic.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509005538$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509005539$
        # - We can talk, but don't ask anything too personal.
        if pick == 0:
            # $script:0831180509005540$
            # - (Ask a difficult question.)
            # TODO: goto 1000, 1100, 2000, 2100, 9011
            return -1
        elif pick == 1:
            # $script:0831180509005541$
            # - (Request an old story.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509005542$
            # - (Talk about a personal topic.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509005543$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509005544$
        # - Was there something else you wanted?
        if pick == 0:
            # $script:0831180509005545$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005546$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005547$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509005548$
        # - What can I do for you this time?
        if pick == 0:
            # $script:0831180509005549$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005550$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005551$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509005552$
        # - Do you need help again?
        if pick == 0:
            # $script:0831180509005553$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005554$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005555$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005556$
            # - "Why do fairies live so much longer than humans," hmm? An excellent question. The secret to our longevity isn't quite what popular opinion would lead you to believe.
            return 1000
        elif index == 1:
            # $script:0831180509005557$
            # - Most believe our ability to commune with nature grants us a regenerative ability that slows aging.
            return 1000
        elif index == 2:
            # $script:0831180509005558$
            # - That's not quite right. The answer is actually because we are embodiments of nature herself. We live long lives the same way trees live for millennia and turtles live for centuries.
            return 1000
        elif index == 3:
            # $script:0831180509005559$
            # - As for why humans can't, it's simple. You refuse to submit to nature. You've decided to change your destinies. And that's why you and I have drastically different natural lifespans.
            return 1000
        elif index == 4:
            # $script:0831180509005560$
            # - Does that answer your question?
            if pick == 0:
                # $script:0831180509005561$
                # - That's absurd!
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509005562$
                # - Yup!
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509005563$
        # - Just because you don't understand it doesn't make it untrue... Now you've upset me.
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509005564$
        # - I didn't expect you to fully understand, but I didn't expect you to react quite like this, $OwnerName$.
        return -1

    def __1011(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005565$
            # - Oh, you understood all that? Your comprehension skills are better than I estimated. I think I can come to enjoy conversing with you.
            return 1011
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509005566$
            # - If you have other questions, you may ask them, but try to space it out, okay?
            return -1
        return -1

    def __1012(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005567$
            # - $OwnerName$, why don't you ask yourself a question. For example, whether humans did the right thing in rejecting nature? That's rather philosophical, don't you think?
            return 1012
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509005568$
            # - Ah, look at the time! I talked for longer than I thought. Well, that's because I enjoyed our conversation.
            return -1
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005569$
            # - Why is the sea such a pretty blue? Are you looking for the scientific answer or the poetic one? I can't speak to why you think blue is pretty, so I'll answer the scientific question instead.
            return 1100
        elif index == 1:
            # $script:0831180509005570$
            # - When light hits the sea, all light waves except the one that our eye interpret as the color blue is absorbed into the water. Do you understand? Similarly, red roses only reflect the red ray, which is why they look red.
            if pick == 0:
                # $script:0831180509005571$
                # - Do you really believe that? Truly?
                # TODO: goto 1111, 1112
                return -1
            elif pick == 1:
                # $script:0831180509005572$
                # - I disagree with you.
                # TODO: goto 1101, 1102
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005573$
            # - Then what is your opinion, $OwnerName$? Debate begins with a difference of opinion, and they often result in enlightenment and shifts in perspective.
            return 1101
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509005574$
            # - So... you think the sea is blue because fairies painted it blue? Do you... really believe that? Well, let's not talk about it, then. I don't wish to argue.
            return -1
        return -1

    def __1102(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005575$
            # - Interesting. It's a pretty simple and well-known scientific fact, but you disagree. Well, what's your theory, $OwnerName$?
            return 1102
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509005576$
            # - You don't know? But how can you disagree if you don't have your own idea of what the answer is? This conversation is nonsense.
            return -1
        return -1

    def __1111(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005577$
            # - What I just explained is the most well-accepted theory, but explaining nature with science can be harsh on your spirit and soul. Truth be told, I have a different idea.
            return 1111
        elif index == 1:
            # $script:0831180509005578$
            # - In my heart, I believe that the sea is blue because it saw that the sky was beautiful and wanted to emulate it. Or because it's a mirror to the sky's own beauty. Or maybe, the sky touched the sea once, staining it forever...
            return 1111
        elif index == 2:
            # functionID=1 openTalkReward=True
            # $script:0831180509005579$
            # - I know that such theories aren't science. But still, they bring me joy. I hope you'll remember that, $OwnerName$.
            return -1
        return -1

    def __1112(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005580$
            # - Scientific facts are not based on belief. They're facts. Absolute. But I like that you asked that question. It shows you don't want to see the world through the lens of pure fact.
            return 1112
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509005581$
            # - That type of mental flexibility will help you grow as a person, $OwnerName$. Trust me. I have an eye for that kind of stuff.
            return -1
        return -1

    def __2000(self, index: int, pick: int) -> int:
        # $script:0831180509005582$
        # - You have another question? Am I your walking encyclopedia? I'm sorry, but I'm in the middle of something. Maybe next time.
        # TODO: gotoConditionTalkID 30, 31, 32, 9011
        return -1

    def __2100(self, index: int, pick: int) -> int:
        # $script:0831180509005583$
        # - I'm sorry, but I don't have time to answer a question right now. As you can clearly see, I'm very busy. This isn't because I don't know the answer...
        # TODO: gotoConditionTalkID 30, 31, 32, 9011
        return -1

    def __3000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005584$
            # - This is a story from so long ago that even history doesn't known when it happened. It's from a time when fairies could speak to the stars, wind, and moon. I wasn't there personally. This is a tale known to all fairies who love reading.
            return 3000
        elif index == 1:
            # $script:0831180509005585$
            # - It is about a male fairy, his sister, and an evil witch.
            #   <font color="#909090">(He goes on and on, summarizing the story from a historian's perspective.)</font>
            return 3000
        elif index == 2:
            # $script:0831180509005586$
            # - <font color="#909090">(He goes into a lot of boring details and even the exciting moments are dragged down by his unnecessary analyses.)</font>
            return 3000
        elif index == 3:
            # functionID=1 openTalkReward=True
            # $script:0831180509005587$
            # - And thus, the brother and sister concluded their adventure. Did you enjoy the tale? You're an excellent listener. I enjoyed relaying the story to you.
            return -1
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005588$
            # - This time, I will share something I experienced firsthand. I've seen quite a lot in my not-so-short life, and I'm sure you'd enjoy some of my extraordinary tales.
            return 3100
        elif index == 1:
            # $script:0831180509005589$
            # - When I was young and curious, I traveled to many locales, even though I don't much care for traveling. This tale takes us to a remove village in the far south, whose name I can no longer remember.
            return 3100
        elif index == 2:
            # $script:0831180509005590$
            # - There was a big tree in the center of the village, which the villagers consulted for important events...
            return 3100
        elif index == 3:
            # $script:0831180509005591$
            # - <font color="#909090">(He goes into a lot of boring details and even the exciting moments are dragged down by his unnecessary analyses.)</font>
            return 3100
        elif index == 4:
            # $script:0831180509005592$
            # - In the end, I left that village to return home, but I still wonder sometimes... what was that tree? Was it really holy?
            return 3100
        elif index == 5:
            # functionID=1 openTalkReward=True
            # $script:0831180509005593$
            # - I experienced that personally, and I guarantee everything I said is 100% truth. Well, I may have exaggerated a little, but doesn't that just make it 120% truth?
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        # $script:0831180509005594$
        # - I can't right now. I just can't. Not even for you, $OwnerName$. You understand, don't you?
        # TODO: gotoConditionTalkID 30, 31, 32, 9011
        return -1

    def __4100(self, index: int, pick: int) -> int:
        # $script:0831180509005595$
        # - Right now? I can't just come up with a story on the spot, $OwnerName$. Also, I'm busy.
        # TODO: gotoConditionTalkID 30, 31, 32, 9011
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005596$
            # - I don't like talking about myself, $OwnerName$, and I prefer to keep things professional. Please understand that.
            return 5000
        elif index == 1:
            # $script:0831180509005597$
            # - If we were friends, I might change my mind, but I don't feel comfortable sharing. Please don't be upset.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005598$
            # - Well, let's see. My name is $MaidName$. I am fairfolk. I wear glasses. I have green hairs and eyes. I enjoy reading. But... this isn't the information you're after, is it?
            return 5100
        elif index == 1:
            # $script:0831180509005599$
            # - Allow me to make this clear so that it doesn't happen again: I do not like being asked about my personal life. If you wish to talk, I enjoy discussing topics of a more academic nature.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005600$
            # - $OwnerName$, why do you slather half the things you eat in ketchup? What appeals to you about that red sauce? I find it quite sour. Why do humans enjoy it so much?
            return 6000
        elif index == 1:
            # $script:0831180509005601$
            # - However, I do find myself quite drawn to the taste of mayonnaise. Its ivory tone, its light scent, its creamy taste... Mmm, dip a celery stick in some mayo, and this fairfolk is in heaven!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005602$
            # - $OwnerName$, last time when you asked me my age, I may have been a little harsh. I still don't wish to reveal my exact age, but I'm willing to give you some idea: I'm ridiculously old in human years but fairly young in fairfolk years.
            return 7000
        elif index == 1:
            # $script:0831180509005603$
            # - We must've grown close, $OwnerName$. I find that I don't mind telling you about myself, and I even catch myself thinking of you as a friend.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509005604$
        # - What brings you to this residence?
        if pick == 0:
            # $script:0831180509005605$
            # - I'm here to see your master.
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509005606$
            # - I came to check out the house.
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509005607$
            # - I wanted you to tell me an old tale.
            # TODO: goto 105, 106
            return -1
        return -1
