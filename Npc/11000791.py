""" 11000791: Solvay """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509005212$
        # - It's a beautiful day, isn't it?
        if pick == 0:
            # $script:0831180509005213$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005214$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005215$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509005216$
        # - Ah... $OwnerName$.
        if pick == 0:
            # $script:0831180509005217$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005218$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005219$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509005220$
        # - Welcome! ...Ah. I thought you were a customer. Hah hah.
        if pick == 0:
            # $script:0831180509005221$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005222$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005223$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509005224$
        # - It's a beautiful day, isn't it?
        if pick == 0:
            # $script:0831180509005225$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005226$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005227$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005228$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509005229$
        # - Ah... $OwnerName$.
        if pick == 0:
            # $script:0831180509005230$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005231$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005232$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005233$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509005234$
        # - Welcome! ...Ah. I thought you were a customer. Hah hah.
        if pick == 0:
            # $script:0831180509005235$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005236$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005237$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005238$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509005239$
        # - Huh? Do you want to give me my paycheck?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509005240$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005241$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005242$
        # - My wallet has felt heavier lately because you always pay me early. Thanks for hiring me for another month! Hah hah!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005243$
        # - Haha, thanks, $OwnerName$. I'm grateful to have a kind, competent boss like you.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005244$
        # - Haha, I told you: money comes and money goes. Thank you. I'll try to minimize the number of customers who come to the house, but I mean, it can't be helped sometimes.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005245$
        # - What? How'd you get so much money so quickly? $OwnerName$, this is serious. You gotta tell me how! Please!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005246$
        # - $OwnerName$, is everything all right? Our contract expires soon and you haven't mentioned it, so I was just wondering.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005247$
        # - But if you're not worried, I won't worry either.
        if pick == 0:
            # $script:0831180509005248$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005249$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005250$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005251$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509005252$
        # - Just say the word.
        if pick == 0:
            # $script:0831180509005253$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005254$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005255$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005256$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509005257$
        # - Do you have business with me?
        if pick == 0:
            # $script:0831180509005258$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005259$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005260$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005261$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509005262$
        # - Ah, I didn't know you were standing there.
        if pick == 0:
            # $script:0831180509005263$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005264$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005265$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005266$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509005268$
        # - Haha, $OwnerName$, you've already paid me for the month. I'm ethical, see? You can trust me.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509005271$
        # - $OwnerName$, what's really going on?
        if pick == 0:
            # $script:0831180509005272$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005273$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005274$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509005275$
        # - Mm... Is this because I keep inviting customers over?
        if pick == 0:
            # $script:0831180509005276$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005277$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005278$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509005279$
        # - This is not because I'm too talkative or too boring, is it?
        if pick == 0:
            # $script:0831180509005280$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005281$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005282$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005284$
        # - Is that really important right now, $OwnerName$? Our contract expired, and I don't mix business with pleasure.
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005285$
        # - It's been $MaidPassedDay$ since I've stopped working as your servant. I'm doing just fine, to be honest.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005286$
        # - You don't have to worry about me.
        if pick == 0:
            # $script:0831180509005287$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005288$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005289$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509005290$
        # - Hm... I'd better behave for a while... 
        if pick == 0:
            # $script:0831180509005291$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005292$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005293$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509005294$
        # - I will attempt to stop inviting customers into your home. That's the reason you won't renew our contract, isn't it? Or is there something else?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509005295$
        # - Hm, this unexpected financial blow is affecting my business. I'll have to think of a solution. Don't worry about me. This isn't the first time I've had a hiccup with money.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509005296$
        # - I have my own business, so I still have a means to live, even if I'm not paid for this side job. But $OwnerName$, you don't have a side job. Are you all right?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005297$
        # - I've learned this little trick while working as a hawker.
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005298$
        # - Let me know if I can help you.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005299$
        # - I'm just an ordinary hawker. That's all.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005300$
        # - Hm... Business is slow today... Ah, nothing. Hah hah!
        if pick == 0:
            # $script:0831180509005301$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005302$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005303$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005304$
        # - Hm... Business is slow today... Ah, nothing. Hah hah!
        if pick == 0:
            # $script:0831180509005305$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005306$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005307$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005308$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509005309$
        # - Taking care of this house sometimes make me want my own property.
        if pick == 0:
            # $script:0831180509005310$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509005311$
            # - (Gossip.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509005312$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509005313$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509005314$
        # - I wonder everything's going at the Barrota Trading Company...
        if pick == 0:
            # $script:0831180509005315$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509005316$
            # - (Gossip.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509005317$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509005318$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509005319$
        # - I need my business to be successful, you know.
        if pick == 0:
            # $script:0831180509005320$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509005321$
            # - (Gossip.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509005322$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509005323$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509005324$
        # - Just say the word.
        if pick == 0:
            # $script:0831180509005325$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005326$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005327$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509005328$
        # - Do you have business with me?
        if pick == 0:
            # $script:0831180509005329$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005330$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005331$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509005332$
        # - Ah, I didn't know you were standing there.
        if pick == 0:
            # $script:0831180509005333$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005334$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005335$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005336$
            # - I want to ask you a serious question. It's about what just happened to $npcName:11000526[gender:0]$.
            return 1000
        elif index == 1:
            # $script:0831180509005337$
            # - I think Dark Wind is suspicious of members of the Barrota Trading Company.
            return 1000
        elif index == 2:
            # $script:0831180509005338$
            # - So... $OwnerName$, what do you think of Dark Wind?
            if pick == 0:
                # $script:0831180509005339$
                # - Dark Wind is essential for keeping the peace in $map:2000100$.
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509005340$
                # - That whole organization is rather shady...
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005341$
        # - Hm... You think so? I guess our opinions differ. I suppose that's only human nature.
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005342$
        # - Does that mean you think it's okay for them to treat me the way they do? The injustice!
        return -1

    def __1011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005343$
        # - I knew I couldn't be the only one who thought so! There's definitely something strange going on.
        return -1

    def __1012(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005344$
        # - Right?! But that organization is already so entrenched in $map:2000100$... Anyway, thank you. Now I'm even more confident in my opinion.
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005345$
            # - Lately, I've been thinking maybe I gossip too much.
            return 1100
        elif index == 1:
            # $script:0831180509005346$
            # - But hearing all sorts of rumors comes with my job. And it's not like I can just forget what I hear.
            return 1100
        elif index == 2:
            # $script:0831180509005347$
            # - Should I stop telling others what I hear? What are your thoughts on this?
            if pick == 0:
                # $script:0831180509005348$
                # - You should be careful about what you say.
                # TODO: goto 1111, 1112
                return -1
            elif pick == 1:
                # $script:0831180509005349$
                # - I don't care either way.
                # TODO: goto 1101, 1102
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005350$
        # - You don't? But I don't want something bad to happen to me, so I'm thinking maybe I should stop.
        return -1

    def __1102(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005351$
        # - You don't care. So that means you don't care if I tell others about you, right, $OwnerName$? I see what you do when you think I'm not looking...
        return -1

    def __1111(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005352$
        # - I should, right? Thank you for being honest with me. I'll be more careful from now on.
        return -1

    def __1112(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005353$
        # - But you like listening to me gossip, don't you, $OwnerName$? Still, I'm glad I asked.
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005354$
            # - Ahhh... Things haven't been so hot with the Barrota Trading Company.
            return 2000
        elif index == 1:
            # $script:0831180509005355$
            # - We're Maple World's largest and most reputable group of traders! How did it come to this...? 
            return 2000
        elif index == 2:
            # $script:0831180509005356$
            # - I don't know how they knew where to find me, but a Dark Wind agent stopped by the house a while ago.
            return 2000
        elif index == 3:
            # $script:0831180509005357$
            # - I swear to you, I've never done anything unethical as a hawker. Not once! Maybe a bit of gossip, but nothing even close to illegal.
            return 2000
        elif index == 4:
            # $script:0831180509005358$
            # - He may be a Dark Wind agent, but that doesn't give him the right to treat me the way he did, accusing me of all sorts of horrible things, asking me all sorts of mean questions. I feel violated!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005359$
            # - While taking care of your home, I've located many items that you don't use.
            return 2100
        elif index == 1:
            # $script:0831180509005360$
            # - For example, this exercise equipment. Only used once or twice, am I correct?
            return 2100
        elif index == 2:
            # $script:0831180509005361$
            # - $OwnerName$, with your permission, I'd like to sell these items. You get the benefit of less clutter, and I get the benefit of a cut of the profits. Win-win, all around, wouldn't you say?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005362$
            # - I hung a banner over the door today, and a lot of people stopped by the house to shop.
            return 2200
        elif index == 1:
            # $script:0831180509005363$
            # - I had no idea having a physical shop could be so convenient!
            return 2200
        elif index == 2:
            # $script:0831180509005364$
            # - Ah, o-of course, $OwnerName$, this is your house, but I get bored sitting around, waiting for you.
            return 2200
        elif index == 3:
            # $script:0831180509005365$
            # - So I was thinking... You don't mind if I do my business in your house from time to time, do you?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __3000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005366$
            # - Okay, so you know $npc:11000074[gender:0]$ in $map:02000001$? He's a trusted subject of $npcName:11000075[gender:1]$.
            return 3000
        elif index == 1:
            # $script:0831180509005367$
            # - He has a daughter, $npcName:11000058[gender:1]$. She lives in her father's mansion in $map:02000119$.
            return 3000
        elif index == 2:
            # $script:0831180509005368$
            # - But rumor has it that the minister had another daughter...
            return 3000
        elif index == 3:
            # $script:0831180509005369$
            # - No, not a lovechild. Sheesh, what are you talking about? $npcName:11000058[gender:1]$ had a twin sister, and she disappeared all of a sudden.
            return 3000
        elif index == 4:
            # functionID=1 openTalkReward=True 
            # $script:0831180509005370$
            # - It happened a long time ago, so no one knows if her sister is alive or dead. Tragic, isn't it?
            return -1
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005371$
            # - This is kind insane, but $npcName:11000252[gender:0]$ in $map:02000100$ has a big secret.
            return 3100
        elif index == 1:
            # $script:0831180509005372$
            # - Who? Really? You've never heard of Goldus Group?
            return 3100
        elif index == 2:
            # $script:0831180509005373$
            # - Goldus Group partakes in all sorts of businesses—real estate, banking, pharmaceutical, to name a few.
            return 3100
        elif index == 3:
            # $script:0831180509005374$
            # - And its chairman is—hm, I don't know if I should tell you this. 
            return 3100
        elif index == 4:
            # $script:0831180509005375$
            # - Its chairman is... He's actually...
            return 3100
        elif index == 5:
            # functionID=1 openTalkReward=True 
            # $script:0831180509005376$
            # - Ugh, no, I can't. If this gets out, the Barrota Trading Company can get in huge trouble.
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005377$
            # - Hawkers travel everywhere in Maple World. Some of us have even recently dared to enter the Shadow World.
            return 4000
        elif index == 1:
            # $script:0831180509005378$
            # - Rumor has it that a hawker named $npcName:11000609[gender:0]$ returned from that shadowy realm, looking like he'd seen a ghost.
            return 4000
        elif index == 2:
            # $script:0831180509005379$
            # - He was lucky. Blackstar protects merchants. I'd be surprised if a normal person made it back from that world.
            return 4000
        elif index == 3:
            # $script:0831180509005380$
            # - $OwnerName$, don't you dare even think of going there. Stop it. Stop. I know you're already thinking about it...
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005381$
            # - They say Maple World is in shambles because of the actions of one young, harmless-looking man named... Um... What was his name? 
            return 4100
        elif index == 1:
            # $script:0831180509005382$
            # - Whatever. Dark Wind is searching everywhere for him.
            return 4100
        elif index == 2:
            # $script:0831180509005383$
            # - I saw his wanted poster in $map:02000100$. He has blond hair, red eyes, and a scar on his face.
            return 4100
        elif index == 3:
            # $script:0831180509005384$
            # - $OwnerName$, if you see anyone looking like him, you should report him to Dark Wind. That way you can collect the bounty and share it with me.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005385$
            # - I have my reasons for being a hawker. Money is one of them, sure. I mean, we all need money, right?
            return 5000
        elif index == 1:
            # $script:0831180509005386$
            # - But that's not the only reason. It might be hard for residents of big cities like $map:02000001$ to imagine, but some folks really do live far, far away from civilization.
            return 5000
        elif index == 2:
            # $script:0831180509005387$
            # - And those people need me to get things for them. They count the days until my next visit and watch me approach with excitement in their eyes.
            return 5000
        elif index == 3:
            # $script:0831180509005388$
            # - It's not easy traveling over rough terrain, weighed down with a backpack of cargo...
            return 5000
        elif index == 4:
            # $script:0831180509005389$
            # - But I truly love it. Selling valued items, delivering news... I get so caught up in all of it that I lose track of time.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005390$
            # - The Barrota Trading Company is Maple World's hawker union. We've got hundreds of members, hawking all over the world.
            return 5100
        elif index == 1:
            # $script:0831180509005391$
            # - We don't just sell items. People also rely on us to deliver the latest news.
            return 5100
        elif index == 2:
            # $script:0831180509005392$
            # - Think of it this way: If this world were a body, we'd be the blood vessels spreading life throughout it! Haha!
            return 5100
        elif index == 3:
            # $script:0831180509005393$
            # - Well, we're in a tight spot right now, but it's got to be some sort of misunderstanding. I couldn't imagine Maple World without hawkers.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005394$
            # - $OwnerName$, you may not remember this...
            return 6000
        elif index == 1:
            # $script:0831180509005395$
            # - Long ago, we first met in $map:63000001$. You were looking for a trip to get to $map:02000062$  for the Empress's event, remember?
            return 6000
        elif index == 2:
            # $script:0831180509005396$
            # - It's okay if you don't remember. I've got a good enough memory for the both of us. In fact, the whole trading company knows about my superb memory.
            return 6000
        elif index == 3:
            # $script:0831180509005397$
            # - Back then, I was so excited about the Empress's little shindig... Who would've thought we'd end up living in the same house? The future is full of secrets, isn't it?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005398$
            # - I've never really given serious thought to settling down. What can I say? I just love being a hawker.
            return 7000
        elif index == 1:
            # $script:0831180509005399$
            # - Now, $npcName:11000170[gender:0]$, on the other hand, he found himself a lady while selling his wares. Says he's ready to settle down. He just has to work up the courage to talk to the girl.
            return 7000
        elif index == 2:
            # $script:0831180509005400$
            # - It's made me think. I don't know, maybe someday I want to settle down, too... Have a family, all that...
            return 7000
        elif index == 3:
            # $script:0831180509005401$
            # - But not yet. First, I want to hustle and build up an amazing reputation as a hawker!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509005402$
        # - Welcome! Is there something you're looking for?
        if pick == 0:
            # $script:0831180509005403$
            # - Show me your wares.
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509005404$
            # - I really don't care.
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509005405$
            # - I thought this was a house, not a store.
            # TODO: goto 105, 106
            return -1
        return -1

