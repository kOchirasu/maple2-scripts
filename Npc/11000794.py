""" 11000794: Yoyo """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509005839$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509005840$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005841$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005842$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509005843$
        # - What's wrong?
        if pick == 0:
            # $script:0831180509005844$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005845$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005846$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509005847$
        # - Beh, I wondered who it was, but it was just you, $OwnerName$.
        if pick == 0:
            # $script:0831180509005848$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005849$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005850$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509005851$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509005852$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005853$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005854$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005855$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509005856$
        # - What's wrong?
        if pick == 0:
            # $script:0831180509005857$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005858$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005859$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005860$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509005861$
        # - Beh, I wondered who it was, but it was just you, $OwnerName$.
        if pick == 0:
            # $script:0831180509005862$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005863$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005864$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005865$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509005866$
        # - Are you really going to pay me?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509005867$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005868$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005869$
        # - Yippee! I'm going to go show my paycheck to $npcName:11000368[gender:0]$! And I'm going to treat him to some delicious food! $OwnerName$, you're the best. Thanks!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005870$
        # - Hee hee! I'm so happy! I'm going to go shop today. I want to make some new shoes. $OwnerName$, I'll make you a pair too!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005871$
        # - Really? Is this for me? Then... I can make things again, can't I? I'm happy, even if this is just a dream! I feel as if I can make any of my illusions real!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005872$
        # - Mm? $OwnerName$... I-I'm sorry I misunderstood you... I thought you hated me. As a token of apology, I'll grant you a wish. Tell me when you want to use it!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005873$
        # - I'm worried. I want to buy some crafting materials, but I don't have money.  I'll just wait until I get my next paycheck... 
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005874$
        # - D-don't worry about it! I was just talking to myself!
        if pick == 0:
            # $script:0831180509005875$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005876$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005877$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005878$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509005879$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509005880$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005881$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005882$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005883$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509005884$
        # - Are you bored?
        if pick == 0:
            # $script:0831180509005885$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005886$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005887$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005888$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509005889$
        # - I'm listening.
        if pick == 0:
            # $script:0831180509005890$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005891$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005892$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005893$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509005895$
        # - $OwnerName$, please don't do this. You already paid me. I guess I could just take it, but I'm a good fairfolk and I don't like to be dishonest. Pay me a compliment instead!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509005898$
        # - It's been $MaidPassedDay$... I feel weak... 
        if pick == 0:
            # $script:0831180509005899$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005900$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005901$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509005902$
        # - $OwnerName$, do you hate me? 
        if pick == 0:
            # $script:0831180509005903$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005904$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005905$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509005906$
        # - Why did you summon me? I don't even have the energy to talk...  
        if pick == 0:
            # $script:0831180509005907$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005908$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005909$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005911$
        # - That's not impooooortant. Our contract expired, and I have no moneeeeey to spend.  This is soooo depressing... 
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005912$
        # - I don't know what to do. I can't do anything... 
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005913$
        # - $OwnerName$, what do you do all day? Can I join you? 
        if pick == 0:
            # $script:0831180509005914$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005915$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005916$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509005917$
        # - Stop talking to me. I'm not happy with you. 
        if pick == 0:
            # $script:0831180509005918$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509005919$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005920$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509005921$
        # - Since I've got nothing to do, I keep zoning out. But if I'm not paying attention, the illusions I cast on this house might disappear, and then I'll be doomed! I don't want you to find out about all the holes in the walls...
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509005922$
        # - I'm hungry... I'm still growing, so I need to eat well or I might be stunted for life. I want to grow tall! 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509005923$
        # - What if I forget how to make shoes because I haven't been practicing? I want to make shoes. $OwnerName$, don't you want me to make shoes?
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005924$
        # - My shoe-making skills are famous amongst fairies.
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005925$
        # - Ask me any time!
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005926$
        # - What are you so curious about?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005927$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509005928$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005929$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005930$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509005931$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509005932$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005933$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005934$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509005935$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509005936$
        # - Do you have something to say to me?
        if pick == 0:
            # $script:0831180509005937$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509005938$
            # - (Talk about illusionism.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509005939$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509005940$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509005941$
        # - I have a feeling something's going to happen today.
        if pick == 0:
            # $script:0831180509005942$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509005943$
            # - (Talk about illusionism.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509005944$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509005945$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509005946$
        # - I hope $npcName:11000368[gender:0]$ will come visit the house.
        if pick == 0:
            # $script:0831180509005947$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509005948$
            # - (Talk about illusionism.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509005949$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509005950$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509005951$
        # - Did you call me?
        if pick == 0:
            # $script:0831180509005952$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005953$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005954$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509005955$
        # - Are you bored?
        if pick == 0:
            # $script:0831180509005956$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005957$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005958$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509005959$
        # - I'm listening.
        if pick == 0:
            # $script:0831180509005960$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509005961$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509005962$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005963$
            # - $OwnerName$, I need your opinion on something.
            return 1000
        elif index == 1:
            # $script:0831180509005964$
            # - My dream is to go to $map:2000100$. I've heard it's filled with beautiful shiny things. I'd love to see it with my own eyes.
            return 1000
        elif index == 2:
            # $script:0831180509005965$
            # - But $npcName:11000368[gender:0]$ says I can't. It's too dangerous. $OwnerName$, what do you think? Can I go to $map:2000100$?
            if pick == 0:
                # $script:0831180509005966$
                # - No.
                # TODO: goto 1001, 1002
                return -1
            elif pick == 1:
                # $script:0831180509005967$
                # - Only if I go with you.
                # TODO: goto 1011, 1012
                return -1
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005968$
        # - $OwnerName$, you're just like $npcName:11000368[gender:0]$! Both of you think I'm too weak to do anything, and it makes me so mad!
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005969$
        # - The more you say no, the more I want to do it. That's the way a fairy is! Ugh, I want to go there. I want to go there. I really want to go there!
        return -1

    def __1011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005970$
        # - Really?! You're going with me? Then let's go! I want to go right now!
        return -1

    def __1012(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005971$
        # - Really? Yippee! I am sooooo so so so happy right now!
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005972$
            # - This is bad... What do I do?
            return 1100
        elif index == 1:
            # $script:0831180509005973$
            # - I use illusions to help people, but I keep getting them in trouble. I'm a disgrace to the fairfolk.
            return 1100
        elif index == 2:
            # $script:0831180509005974$
            # - Maybe I should stop messing with illusions altogether. 
            if pick == 0:
                # $script:0831180509005975$
                # - You're overreacting.
                # TODO: goto 1111, 1112
                return -1
            elif pick == 1:
                # $script:0831180509005976$
                # - Maybe... a little?
                # TODO: goto 1101, 1102
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005977$
        # - You don't have to say it. I already know it. Words can cut deep, you know.
        return -1

    def __1102(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005978$
        # - You're so insensitive, $OwnerName$. Maybe that's why your face is so ugly. Hmph.
        return -1

    def __1111(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005979$
        # - Do you mean that? Really? I wish everyone was more like you, $OwnerName$.
        return -1

    def __1112(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509005980$
        # - Thank you, $OwnerName$. I feel much better now.
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005981$
            # - A friend of mine came to see me for the first time after a long time. His name is $npcName:11000368[gender:0]$ and he lives in $map:02000017$.
            return 2000
        elif index == 1:
            # $script:0831180509005982$
            # - He's round and furry. I love him very much. $OwnerName$, have you met him by any chance?
            return 2000
        elif index == 2:
            # $script:0831180509005983$
            # - I was so happy to see him that I danced. But then I noticed that $npcName:11000368[gender:0]$ looked very sad.
            return 2000
        elif index == 3:
            # $script:0831180509005984$
            # - $npcName:11000368[gender:0]$ said humans are destroying the forest and that a lot of the zelkovas and willows are gone now.
            return 2000
        elif index == 4:
            # $script:0831180509005985$
            # - I can't imagine losing my friends. I just said "see you later!" to them a few days ago...
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005986$
            # - Not a thing... I may have cracked the wall over there... 
            return 2100
        elif index == 1:
            # $script:0831180509005987$
            # - S-sorry! It's all my fault!! Wahhhh!
            return 2100
        elif index == 2:
            # $script:0831180509005988$
            # - I wanted to know if the $item:30000104$ $npcName:11000368[gender:0]$ gave me was real, so I threw it at the tree in the back of the house... All of it.
            return 2100
        elif index == 3:
            # $script:0831180509005989$
            # - The tree grew taller than the house in the blink of an eye! I thought I was going to be swallowed alive!
            return 2100
        elif index == 4:
            # $script:0831180509005990$
            # - $npcName:11000368[gender:0]$ said I should be careful... I should've listened to him. This is all because I didn't trust my friend.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005991$
            # - $OwnerName$! $OwnerName$! I've got something for you!
            return 2200
        elif index == 1:
            # $script:0831180509005992$
            # - Tah-dah! I made these shoes for you! I've even embroidered your name right here, $OwnerName$. Try them on!
            return 2200
        elif index == 2:
            # $script:0831180509005993$
            # - ...
            #   ...
            #   ...
            #   They don't fit... $OwnerName$, your feet are too big.
            return 2200
        elif index == 3:
            # $script:0831180509005994$
            # - I thought you were the same size as me. I was wrong. I'm sad now. Waaahhh!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __3000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005995$
            # - My illusions don't last forever because they're thoughts from my head given shape and form.
            return 3000
        elif index == 1:
            # $script:0831180509005996$
            # - And thoughts never last long. To keep my illusions up, I have to think about them constantly, but my head gets filled with new thoughts all the time.
            return 3000
        elif index == 2:
            # $script:0831180509005997$
            # - Some of the other fairies have such great concentration they can retain illusions for a very long time, but not me.
            return 3000
        elif index == 3:
            # functionID=1 openTalkReward=True 
            # $script:0831180509005998$
            # - I'm doomed! I made a hole in the wall, so I placed an illusion on it. Now the illusion's gone because I was distracted for a second. Waaaah.
            return -1
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509005999$
            # - It's not easy to cast illusions. I have to be happy, or my thoughts won't materialize.
            return 3100
        elif index == 1:
            # $script:0831180509006000$
            # - The more exciting a thought, the easier it is to materialize it. That's why I can't resurrect the dead or hurt people with my illusions. Even if I could, I would never do it.
            return 3100
        elif index == 2:
            # functionID=1 openTalkReward=True 
            # $script:0831180509006001$
            # - Humans often think fairies are mischievous because of our illusionism. But it's entertaining, isn't it? Heh heh!
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509006002$
            # - I can cast illusions. All fairies can.
            return 4000
        elif index == 1:
            # $script:0831180509006003$
            # - Illusionism is not magic. They're two different things.
            return 4000
        elif index == 2:
            # $script:0831180509006004$
            # - The fairies of Ellinia use magic. It's the great—and scary—power of nature.
            return 4000
        elif index == 3:
            # $script:0831180509006005$
            # - But we use illusionism, a mysterious and interesting power unique to us.
            return 4000
        elif index == 4:
            # $script:0831180509006006$
            # - Illusionism enables us to materialize the thoughts in our heads. The problem is that you can't always perfectly control your thoughts. You have to be careful when you cast illusions.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509006007$
            # - Did you just ask me to cast an illusion? Did you really?
            return 4100
        elif index == 1:
            # $script:0831180509006008$
            # - All right! Count on me! Now, what kind of illusion do you want?
            return 4100
        elif index == 2:
            # $script:0831180509006009$
            # - You want to grow taller? That's easy, $OwnerName$! Real easy!
            return 4100
        elif index == 3:
            # $script:0831180509006010$
            # - Abracadingdong!
            #   Yaliyali pingpong!
            #   Grow tall!
            return 4100
        elif index == 4:
            # $script:0831180509006011$
            # - I-I'm sorry... Only your head grew bigger... Actually it was big before, and now it's even bigger... 
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509006012$
            # - I thought I was the only fairfolk who loses shoes all the time, but I'm not.
            return 5000
        elif index == 1:
            # $script:0831180509006013$
            # - Sometimes I can hear one of the fairfolk crying about lost shoes somewhere near $map:02000023$. $OwnerName$, could you go help her?
            return 5000
        elif index == 2:
            # $script:0831180509006014$
            # - From her voice, I can tell she's a pretty fairfolk. Ahem, $OwnerName$, you look like you're too busy to help her. I'll go.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509006015$
            # - I'm so scared of humans. I can't help it! You're scary and I'm shy!
            return 5100
        elif index == 1:
            # $script:0831180509006016$
            # - But, $OwnerName$, you're different. You're kind and affectionate. I hope all humans can be more like you. 
            return 5100
        elif index == 2:
            # $script:0831180509006017$
            # - But I'm not ready to meet them. Once, a human swindled me out of all my money. 
            return 5100
        elif index == 3:
            # $script:0831180509006018$
            # - $OwnerName$, I know you're good, but I can't trust the others of your kind. 
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509006019$
            # - Some fairies hibernate. $npcName:11000368[gender:0]$ does. So does $npcName:11000677$.
            return 6000
        elif index == 1:
            # $script:0831180509006020$
            # - They say they can't stop themselves from falling asleep. I don't hibernate, so I wouldn't know.
            return 6000
        elif index == 2:
            # $script:0831180509006021$
            # - They get really irritated if their sleep is interrupted. Some fairies even attack anyone who wakes them up.
            return 6000
        elif index == 3:
            # $script:0831180509006022$
            # - So if you see some fairies hibernating, you'd better let them sleep. Got it?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509006023$
            # - $npcName:11000368[gender:0]$ keeps telling everyone that I'm timid, and it's getting on my nerves! I'm not timid at all!
            return 7000
        elif index == 1:
            # $script:0831180509006024$
            # - Remember how I spent all of last Friday preparing dinner for you, $OwnerName$? And you said the soup was salty? See? I'm bold! I'm not too timid to use a lot of salt! 
            return 7000
        elif index == 2:
            # $script:0831180509006025$
            # - You know what, I don't care what $npcName:11000368[gender:0]$ says. I'm not upset at him.
            return 7000
        elif index == 3:
            # $script:0831180509006026$
            # - I mean it! I know I'm not the timid fairfolk he thinks I am! I'm bold... and I'm magnanimous and forgiving! That's right, I'm pretty amazing!
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509006027$
        # - A s-stranger...?! D-did you come for me?!
        if pick == 0:
            # $script:0831180509006028$
            # - Yep!
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509006029$
            # - Nope!
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509006030$
            # - Who are you?
            # TODO: goto 105, 106
            return -1
        return -1

