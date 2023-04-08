""" 11000544: Tim """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509000251$
        # - Hello, $OwnerName$.
        if pick == 0:
            # $script:0831180509000252$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000253$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000254$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509000255$
        # - Is there anything I can help you with?
        if pick == 0:
            # $script:0831180509000256$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000257$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000258$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509000259$
        # - Just say the word, $OwnerName$.
        if pick == 0:
            # $script:0831180509000260$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000261$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000262$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509000263$
        # - Hello, $OwnerName$.
        if pick == 0:
            # $script:0831180509000264$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000265$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000266$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000267$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509000268$
        # - Is there anything I can help you with?
        if pick == 0:
            # $script:0831180509000269$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000270$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000271$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000272$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509000273$
        # - Just say the word, $OwnerName$.
        if pick == 0:
            # $script:0831180509000274$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000275$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000276$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000277$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509000278$
        # - Are you giving me my paycheck?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509000279$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000280$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000281$
        # - Thank you for hiring me for another month. You won't regret it.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000282$
        # - Thank you for paying me on time, $OwnerName$. My bosses at Helping Hands just can't stop talking about how wonderful you are.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000283$
        # - I thought you'd forgotten about me. You were late, but you made it before I had no choice but to leave. Now, would you like a cup of tea?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000284$
        # - Thank you for not disappointing me $OwnerName$. It is my pleasure to stay under your employment.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000285$
        # - Just so you are aware, it is almost payday.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000286$
        # - I hope you haven't forgotten about it.
        if pick == 0:
            # $script:0831180509000287$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000288$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000289$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000290$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509000291$
        # - Sure, $OwnerName$. I always enjoy talking to you.
        if pick == 0:
            # $script:0831180509000292$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000293$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000294$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000295$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509000296$
        # - Sometimes, I feel quite close to you, $OwnerName$.
        if pick == 0:
            # $script:0831180509000297$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000298$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000299$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000300$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509000301$
        # - Hmm? Did something happen, $OwnerName$?
        if pick == 0:
            # $script:0831180509000302$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000303$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000304$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000305$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509000307$
        # - You've already paid me this month. You must be a little stressed out.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509000310$
        # - It's a violation of company policy to work without being paid on time.
        if pick == 0:
            # $script:0831180509000311$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000312$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000313$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509000314$
        # - You are already $MaidPassedDay$ late on my paycheck.
        if pick == 0:
            # $script:0831180509000315$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000316$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000317$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509000318$
        # - I understand that you're having financial difficulties, $OwnerName$, but I'm afraid I can't offer you any more leeway.
        if pick == 0:
            # $script:0831180509000319$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000320$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000321$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000323$
        # - $OwnerName$, shouldn't we be talking how you're $MaidPassedDay$ overdue on my paycheck instead?
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000324$
        # - I don't really have much to say.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000325$
        # - You're $MaidPassedDay$ behind on my paycheck.
        if pick == 0:
            # $script:0831180509000326$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000327$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000328$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509000329$
        # - You're $MaidPassedDay$ behind on my paycheck.
        if pick == 0:
            # $script:0831180509000330$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000331$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000332$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509000333$
        # - You're $MaidPassedDay$ behind on my paycheck. I know we're friends, but policy is policy.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509000334$
        # - You may think my mind is always on business, but you're $MaidPassedDay$ overdue on paying me, and I have bills, too...
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509000335$
        # - I never thought you'd be like this, $OwnerName$. A contract is a promise between two parties. You seemed like someone who would keep $male:his,female:her$ word.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000336$
        # - Would you like me to craft you a ring?
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000337$
        # - Feel free to discuss rings with me whenever you like.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000338$
        # - Ah, you must wish to learn more about me.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000339$
        # - But I just don't feel comfortable going into too much detail about myself...
        if pick == 0:
            # $script:0831180509000340$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000341$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000342$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1
        # $script:0831180509000343$
        # - But I just don't feel comfortable going into too much detail about myself...
        if pick == 0:
            # $script:0831180509000344$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000345$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000346$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509000347$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509000348$
        # - You look happy today. What did you want to talk about?
        if pick == 0:
            # $script:0831180509000349$
            # - Did anything interesting happen?
            # TODO: goto 1000, 1100, 1200, 1300, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509000350$
            # - May I have a cup of tea?
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509000351$
            # - Let's talk for a bit, me and you.
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509000352$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509000353$
        # - Oh? You have something you'd like to talk to me about?
        if pick == 0:
            # $script:0831180509000354$
            # - Did anything interesting happen?
            # TODO: goto 1000, 1100, 1200, 1300, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509000355$
            # - May I have a cup of tea?
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509000356$
            # - Let's talk for a bit, me and you.
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509000357$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509000358$
        # - I'm not much of a talker, but as you wish.
        if pick == 0:
            # $script:0831180509000359$
            # - Did anything interesting happen?
            # TODO: goto 1000, 1100, 1200, 1300, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509000360$
            # - May I have a cup of tea?
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509000361$
            # - Let's talk for a bit, me and you.
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509000362$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509000363$
        # - Sure, $OwnerName$. I always enjoy talking to you.
        if pick == 0:
            # $script:0831180509000364$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000365$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000366$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509000367$
        # - Sometimes, I feel quite close to you, $OwnerName$.
        if pick == 0:
            # $script:0831180509000368$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000369$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000370$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509000371$
        # - Hmm? Did something happen, $OwnerName$?
        if pick == 0:
            # $script:0831180509000372$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000373$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000374$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000375$
            # - While nothing particularly interesting occurred today, I try to appreciate every single day that passes. Once it's gone, you can never get it back.
            return 1000
        elif index == 1:
            # $script:0831180509000376$
            # - When you take time to be grateful, the world around you changes. The flowers you see, the sky above your head, even the bus that stops by the house at the same time each day, all of those become special. In the end, you realize that no two days are ever the same.
            return 1000
        elif index == 2:
            # $script:0831180509000377$
            # - For example, today, right now, I'm talking to you, $OwnerName$, and that makes this moment special. Every moment we share is special.
            if pick == 0:
                # $script:0831180509000378$
                # - I completely agree.
                # TODO: goto 1011, 1012
                return -1
            elif pick == 1:
                # $script:0831180509000379$
                # - Uh, are you feeling okay?
                # TODO: goto 1001, 1002
                return -1
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000380$
        # - I apologize. I should be working, not spouting philosophy. If you'll excuse me...
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000381$
        # - You may think it's corny, but there are many books that go into great depth about this topic. But perhaps I should keep my thoughts to myself.
        return -1

    def __1011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000382$
        # - I knew you would, $OwnerName$. Some may think what I said is corny, but I knew you would understand.
        return -1

    def __1012(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000383$
        # - Take a deep breath. Ahhh. See? Even the air is more invigorating when you take a moment to treasure it. Thank you for chatting with me about this, $OwnerName$.
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000384$
            # - I was gardening today, when a grubby little dog showed up and started running around.
            return 1100
        elif index == 1:
            # $script:0831180509000385$
            # - He came up to me, wagging his tail as if he wanted to play. I was elbows deep in weeds, so I wasn't sure what to do.
            if pick == 0:
                # $script:0831180509000386$
                # - You let a filthy dog into my garden?!
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509000387$
                # - Awww, did you play with him? And feed him?
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000388$
        # - Ah, I sent him away, as gently as I could, and wiped away all his paw prints. That's all.
        return -1

    def __1102(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000389$
            # - I didn't "let" him, he jumped the fence. It was no big deal. He didn't mess up your flowers or anything.
            return 1102
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509000390$
            # - He was such a cute little thing. I couldn't scold him. He was so cute, you wouldn't have been able to either, $OwnerName$.
            return -1
        return -1

    def __1111(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000391$
            # - I did. In fact, I probably should've asked permission before I did this, but...
            return 1111
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509000392$
            # - I also gave him a much-needed bath. He was such a cute little guy. I hope he comes back.
            return -1
        return -1

    def __1112(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000393$
            # - I knew you'd say that, $OwnerName$. You're just like me.
            return 1112
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509000394$
            # - I not only fed him and played with him, I also gave him a bath and brushed his fur. Then he settled down for a nice long nap at my side while I finished with the garden.
            return -1
        return -1

    def __1200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000395$
            # - I had a terrible day, $OwnerName$. Are you ready to hear my horrific story?
            return 1200
        elif index == 1:
            # $script:0831180509000396$
            # - I was ironing your clothes, and for some reason, I just couldn't get the seams perfect! I tried over and over and over. Seams are one of my specialties, you know.
            return 1200
        elif index == 2:
            # $script:0831180509000397$
            # - I was so frustrated! I tried ironing my own clothes, starting with the one I'm wearing now.
            return 1200
        elif index == 3:
            # $script:0831180509000398$
            # - And wouldn't you know, it turned out perfectly! So I went back to ironing yours, and I just couldn't do it. Ugh...
            return 1200
        elif index == 4:
            # $script:0831180509000399$
            # - To conclude, none of your clothes have been ironed. What a nightmare.
            if pick == 0:
                # $script:0831180509000400$
                # - Hey, at least your shirt looks good.
                # TODO: goto 1211, 1212
                return -1
            elif pick == 1:
                # $script:0831180509000401$
                # - Wait, so I don't have any ironed clothes to wear tomorrow?
                # TODO: goto 1201, 1202
                return -1
            return -1
        return -1

    def __1201(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000402$
        # - That's correct. I'm so, so sorry. I feel absolutely horrible.
        return -1

    def __1202(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000403$
        # - I have no excuse. I will stay up all through the night to attempt to get at least one outfit wrinkle-free for you to wear tomorrow.
        return -1

    def __1211(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000404$
            # - I'm so sorry, I know I've completely ruined your— Excuse me? Did you just compliment me? Heh, I guess my shirt does look pretty good, doesn't it?
            return 1211
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509000405$
            # - $OwnerName$, you are an amazing person. I am honored to work for you. Let me try ironing your clothes one more time. I think I can do it this time!
            return -1
        return -1

    def __1212(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000406$
            # - Oh! Um. Heh. T-thank you. A servant should look presentable and sharp at all times. See this edge here? I'm normally so good at getting the seams to an extra sharp point!
            return 1212
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509000407$
            # - I feel inspired and motivated now. I will collect my ironing kit and try ironing your clothes again. Thank you for the compliment.
            return -1
        return -1

    def __1300(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000408$
            # - A-ah! W-what? N-nothing! Nothing happened today! N-n-nothing!
            return 1300
        elif index == 1:
            # $script:0831180509000409$
            # - Ahhh, how do you always know when I'm trying to hide something, $OwnerName$?
            return 1300
        elif index == 2:
            # $script:0831180509000410$
            # - Here, take a look at this paper. It says, "Your soul mate is lurking nearby. Expect an unexpected kiss at an unexpected place."
            return 1300
        elif index == 3:
            # $script:0831180509000411$
            # - I got it from a fortune cookie sample at the grocery store.
            return 1300
        elif index == 4:
            # $script:0831180509000412$
            # - <font color="#909090">(He takes back the paper and daintily places it in his inner pocket.)</font>
            #   I told you it was nothing.
            if pick == 0:
                # $script:0831180509000413$
                # - You're not taking a fortune cookie seriously, are you?
                # TODO: goto 1301, 1302
                return -1
            elif pick == 1:
                # $script:0831180509000414$
                # - Hey, hey! Congratulations!
                # TODO: goto 1311, 1312
                return -1
            return -1
        return -1

    def __1301(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000415$
        # - Who says I'm taking it seriously? You asked if anything interesting happened. I answered. Now if you'll excuse me, I have to go mend your socks.
        return -1

    def __1302(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000416$
        # - Of course not. Do you take me for an idiot? For the record, I've always carried I pack of mints on me. I didn't just start today.
        return -1

    def __1311(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True
        # $script:0831180509000417$
        # - Wh-what? No! It's not... I'm not... Ahem. Let's not talk about this anymore.
        return -1

    def __1312(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000418$
            # - You've got it all wrong, $OwnerName$. It's just a silly fortune. I'm not stupid enough to get all excited over it.
            return 1312
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509000419$
            # - Now if you'll excuse me, I believe I hear the kettle. Your tea is almost ready. Ahem.
            #   <font color="#909090">(He walks away, blushing hard.)</font>
            return -1
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000420$
            # - Ah, today was just an ordinary day. Nothing to report, really.
            return 2000
        elif index == 1:
            # $script:0831180509000421$
            # - How was your day, $OwnerName$?
            return 2000
        elif index == 2:
            # $script:0831180509000422$
            # - Ah, I see. Some days pass by so peacefully. Perhaps it's days like this that make us truly happy.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000423$
            # - The most notable event of the day is you talking to me, $OwnerName$. Other than that, I've just been listening to the birds chirping.
            return 2100
        elif index == 1:
            # $script:0831180509000424$
            # - On days like this, I like to relax with a nice cup of tea.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __3000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000425$
            # - In fact, that's just what you should do. Nothing like a sunny afternoon sipping a cup of tea. Just give me a moment to prepare it...
            return 3000
        elif index == 1:
            # functionID=1 openTalkReward=True
            # $script:0831180509000426$
            # - There you go. How do you like it? It's Royal Blend with a touch of cream, perfect for an afternoon as beautiful as this one. I'll leave you to enjoy your tea in peace.
            return -1
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000427$
            # - I recently purchases an amazing Earl Grey tea. How about I treat you to a cup, $OwnerName$? Just give me a moment, and you'll have the best tea you've ever tasted in your life.
            return 3100
        elif index == 1:
            # $script:0831180509000428$
            # - Here you go. My favorite Earl Grey blend. Do you taste the bergamot flavor? Magnificent! Do you like it?
            return 3100
        elif index == 2:
            # functionID=1 openTalkReward=True
            # $script:0831180509000429$
            # - I knew you would like it. The secret to brewing the perfect cup of tea is whispering for it to be delicious as you prepare it, and that's just what I did today.
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        # $script:0831180509000430$
        # - Apologies, but I can't join you for tea at the moment. There are some items that require my immediate attention. Perhaps later.
        # TODO: gotoConditionTalkID 30, 31, 32, 9011
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000431$
            # - Oh, would you like coffee instead of tea today? I will prepare your favorite latte, then.
            return 4100
        elif index == 1:
            # $script:0831180509000432$
            # - I've carefully brewed the espresso and added fresh milk. I hope you like it. Oh, no, you don't need to save any for me. I don't drink coffee.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000433$
            # - You want to know about my home? Hmm, I don't usually talk about myself. Let's see...
            return 5000
        elif index == 1:
            # $script:0831180509000434$
            # - I come from a beautiful little place right by the sea, near a sharp cliff. It's cold and windy there, but the people are kind and love to sing.
            return 5000
        elif index == 2:
            # $script:0831180509000435$
            # - I've been drinking tea since before I could walk.  It reminds me of home. Oh, don't worry. I'm content with my life here. I just like to reminisce sometimes.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000436$
            # - You want to know my favorite hand cream? You're aware I wear gloves, aren't you? Even if I didn't, scented creams would disrupt the delicate glean of teacups and plates. It would ruin the entire tea-drinking experience.
            return 5100
        elif index == 1:
            # $script:0831180509000437$
            # - When I go out out, however, I have been known to dab on a small amount of light lavender or verbena scented lotion.
            return 5100
        elif index == 2:
            # $script:0831180509000438$
            # - Does that answer your question?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000439$
            # - Curiosity is a powerful thing. It cultivates knowledge! It is the foundation of human civilization! Perhaps you're curious about the linen towel draped over my arm?
            return 6000
        elif index == 1:
            # $script:0831180509000440$
            # - Linen towels are essential for a servant. When a spot of tea drips from a spout, the linen towel comes to the rescue. When an errant crumb falls from a cracker, the linen towel brushes it away.
            return 6000
        elif index == 2:
            # $script:0831180509000441$
            # - The most important rule is to use fresh towels every hour, pristine and crisply folded. If dirtied, it is perfectly acceptable to replace the towel more often than that.
            return 6000
        elif index == 3:
            # $script:0831180509000442$
            # - The linen towel has become an icon of cleanliness, professionalism, comfort, and bliss.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509000443$
            # - Ah, what a wonderful day. The dishes were washed to a sparkle! My heart fluttered watching the laundry fluttering in the breeze!
            return 7000
        elif index == 1:
            # $script:0831180509000444$
            # - The tea I poured reminded me of someone I knew, and the water I squeezed the linen towel felt like the melody of her voice.
            return 7000
        elif index == 2:
            # $script:0831180509000445$
            # - She was a childhood friend. I still remember how she held onto her wide-brimmed hat against the breeze atop that cliff, how the skirt of her white dress caressed her legs.
            return 7000
        elif index == 3:
            # $script:0831180509000446$
            # - ...What am I talking about? I apologize, $OwnerName$. I've grown too comfortable around you. I never meant to share such a private memory.
            return 7000
        elif index == 4:
            # $script:0831180509000447$
            # - Please forget what I just told you. I suppose even I get sentimental sometimes.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509000448$
        # - Hello. I don't think I've seen you before. How may I help you?
        if pick == 0:
            # $script:0831180509000449$
            # - I'm here to see your master.
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509000450$
            # - Oh, I don't need anything.
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509000451$
            # - Hey, do I smell tea? It smells good!
            # TODO: goto 105, 106
            return -1
        return -1
