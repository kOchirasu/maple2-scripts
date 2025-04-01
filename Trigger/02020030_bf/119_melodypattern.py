""" trigger/02020030_bf/119_melodypattern.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PatternPick', value=0)
        self.set_user_value(key='Reset', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PatternPick') == 1:
            return MelodyPlay01_Start(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(key='Reset', value=0)


# 퀴즈시작 / 라-파-레-솔-미
class MelodyPlay01_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[11206], visible=True) # Bell F
        self.set_actor(trigger_id=11006, visible=True, initial_sequence='ks_quest_musical_B01_navy') # Bell F

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay01_End(self.ctx)


class MelodyPlay01_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11006, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell F

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay02_Start(self.ctx)


class MelodyPlay02_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[11204], visible=True) # Bell D
        self.set_actor(trigger_id=11004, visible=True, initial_sequence='ks_quest_musical_B01_green') # Bell D

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay02_End(self.ctx)


class MelodyPlay02_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11004, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell D

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay03_Start(self.ctx)


class MelodyPlay03_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[11202], visible=True) # Bell A
        self.set_actor(trigger_id=11002, visible=True, initial_sequence='ks_quest_musical_B01_orange') # Bell A

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay03_End(self.ctx)


class MelodyPlay03_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11002, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell A

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay04_Start(self.ctx)


class MelodyPlay04_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[11205], visible=True) # Bell B
        self.set_actor(trigger_id=11005, visible=True, initial_sequence='ks_quest_musical_B01_blue') # Bell B

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay04_End(self.ctx)


class MelodyPlay04_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11005, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell B

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay05_Start(self.ctx)


class MelodyPlay05_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[11203], visible=True) # Bell HighC
        self.set_actor(trigger_id=11003, visible=True, initial_sequence='ks_quest_musical_B01_yellow') # Bell HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay05_End(self.ctx)


class MelodyPlay05_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11003, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return CheckAnswer01_Start(self.ctx)


# 정답체크 / 라-파-레-솔-미
class CheckAnswer01_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11101, initial_sequence='ks_quest_musical_A01_off') # Dummy Lever C
        self.set_actor(trigger_id=11102, initial_sequence='ks_quest_musical_A01_off') # Dummy Lever D
        self.set_actor(trigger_id=11103, initial_sequence='ks_quest_musical_A01_off') # Dummy Lever E
        self.set_actor(trigger_id=11104, initial_sequence='ks_quest_musical_A01_off') # Dummy Lever F
        self.set_actor(trigger_id=11105, initial_sequence='ks_quest_musical_A01_off') # Dummy Lever G
        self.set_actor(trigger_id=11106, initial_sequence='ks_quest_musical_A01_off') # Dummy Lever A
        self.set_actor(trigger_id=11107, initial_sequence='ks_quest_musical_A01_off') # Dummy Lever B
        self.set_actor(trigger_id=11108, initial_sequence='ks_quest_musical_A01_off') # Dummy Lever HighC
        self.set_interact_object(trigger_ids=[12000058], state=1) # Lever C
        self.set_interact_object(trigger_ids=[12000059], state=1) # Lever D
        self.set_interact_object(trigger_ids=[12000060], state=1) # Lever E
        self.set_interact_object(trigger_ids=[12000061], state=1) # Lever F
        self.set_interact_object(trigger_ids=[12000062], state=1) # Lever G
        self.set_interact_object(trigger_ids=[12000063], state=1) # Lever A
        self.set_interact_object(trigger_ids=[12000064], state=1) # Lever B
        self.set_interact_object(trigger_ids=[12000065], state=1) # Lever HighC
        self.set_user_value(trigger_id=11001, key='PlayC', value=1)
        self.set_user_value(trigger_id=11002, key='PlayD', value=1)
        self.set_user_value(trigger_id=11003, key='PlayE', value=1)
        self.set_user_value(trigger_id=11004, key='PlayF', value=1)
        self.set_user_value(trigger_id=11005, key='PlayG', value=1)
        self.set_user_value(trigger_id=11006, key='PlayA', value=1)
        self.set_user_value(trigger_id=11007, key='PlayB', value=1)
        self.set_user_value(trigger_id=11008, key='PlayHighC', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000058], state=0):
            # C
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000059], state=0):
            # D
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000060], state=0):
            # E
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000061], state=0):
            # F
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000062], state=0):
            # G
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000063], state=0):
            # A
            return CheckAnswer01_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000064], state=0):
            # B
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000065], state=0):
            # HighC
            return AnswerIsWrong_Delay(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)


class CheckAnswer01_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            # SoundEffectDelay
            return CheckAnswer02_Start(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[12000063], state=1) # Lever F


class CheckAnswer02_Start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000058], state=0):
            # C
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000059], state=0):
            # D
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000060], state=0):
            # E
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000061], state=0):
            # F
            return CheckAnswer02_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000062], state=0):
            # G
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000063], state=0):
            # A
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000064], state=0):
            # B
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000065], state=0):
            # HighC
            return AnswerIsWrong_Delay(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)


class CheckAnswer02_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            # SoundEffectDelay
            return CheckAnswer03_Start(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[12000061], state=1) # Lever D


class CheckAnswer03_Start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000058], state=0):
            # C
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000059], state=0):
            # D
            return CheckAnswer03_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000060], state=0):
            # E
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000061], state=0):
            # F
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000062], state=0):
            # G
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000063], state=0):
            # A
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000064], state=0):
            # B
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000065], state=0):
            # HighC
            return AnswerIsWrong_Delay(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)


class CheckAnswer03_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            # SoundEffectDelay
            return CheckAnswer04_Start(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[12000059], state=1) # Lever A


class CheckAnswer04_Start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000058], state=0):
            # C
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000059], state=0):
            # D
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000060], state=0):
            # E
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000061], state=0):
            # F
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000062], state=0):
            # G
            return CheckAnswer04_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000063], state=0):
            # A
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000064], state=0):
            # B
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000065], state=0):
            # HighC
            return AnswerIsWrong_Delay(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)


class CheckAnswer04_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            # SoundEffectDelay
            return CheckAnswer05_Start(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[12000062], state=1) # Lever B


class CheckAnswer05_Start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[12000058], state=0):
            # C
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000059], state=0):
            # D
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000060], state=0):
            # E
            return CheckAnswer05_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000061], state=0):
            # F
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000062], state=0):
            # G
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000063], state=0):
            # A
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000064], state=0):
            # B
            return AnswerIsWrong_Delay(self.ctx)
        if self.object_interacted(interact_ids=[12000065], state=0):
            # HighC
            return AnswerIsWrong_Delay(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)


class CheckAnswer05_Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)
        if self.wait_tick(wait_tick=500):
            # SoundEffectDelay
            return AnswerIsRight(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(trigger_ids=[12000060], state=1) # Lever B


# 정답
class AnswerIsRight(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=11001, key='PlayC', value=0)
        self.set_user_value(trigger_id=11002, key='PlayD', value=0)
        self.set_user_value(trigger_id=11003, key='PlayE', value=0)
        self.set_user_value(trigger_id=11004, key='PlayF', value=0)
        self.set_user_value(trigger_id=11005, key='PlayG', value=0)
        self.set_user_value(trigger_id=11006, key='PlayA', value=0)
        self.set_user_value(trigger_id=11007, key='PlayB', value=0)
        self.set_user_value(trigger_id=11008, key='PlayHighC', value=0)
        self.set_user_value(trigger_id=11000, key='AnswerIsRight', value=1)
        self.set_interact_object(trigger_ids=[12000058], state=0) # Lever C
        self.set_interact_object(trigger_ids=[12000059], state=0) # Lever D
        self.set_interact_object(trigger_ids=[12000060], state=0) # Lever E
        self.set_interact_object(trigger_ids=[12000061], state=0) # Lever F
        self.set_interact_object(trigger_ids=[12000062], state=0) # Lever G
        self.set_interact_object(trigger_ids=[12000063], state=0) # Lever A
        self.set_interact_object(trigger_ids=[12000064], state=0) # Lever B
        self.set_interact_object(trigger_ids=[12000065], state=0) # Lever HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)


# 오답
class AnswerIsWrong_Delay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=11001, key='PlayC', value=0)
        self.set_user_value(trigger_id=11001, key='PlayC', value=0)
        self.set_user_value(trigger_id=11002, key='PlayD', value=0)
        self.set_user_value(trigger_id=11003, key='PlayE', value=0)
        self.set_user_value(trigger_id=11004, key='PlayF', value=0)
        self.set_user_value(trigger_id=11005, key='PlayG', value=0)
        self.set_user_value(trigger_id=11006, key='PlayA', value=0)
        self.set_user_value(trigger_id=11007, key='PlayB', value=0)
        self.set_user_value(trigger_id=11008, key='PlayHighC', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            # SoundEffectDelay
            return AnswerIsWrong(self.ctx)
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)


class AnswerIsWrong(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=11000, key='AnswerIsWrong', value=1)
        self.set_interact_object(trigger_ids=[12000058], state=0) # Lever C
        self.set_interact_object(trigger_ids=[12000059], state=0) # Lever D
        self.set_interact_object(trigger_ids=[12000060], state=0) # Lever E
        self.set_interact_object(trigger_ids=[12000061], state=0) # Lever F
        self.set_interact_object(trigger_ids=[12000062], state=0) # Lever G
        self.set_interact_object(trigger_ids=[12000063], state=0) # Lever A
        self.set_interact_object(trigger_ids=[12000064], state=0) # Lever B
        self.set_interact_object(trigger_ids=[12000065], state=0) # Lever HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)
        if self.user_value(key='Reset') == 0:
            return MelodyPlay01_ReStartDelay01(self.ctx)


# 재도전 딜레이
class MelodyPlay01_ReStartDelay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay01_ReStartDelay02(self.ctx)


class MelodyPlay01_ReStartDelay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[4301], visible=True) # Right Sound Effect
        self.set_actor(trigger_id=11001, visible=True, initial_sequence='ks_quest_musical_B01_red') # Bell C
        self.set_actor(trigger_id=11002, visible=True, initial_sequence='ks_quest_musical_B01_orange') # Bell D
        self.set_actor(trigger_id=11003, visible=True, initial_sequence='ks_quest_musical_B01_yellow') # Bell E
        self.set_actor(trigger_id=11004, visible=True, initial_sequence='ks_quest_musical_B01_green') # Bell F
        self.set_actor(trigger_id=11005, visible=True, initial_sequence='ks_quest_musical_B01_blue') # Bell G
        self.set_actor(trigger_id=11006, visible=True, initial_sequence='ks_quest_musical_B01_navy') # Bell A
        self.set_actor(trigger_id=11007, visible=True, initial_sequence='ks_quest_musical_B01_purple') # Bell B
        self.set_actor(trigger_id=11008, visible=True, initial_sequence='ks_quest_musical_B01_pink') # Bell HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return StartMelodyQuiz_Delay03(self.ctx)


class StartMelodyQuiz_Delay03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=11001, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell C
        self.set_actor(trigger_id=11002, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell D
        self.set_actor(trigger_id=11003, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell E
        self.set_actor(trigger_id=11004, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell F
        self.set_actor(trigger_id=11005, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell G
        self.set_actor(trigger_id=11006, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell A
        self.set_actor(trigger_id=11007, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell B
        self.set_actor(trigger_id=11008, visible=True, initial_sequence='ks_quest_musical_B01_off') # Bell HighC

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reset') == 1:
            return ResetDelay(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return MelodyPlay01_Start(self.ctx)


# 리셋
class ResetDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Wait(self.ctx)


initial_state = Wait
