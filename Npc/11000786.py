""" 11000786: Eka """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])


    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509004137$
        # - Who's there?! Ah, it's you, $OwnerName$. Heh heh.
        if pick == 0:
            # $script:0831180509004138$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004139$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004140$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509004141$
        # - The coast is clear, like always!
        if pick == 0:
            # $script:0831180509004142$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004143$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004144$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509004145$
        # - I'm on duty. Please make it short.
        if pick == 0:
            # $script:0831180509004146$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004147$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004148$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509004149$
        # - Who's there?! Ah, it's you, $OwnerName$. Heh heh.
        if pick == 0:
            # $script:0831180509004150$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004151$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004152$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004153$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509004154$
        # - The coast is clear, like always!
        if pick == 0:
            # $script:0831180509004155$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004156$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004157$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004158$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509004159$
        # - I'm on duty. Please make it short.
        if pick == 0:
            # $script:0831180509004160$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004161$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004162$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004163$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509004164$
        # - Are you giving me my paycheck?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509004165$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004166$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004167$
        # - Whoa, you're paying me already? Thank you much! Teehee! Let's have a feast tonight!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004168$
        # - I needed this! I spent all my money on a preparing a fancy lunch box for $npcName:11000015[gender:1]$ the other day. Teehee! Thank you, $OwnerName$!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004169$
        # - Yay, you finally have money to pay me! I thought I was going to starve to death. I'm so happy everything worked out!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509004170$
        # - Whoa! I was debating whether I should look for another job. It's not because of you, $OwnerName$, promise. But, a girl's gotta eat.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004171$
        # - Hmmm, our contract expires in a few days and I'm running out of money for groceries. Are you planning to pay me soon? 
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004172$
        # - Hah hah! No pressure! 
        if pick == 0:
            # $script:0831180509004173$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004174$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004175$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004176$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509004177$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509004178$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004179$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004180$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004181$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509004182$
        # - Just say the word.
        if pick == 0:
            # $script:0831180509004183$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004184$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004185$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004186$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509004187$
        # - Is there something else you wanted?
        if pick == 0:
            # $script:0831180509004188$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004189$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004190$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004191$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509004193$
        # - Um, didn't you already pay me this month?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509004196$
        # - ...Huh? Did you say something?
        if pick == 0:
            # $script:0831180509004197$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004198$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004199$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509004200$
        # - What do you think $npcName:11000015[gender:1]$ would say if she finds out about this?
        if pick == 0:
            # $script:0831180509004201$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004202$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004203$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509004204$
        # - The injury I got from training isn't healing well, but I don't have the money to pay ointment for it... 
        if pick == 0:
            # $script:0831180509004205$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004206$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004207$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004210$
        # - I haven't eaten for $MaidPassedDay$. Maybe my injuries aren't healing due to lack of nutrition!  
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004211$
        # - I feel so weak... 
        if pick == 0:
            # $script:0831180509004212$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004213$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004214$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509004215$
        # - I miss $npcName:11000015[gender:1]$... 
        if pick == 0:
            # $script:0831180509004216$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509004217$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004218$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509004219$
        # - Now I know that being neglected is worse than being scolded. $OwnerName$, you don't want me, do you?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509004220$
        # - Is this because I gave your food to $npc:11000502[gender:0]$? I hope not. I didn't think you were a petty person. 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509004221$
        # - If I die from starvation, please bury me somewhere sunny in $map:02000076$, somewhere close to
        #   $npcName:11000015[gender:1]$. Don't let her know I suffered... What?! I'm really hungry!!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004222$
        # - I love messing around with beads! I'm good at it, too.
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004223$
        # - I can craft stuff for you whenever.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004224$
        # - Our contract includes some details about me.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004225$
        # - Just say the word.
        if pick == 0:
            # $script:0831180509004226$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004227$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004228$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509004229$
        # - Just say the word.
        if pick == 0:
            # $script:0831180509004230$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004231$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004232$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509004233$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509004234$
        # - Yes?
        if pick == 0:
            # $script:0831180509004235$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509004236$
            # - Tell me about $npcName:11000015[gender:1]$.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509004237$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509004238$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509004239$
        # - Everyone in $map:2000076$ should be okay, right?
        if pick == 0:
            # $script:0831180509004240$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509004241$
            # - Tell me about $npcName:11000015[gender:1]$.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509004242$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509004243$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509004244$
        # - I don't have time for chitchat.
        if pick == 0:
            # $script:0831180509004245$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509004246$
            # - Tell me about $npcName:11000015[gender:1]$.
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509004247$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509004248$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509004249$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509004250$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004251$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004252$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509004253$
        # - Just say the word.
        if pick == 0:
            # $script:0831180509004254$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004255$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004256$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509004257$
        # - Is there something else you wanted?
        if pick == 0:
            # $script:0831180509004258$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509004259$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509004260$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004261$
            # - $npcName:11000015[gender:1]$... I wonder if she's eating well...
            return 1000
        elif index == 1:
            # $script:0831180509004262$
            # - $OwnerName$, I want to ask you something. I can't stop thinking about $npcName:11000015[gender:1]$. I'm worried she might think I'm bothering her.
            return 1000
        elif index == 2:
            # $script:0831180509004263$
            # - A while ago, I was badly injured during an operation. $npcName:11000015[gender:1]$ was furious! I've never seen her like that. Do you think... she hates me?
            if pick == 0:
                # $script:0831180509004264$
                # - Yes.
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509004265$
                # - I think it's the opposite, actually.
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004270$
            # - The Green Hoods protect the order of Maple World! But...
            return 1100
        elif index == 1:
            # $script:0831180509004271$
            # - A while ago, I was injured during an operation, and my father has been urging me to quit ever since.
            return 1100
        elif index == 2:
            # $script:0831180509004272$
            # - I understand he loves his daughter, but I don't want to quit. I don't want disappoint my father, either... What do I do?
            if pick == 0:
                # $script:0831180509004273$
                # - Stay true to your convictions, for yourself and your father's sake.
                # TODO: goto 1111, 1112
                return -1
            elif pick == 1:
                # $script:0831180509004274$
                # - Stop caring only about $npcName:11000015[gender:1]$. Think about your parents, too!
                # TODO: goto 1101, 1102
                return -1
            return -1
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004279$
            # - $npcName:11000508[gender:1]$ stopped by this afternoon. She and I grew up together in $map:2000076$.
            return 2000
        elif index == 1:
            # $script:0831180509004280$
            # - She said $npcName:11000015[gender:1]$ ate nothing but a piece of bread for lunch today.
            return 2000
        elif index == 2:
            # $script:0831180509004281$
            # - I can't believe they're neglecting her meals like that!!
            return 2000
        elif index == 3:
            # $script:0831180509004282$
            # - So I packed a three-layered lunch box with the ingredients that I was going to use for dinner tonight and sent it back with $npcName:11000508[gender:1]$. Gosh, the Green Hoods can't do anything without me! ...By the way, we'll have to skip dinner tonight.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004283$
            # - Today, after finishing the housework, I patrolled the house and saw a stranger.
            return 2100
        elif index == 1:
            # $script:0831180509004284$
            # - He looked suspicious, so I hid and watched... He snuck into our house! I stayed still because I wanted to catch him red-handed.
            return 2100
        elif index == 2:
            # $script:0831180509004285$
            # - He went into the kitchen and poked around, looking for food. I couldn't wait any longer, so I pounced on him! And...
            return 2100
        elif index == 3:
            # $script:0831180509004286$
            # - It was someone I knew: $npc:11000502[gender:0]$. He's a disgrace to his father.
            return 2100
        elif index == 4:
            # $script:0831180509004287$
            # - He looked like he hadn't eaten for two days, so I had to give him food... I'm sorry I gave away your food. You can take it out of my pay if you want.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004288$
            # - It's too boring to stay inside the house all day. I want to go out and exercise. $OwnerName$, want to come with me?
            return 2200
        elif index == 1:
            # $script:0831180509004289$
            # - I want to join $map:61000006$, which takes place in $map:2000064$ every day, once in the morning and once in the evening.
            return 2200
        elif index == 2:
            # $script:0831180509004290$
            # - It'll be fun! We'll do it together! Come on, go change into your workout gear!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004299$
            # - Huh? $npcName:11000015[gender:1]$? Hah hah! What about $npcName:11000015[gender:1]$?
            return 4000
        elif index == 1:
            # $script:0831180509004300$
            # - W-wait. Did something happen to $npcName:11000015[gender:1]$? Is that it? Huh? Huh? Come on, you're killing me here. Answer me!
            return 4000
        elif index == 2:
            # $script:0831180509004301$
            # - ...Oh. You don't think $npcName:11000015[gender:1]$ washed her hair today. Sheesh, what does it matter if she washed her hair or not?
            return 4000
        elif index == 3:
            # $script:0831180509004302$
            # - Besides, $npcName:11000015[gender:1]$ is not a slob. She must have gotten oil on her hair while fighting. Duh!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004303$
            # - Many of us joined the group because we admired $npcName:11000015[gender:1]$. T-that was my reason, obviously.
            return 4100
        elif index == 1:
            # $script:0831180509004304$
            # - Charismatic, a natural leader, a heart of gold, amazing combat skills, and unparalleled beauty! $npcName:11000015[gender:1]$ is perfect in every way.
            return 4100
        elif index == 2:
            # $script:0831180509004305$
            # - Hey, if you think I'm infatuated with her, fine. Think whatever you want, as long as it distracts you from crushing on her yourself.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004306$
            # - A Green Hood from $map:2000076$, that's me! Born and raised in $map:2000076$, I know everyone there as well as my own family.
            return 5000
        elif index == 1:
            # $script:0831180509004307$
            # - Have you met $npcName:11000508[gender:1]$ in $map:2000203$ before? She's been my best friend since we were young.
            return 5000
        elif index == 2:
            # $script:0831180509004308$
            # - That girl is so strong that she can do any man's work with no problem... Hm, I guess the same goes for me too, huh? Teehee!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004309$
            # - That reminds me of $npcName:11000502[gender:0]$. I hope he's not being taken advantage of by anyone, wherever he is.
            return 5100
        elif index == 1:
            # $script:0831180509004310$
            # - He's some guy I've known since I young. He's a decent fellow, but a bit naive and immature. It makes him easy prey.
            return 5100
        elif index == 2:
            # $script:0831180509004311$
            # - I don't know why he couldn't learn from his father... $npcName:11000502[gender:0]$ is the son of Elder $npcName:11000001[gender:0]$ in $map:2000076$.
            return 5100
        elif index == 3:
            # $script:0831180509004312$
            # - Come to think of it, rumor has it that every elder for generations has had a troublemaker son. Do you think that's true?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004313$
            # - I thought I was going to live ordinary life, staying in peaceful $map:2000076$ for all of my days.
            return 6000
        elif index == 1:
            # $script:0831180509004314$
            # - Meeting $npcName:11000015[gender:1]$ completely changed my life. Watching a small, dainty-looking woman command a cohort of warriors touched me in a way nothing else ever has.
            return 6000
        elif index == 2:
            # $script:0831180509004315$
            # - I'd never seen the world outside of $map:2000076$ or held a bow in my hand, but I decided to join her group, despite my father's objections.
            return 6000
        elif index == 3:
            # $script:0831180509004316$
            # - Now that I've joined the Green Hoods, sometimes I feel sorry for $npcName:11000015[gender:1]$. She was trained to be the leader of the Green Hoods since she was born, and being responsible for so many lives has to be tough.
            return 6000
        elif index == 4:
            # $script:0831180509004317$
            # - I'd love to be there when she needs someone to talk to, but I know $npcName:11000015[gender:1]$ would never show any weakness, no matter how troubled she was on the inside..
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509004318$
            # - Ugh... I don't think the injury I got on that last operation ever properly healed. It's throbbing.
            return 7000
        elif index == 1:
            # $script:0831180509004319$
            # - Do you mind putting this medicated patch on my back? I can't do it myself.
            return 7000
        elif index == 2:
            # $script:0831180509004320$
            # - Whew, thanks. I bet you're curious how I got this injury...
            return 7000
        elif index == 3:
            # $script:0831180509004321$
            # - I was on duty at the guard post when a group of creeps attacked. I'd never seen them before, and they used some kind of strange magic.
            return 7000
        elif index == 4:
            # $script:0831180509004322$
            # - Ah, I'm still not good enough for $npcName:11000015[gender:1]$. I can't protect myself, let alone her...
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509004323$
        # - Halt! Who goes there!
        if pick == 0:
            # $script:0831180509004324$
            # - I know the owner.
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509004325$
            # - Oops, wrong house.
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509004326$
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
