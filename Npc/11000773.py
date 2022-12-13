""" 11000773: Shadow Doc """
from npc_api import Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __1(self, index: int, pick: int) -> int:
        # $script:0831180509002564$
        # - ...Did you call me?
        if pick == 0:
            # $script:0831180509002565$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002566$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002567$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __2(self, index: int, pick: int) -> int:
        # $script:0831180509002568$
        # - Are you wounded?
        if pick == 0:
            # $script:0831180509002569$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002570$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002571$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __3(self, index: int, pick: int) -> int:
        # $script:0831180509002572$
        # - Please stop bothering me.
        if pick == 0:
            # $script:0831180509002573$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002574$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002575$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __4(self, index: int, pick: int) -> int:
        # $script:0831180509002576$
        # - ...Did you call me?
        if pick == 0:
            # $script:0831180509002577$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002578$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002579$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002580$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, index: int, pick: int) -> int:
        # $script:0831180509002581$
        # - Are you wounded?
        if pick == 0:
            # $script:0831180509002582$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002583$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002584$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002585$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, index: int, pick: int) -> int:
        # $script:0831180509002586$
        # - Please stop bothering me.
        if pick == 0:
            # $script:0831180509002587$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002588$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002589$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002590$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, index: int, pick: int) -> int:
        # $script:0831180509002591$
        # - Did you just say you want to pay me?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509002592$
            # - Let me think about it some more.
            # TODO: goto 8040, 8050, 8060, 9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002593$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000, 8001, 8010, 8011, 8901
            # TODO: gotoFail 8900, 8910
            return 8900, 8910
        return -1

    def __8000(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002594$
        # - You've made a good decision. You scratch my back, I'll scratch yours. Heh. Heh. 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002595$
        # - I like staying with you. Our relationship is mutually beneficial, you know. Heh. Heh.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8010(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002596$
        # - I won't hold a grudge against you for neglecting me. Our relationship is strictly business, and I like that we keep a professional distance from each other. 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002597$
        # - Ah, I was getting ready to go to the Land of Darkness. Now I have to unpack everything, thanks to your indecisiveness.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __8020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002598$
        # - I got only a few days left to work here in this house. Time passes really quickly. Heh. 
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __8021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002599$
        # - But then, not really news, is it? 
        if pick == 0:
            # $script:0831180509002600$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002601$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002602$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002603$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, index: int, pick: int) -> int:
        # $script:0831180509002604$
        # - What do you want?
        if pick == 0:
            # $script:0831180509002605$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002606$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002607$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002608$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, index: int, pick: int) -> int:
        # $script:0831180509002609$
        # - I'm listening.
        if pick == 0:
            # $script:0831180509002610$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002611$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002612$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002613$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, index: int, pick: int) -> int:
        # $script:0831180509002614$
        # - Would you stop bothering me?
        if pick == 0:
            # $script:0831180509002615$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002616$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002617$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002618$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8901(self, index: int, pick: int) -> int:
        # $script:0831180509002620$
        # - Tsk, tsk. Have you heard of short-term memory loss? You've already paid me this month. You should've let me operate on you when I offered.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9001(self, index: int, pick: int) -> int:
        # $script:0831180509002623$
        # - It's been $MaidPassedDay$. Maybe it's time I move on...
        if pick == 0:
            # $script:0831180509002624$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002625$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002626$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9002(self, index: int, pick: int) -> int:
        # $script:0831180509002627$
        # - You still look like mushroom droppings. Then again, who am I to talk?
        if pick == 0:
            # $script:0831180509002628$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002629$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002630$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9003(self, index: int, pick: int) -> int:
        # $script:0831180509002631$
        # - First I lose my medical license, and now I'm losing my job as a housekeeper. Go figure. 
        if pick == 0:
            # $script:0831180509002632$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002633$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002634$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9011(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002636$
        # - Did you really think you could fool me with such shallow trickery? I know our contract has expired. 
        return -1

    def __9020(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002637$
        # - First you lose your place in society, then you lose your home, and then you even lose all the people you love. Such is life.
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __9021(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002638$
        # - You think that's never going to happen to you? Think again. 
        if pick == 0:
            # $script:0831180509002639$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002640$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002641$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9040(self, index: int, pick: int) -> int:
        # $script:0831180509002642$
        # - ...You're more talkative than usual today.
        if pick == 0:
            # $script:0831180509002643$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509002644$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002645$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __9030(self, index: int, pick: int) -> int:
        # $script:0831180509002646$
        # - I'm a skilled medical professional and you're not taking advantage of that. What a shame! 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9031(self, index: int, pick: int) -> int:
        # $script:0831180509002647$
        # - When one has no money, one cannot hire a housekeeper or receive medical treatment... or save a person one loves. 
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __9032(self, index: int, pick: int) -> int:
        # $script:0831180509002648$
        # - Patients are the worse. Half of them want treatment and then don't pay. That's why I ask for money upfront.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060, 9040
        return -1

    def __10(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002649$
        # - Want a potion that will make your head spin? Literally spin?
        # TODO: gotoConditionTalkID 11, 9011
        return -1

    def __11(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002650$
        # - Just say the word.
        # TODO: gotoConditionTalkID 40, 50, 60, 8040, 8050, 8060
        return -1

    def __20(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002651$
        # - Why do you want to know about my past?
        # TODO: gotoConditionTalkID 21, 22, 8021, 9021
        return -1

    def __21(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002652$
        # - You look horrible.
        if pick == 0:
            # $script:0831180509002653$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002654$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002655$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __22(self, index: int, pick: int) -> int:
        # functionID=1 
        # $script:0831180509002656$
        # - You look horrible.
        if pick == 0:
            # $script:0831180509002657$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002658$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002659$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        elif pick == 3:
            # $script:0831180509002660$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, index: int, pick: int) -> int:
        # $script:0831180509002661$
        # - I have nothing to tell you.
        if pick == 0:
            # $script:0831180509002662$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509002663$
            # - (Ask for treatment.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509002664$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509002665$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __31(self, index: int, pick: int) -> int:
        # $script:0831180509002666$
        # - This is dull, dull, dull.
        if pick == 0:
            # $script:0831180509002667$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509002668$
            # - (Ask for treatment.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509002669$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509002670$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __32(self, index: int, pick: int) -> int:
        # $script:0831180509002671$
        # - If you have something to say, spit it out!
        if pick == 0:
            # $script:0831180509002672$
            # - Anything interesting happen today?
            # TODO: goto 1000, 1100, 2000, 2100, 2200, 9011
            return -1
        elif pick == 1:
            # $script:0831180509002673$
            # - (Ask for treatment.)
            # TODO: goto 3000, 3100, 4000, 4100, 9011
            return -1
        elif pick == 2:
            # $script:0831180509002674$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000, 5100, 6000, 6100, 7000, 9011
            return -1
        elif pick == 3:
            # $script:0831180509002675$
            # - Back.
            # TODO: goto 8040, 8050, 8060, 40, 50, 60, 9040
            return -1
        return -1

    def __40(self, index: int, pick: int) -> int:
        # $script:0831180509002676$
        # - What do you want?
        if pick == 0:
            # $script:0831180509002677$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002678$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002679$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __50(self, index: int, pick: int) -> int:
        # $script:0831180509002680$
        # - I'm listening.
        if pick == 0:
            # $script:0831180509002681$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002682$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002683$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __60(self, index: int, pick: int) -> int:
        # $script:0831180509002684$
        # - Would you stop bothering me?
        if pick == 0:
            # $script:0831180509002685$
            # - I need you to craft something.
            # TODO: goto 10, 9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002686$
            # - I want to check your profile.
            # TODO: goto 20, 8020, 9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002687$
            # - Let's chat!
            # TODO: goto 30, 31, 32, 9030, 9031, 9032
            return -1
        return -1

    def __1000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002688$
            # - The nerve! The mistreatment! Do they have any idea who they're dealing with?!
            return 1000
        elif index == 1:
            # $script:0831180509002689$
            # - A former patient barged into your house today. He claimed I had made him worse! He called me a quack! A quack!! Can you imagine?
            return 1000
        elif index == 2:
            # $script:0831180509002690$
            # - It was everything I could do not to throw a bottle of ketchup at him. What do you think? Am I a quack?
            if pick == 0:
                # $script:0831180509002691$
                # - No, but your personality could use some work.
                # TODO: goto 1011, 1012
                return -1
            elif pick == 1:
                # $script:0831180509002692$
                # - Hmm, you might be a quack...
                # TODO: goto 1001, 1002
                return -1
            return -1
        return -1

    def __1001(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002693$
        # - What?! Where's that bottle of ketchup?!
        return -1

    def __1002(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002694$
        # - That's harsh. If I'm a quack, maybe I should stop treating you for a while, see how you like it.
        return -1

    def __1011(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002695$
        # - Who cares about personality? It's about skills! I can't believe I let him talk to me like that... I'm losing my touch.
        return -1

    def __1012(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002696$
        # - You're not afraid to speak your mind, are you? Heh. Heh. Heh.
        return -1

    def __1100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002697$
            # - What do you know about the Land of Darkness?
            return 1100
        elif index == 1:
            # $script:0831180509002698$
            # - A gateway has opened to that dangerous world. Not much is known, but I believe incredible treasure hides in that world...
            return 1100
        elif index == 2:
            # $script:0831180509002699$
            # - And the Alliance is too frightened to go find it! They won't let anyone else go, either. Isn't that idiotic?!
            if pick == 0:
                # $script:0831180509002700$
                # - It's good to be cautious.
                # TODO: goto 1101, 1102
                return -1
            elif pick == 1:
                # $script:0831180509002701$
                # - I completely agree with you.
                # TODO: goto 1111, 1112
                return -1
            return -1
        return -1

    def __1101(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002702$
        # - Hmpf! You're just as cowardly as they are!
        return -1

    def __1102(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002703$
        # - Are you afraid? At least you're honest about it.
        return -1

    def __1111(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002704$
        # - Heh, heh! I knew we spoke the same language!
        return -1

    def __1112(self, index: int, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509002705$
        # - Ah... So you're as dangerous as I am. Heh, heh!
        return -1

    def __2000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002706$
            # - Some teenager barged into the house today.
            return 2000
        elif index == 1:
            # $script:0831180509002707$
            # - He was pale and his eyes were a bit crazed. He started yelling for a doctor.
            return 2000
        elif index == 2:
            # $script:0831180509002708$
            # - I told him I was a doctor and that he didn't have to yell. He told me to treat him. He acted like he was going to die if I didn't.
            return 2000
        elif index == 3:
            # $script:0831180509002709$
            # - But I'm the ruthless $MaidName$!
            return 2000
        elif index == 4:
            # $script:0831180509002710$
            # - I told him he had to pay me first. He begged me on his hands and knees, then left when he realized he couldn't change my mind. He didn't even apologize when he left!
            return 2000
        elif index == 5:
            # $script:0831180509002711$
            # - Young folks these days are so spoiled. They think they can get everything for free. I really hope he's not dead out there somewhere, though.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002712$
            # - Today was a productive day. I treated so many patients. My wallet is bursting with mesos.
            return 2100
        elif index == 1:
            # $script:0831180509002713$
            # - Some of them were attacked by monsters. Some fell from high places. One tripped into lava.
            return 2100
        elif index == 2:
            # $script:0831180509002714$
            # - When you're hurt, you have no choice but to find the closest doctor you can, no matter how much he charges, heh heh heh heh.
            return 2100
        elif index == 3:
            # $script:0831180509002715$
            # - That's why I like staying here with you. Our relationship is mutually beneficial, you know.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __2200(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002716$
            # - A bunch of angry militia members barged in here today. They said this was my last warning. Next time they would arrest me.
            return 2200
        elif index == 1:
            # $script:0831180509002717$
            # - My crimes? Overcharging my patients and... having ketchup stains on my clothes, which supposely distresses our neighbors!
            return 2200
        elif index == 2:
            # $script:0831180509002718$
            # - It's nonsense. I charge my patients what I think I'm worth, and I'm worth more than most doctors.
            return 2200
        elif index == 3:
            # $script:0831180509002719$
            # - And they're making fun of my clothes now? What are they, children?
            return 2200
        elif index == 4:
            # $script:0831180509002720$
            # - The idiocy of this world boggles my mind. Well! They can threaten me all they want, I'm not budging.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __3000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002721$
            # - I'll treat you for free, but it's just this once. No more freebies after this.
            return 3000
        elif index == 1:
            # $script:0831180509002722$
            # - Let's see... Hm... Was it here? 
            #   <font color="#909090">(He digs around, searching for something.)</font>
            return 3000
        elif index == 2:
            # $script:0831180509002723$
            # - This is bad. Really bad. We need to operate right away.
            return 3000
        elif index == 3:
            # functionID=1 openTalkReward=True 
            # $script:0831180509002724$
            # - You have a serious, serious case of... hypochondria! Hah hah!
            return -1
        return -1

    def __3100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002725$
            # - Sure, $OwnerName$, and I'll add the bill to my monthly salary.
            return 3100
        elif index == 1:
            # $script:0831180509002726$
            # - I have a few questions for you. One, do you feel constantly tired, no matter how much you sleep?
            return 3100
        elif index == 2:
            # $script:0831180509002727$
            # - Oh, you do? I see. Two, do you have bouts of dizziness and lack of appetite?
            return 3100
        elif index == 3:
            # $script:0831180509002728$
            # - I see, I see. Finally, three, do you find yourself more forgetful these days?
            return 3100
        elif index == 4:
            # $script:0831180509002729$
            # - I see. Heh. Heh. Just as I suspected.
            return 3100
        elif index == 5:
            # functionID=1 openTalkReward=True 
            # $script:0831180509002730$
            # - You're not sick, $OwnerName$. You're aging. Hah, hah.
            return -1
        return -1

    def __4000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002731$
            # - You can pay, right? If you don't have money, don't expect me to treat you.
            return 4000
        elif index == 1:
            # $script:0831180509002732$
            # - You think people's lives and health are more important than mesos...
            return 4000
        elif index == 2:
            # $script:0831180509002733$
            # - I was like you once, naive and believing the best in people...
            return 4000
        elif index == 3:
            # $script:0831180509002734$
            # - It doesn't matter now. The fact is, I'm not treating anyone unless I'm paid.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __4100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002735$
            # - Uh oh, not good. You're a tiny bit sniffly and the slightest bit warm. You need an operation at once!
            return 4100
        elif index == 1:
            # $script:0831180509002736$
            # - We don't have time to discuss details about the illness. You wouldn't know it even if I told you. The important thing now is to put you under as fast as we can!
            return 4100
        elif index == 2:
            # $script:0831180509002737$
            # - Why do you keep resisting? Don't you trust me?
            return 4100
        elif index == 3:
            # $script:0831180509002738$
            # - Fine, we'll do it later. That's your choice, but let me tell you, you're going to regret it... Tsk.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002739$
            # - You keep looking at the stains on my shirt.
            return 5000
        elif index == 1:
            # $script:0831180509002740$
            # - Don't look so queasy. It's just ketchup. 
            return 5000
        elif index == 2:
            # $script:0831180509002741$
            # - I just love ketchup. Sweet and tangy, with that cool texture sliding down your throat. I have to eat some every time I get a craving, and trust me, that happens a lot.
            return 5000
        elif index == 3:
            # $script:0831180509002742$
            # - $OwnerName$, you want some? Don't be shy. Open wide, and I'll squeeze some into your mouth. Come on, aaaaah.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __5100(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002743$
            # - My patients in the Land of Darkness generally suffer from more serious ailments than the ones from other parts of Maple World.
            return 5100
        elif index == 1:
            # $script:0831180509002744$
            # - That's not surprising. They're wounded by the thralls of the Shadow Domination, after all.
            return 5100
        elif index == 2:
            # $script:0831180509002745$
            # - Shadow Power is no joke. You can't resist it. Those who try, pay dearly.
            return 5100
        elif index == 3:
            # $script:0831180509002746$
            # - If you must ever venture into the Land of Darkness, be extra cautious. Move in shadows. Do not draw attention to yourself.
            return 5100
        elif index == 4:
            # $script:0831180509002747$
            # - Don't be like the fools who trust in their own strength, thinking they can handle what comes at them. They always end up in my office.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __6000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002748$
            # - You want to know why I practice in a dangerous place like the Land of Darkness?
            return 6000
        elif index == 1:
            # $script:0831180509002749$
            # - Because of rest of Maple World is filled with blockheads. I can't stand it!
            return 6000
        elif index == 2:
            # $script:0831180509002750$
            # - I used to use $item:20000046$ to help my patients deal with pain. It's surprisingly effective.
            return 6000
        elif index == 3:
            # $script:0831180509002751$
            # - It was an act of compassion, but the association revoked my license for using a banned drug.
            return 6000
        elif index == 4:
            # $script:0831180509002752$
            # - It's just as well. I didn't like being a member of their organization anyway. Heh heh.
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __7000(self, index: int, pick: int) -> int:
        if index == 0:
            # $script:0831180509002753$
            # - My family is gone. It's my fault. 
            return 7000
        elif index == 1:
            # $script:0831180509002754$
            # - I had a daughter once. She had a laugh that would melt anyone's heart.
            return 7000
        elif index == 2:
            # $script:0831180509002755$
            # - She was sick. Her illness was supposedly incurable.
            return 7000
        elif index == 3:
            # $script:0831180509002756$
            # - I researched like a madman, until I learned of a mysterious herb that grows only in the Shadow World. It would have healed her.
            return 7000
        elif index == 4:
            # $script:0831180509002757$
            # - But nothing from that world could be brought to this one. We're not allowed to even enter that world, let alone use items found there...
            return 7000
        elif index == 5:
            # $script:0831180509002758$
            # - I lost my daughter because I was too afraid to break the law. Hah. How stupid is that?
            # TODO: gotoConditionTalkID 30, 31, 32, 9011
            return -1
        return -1

    def __100(self, index: int, pick: int) -> int:
        # $script:0831180509002759$
        # - Yeesh, you look awful.
        if pick == 0:
            # $script:0831180509002760$
            # - Help... me... please!
            # TODO: goto 101, 102
            return -1
        elif pick == 1:
            # $script:0831180509002761$
            # - Don't worry about me. I'm fine.
            # TODO: goto 103, 104
            return -1
        elif pick == 2:
            # $script:0831180509002762$
            # - Who are you?
            # TODO: goto 105, 106
            return -1
        return -1

