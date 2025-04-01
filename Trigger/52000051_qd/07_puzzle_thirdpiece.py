""" trigger/52000051_qd/07_puzzle_thirdpiece.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='PickThirdPiece', value=0)
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309]) # Pattern_Ground
        self.set_mesh(trigger_ids=[3310,3311,3312,3313,3314,3315,3316,3317,3318,3319]) # Pattern_LightOn

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PickThirdPiece') == 1:
            return RandomPick(self.ctx)


class RandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=10.0):
            return Pattern01_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern02_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern03_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern04_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern05_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern06_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern07_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern08_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern09_Pick(self.ctx)
        if self.random_condition(weight=10.0):
            return Pattern10_Pick(self.ctx)


# 첫 번째 패턴 뽑힘
class Pattern01_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3300], visible=True) # Pattern_Ground_A01
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptA01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern01_Check(self.ctx)


# 첫 번째 패턴 정답 체크
class Pattern01_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000565):
            # Pattern_A01
            return Pattern01_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000565):
            # 돌이 없거나 정답이 아니면
            return Pattern01_WrongAnswer(self.ctx)


# 첫 번째 패턴 정답
class Pattern01_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3310], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_A01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern01_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 첫 번째 패턴 오답
class Pattern01_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern01_Reset01(self.ctx)


class Pattern01_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern01_Reset02(self.ctx)


# 첫 번째 패턴 다시체크
class Pattern01_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3310], start_delay=100, fade=5.0) # Pattern_LightOn_A01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern01_Check(self.ctx)


# 두 번째 패턴 뽑힘
class Pattern02_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3301], visible=True) # Pattern_Ground_A02
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptA02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern02_Check(self.ctx)


# 두 번째 패턴 정답 체크
class Pattern02_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000566):
            # Pattern_A02
            return Pattern02_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000566):
            # 돌이 없거나 정답이 아니면
            return Pattern02_WrongAnswer(self.ctx)


# 두 번째 패턴 정답
class Pattern02_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3311], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_A02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern02_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 두 번째 패턴 오답
class Pattern02_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern02_Reset01(self.ctx)


class Pattern02_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern02_Reset02(self.ctx)


# 두 번째 패턴 다시체크
class Pattern02_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3311], start_delay=100, fade=5.0) # Pattern_LightOn_A02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern02_Check(self.ctx)


# 세 번째 패턴 뽑힘
class Pattern03_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3302], visible=True) # Pattern_Ground_A03
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptA03', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern03_Check(self.ctx)


# 세 번째 패턴 정답 체크
class Pattern03_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000567):
            # Pattern_A03
            return Pattern03_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000567):
            # 돌이 없거나 정답이 아니면
            return Pattern03_WrongAnswer(self.ctx)


# 세 번째 패턴 정답
class Pattern03_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3312], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_A03

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern03_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 세 번째 패턴 오답
class Pattern03_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern03_Reset01(self.ctx)


class Pattern03_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern03_Reset02(self.ctx)


# 세 번째 패턴 다시체크
class Pattern03_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3312], start_delay=100, fade=5.0) # Pattern_LightOn_A03

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern03_Check(self.ctx)


# 네 번째 패턴 뽑힘
class Pattern04_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3303], visible=True) # Pattern_Ground_B01
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptB01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern04_Check(self.ctx)


# 네 번째 패턴 정답 체크
class Pattern04_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000568):
            # Pattern_B01
            return Pattern04_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000568):
            # 돌이 없거나 정답이 아니면
            return Pattern04_WrongAnswer(self.ctx)


# 네 번째 패턴 정답
class Pattern04_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3313], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_B01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern04_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 네 번째 패턴 오답
class Pattern04_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern04_Reset01(self.ctx)


class Pattern04_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern04_Reset02(self.ctx)


# 네 번째 패턴 다시체크
class Pattern04_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3313], start_delay=100, fade=5.0) # Pattern_LightOn_B01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern04_Check(self.ctx)


# 다섯 번째 패턴 뽑힘
class Pattern05_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3304], visible=True) # Pattern_Ground_B02
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptB02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern05_Check(self.ctx)


# 다섯 번째 패턴 정답 체크
class Pattern05_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000569):
            # Pattern_B02
            return Pattern05_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000569):
            # 돌이 없거나 정답이 아니면
            return Pattern05_WrongAnswer(self.ctx)


# 다섯 번째 패턴 정답
class Pattern05_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3314], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_B02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern05_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 다섯 번째 패턴 오답
class Pattern05_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern05_Reset01(self.ctx)


class Pattern05_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern05_Reset02(self.ctx)


# 다섯 번째 패턴 다시체크
class Pattern05_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3314], start_delay=100, fade=5.0) # Pattern_LightOn_B02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern05_Check(self.ctx)


# 여섯 번째 패턴 뽑힘
class Pattern06_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3305], visible=True) # Pattern_Ground_C01
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptC01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern06_Check(self.ctx)


# 여섯 번째 패턴 정답 체크
class Pattern06_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000570):
            # Pattern_C01
            return Pattern06_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000570):
            # 돌이 없거나 정답이 아니면
            return Pattern06_WrongAnswer(self.ctx)


# 여섯 번째 패턴 정답
class Pattern06_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3315], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_C01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern06_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 여섯 번째 패턴 오답
class Pattern06_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern06_Reset01(self.ctx)


class Pattern06_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern06_Reset02(self.ctx)


# 여섯 번째 패턴 다시체크
class Pattern06_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3315], start_delay=100, fade=5.0) # Pattern_LightOn_C01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern06_Check(self.ctx)


# 일곱 번째 패턴 뽑힘
class Pattern07_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3306], visible=True) # Pattern_Ground_D01
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptD01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern07_Check(self.ctx)


# 일곱 번째 패턴 정답 체크
class Pattern07_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000571):
            # Pattern_D01
            return Pattern07_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000571):
            # 돌이 없거나 정답이 아니면
            return Pattern07_WrongAnswer(self.ctx)


# 일곱 번째 패턴 정답
class Pattern07_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3316], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_D01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern07_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 일곱 번째 패턴 오답
class Pattern07_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern07_Reset01(self.ctx)


class Pattern07_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern07_Reset02(self.ctx)


# 일곱 번째 패턴 다시체크
class Pattern07_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3316], start_delay=100, fade=5.0) # Pattern_LightOn_D01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern07_Check(self.ctx)


# 여덟 번째 패턴 뽑힘
class Pattern08_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3307], visible=True) # Pattern_Ground_D02
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptD02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern08_Check(self.ctx)


# 여덟 번째 패턴 정답 체크
class Pattern08_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000572):
            # Pattern_D02
            return Pattern08_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000572):
            # 돌이 없거나 정답이 아니면
            return Pattern08_WrongAnswer(self.ctx)


# 여덟 번째 패턴 정답
class Pattern08_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3317], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_D02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern08_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 여덟 번째 패턴 오답
class Pattern08_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern08_Reset01(self.ctx)


class Pattern08_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern08_Reset02(self.ctx)


# 여덟 번째 패턴 다시체크
class Pattern08_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3317], start_delay=100, fade=5.0) # Pattern_LightOn_D02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern08_Check(self.ctx)


# 아홉 번째 패턴 뽑힘
class Pattern09_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3308], visible=True) # Pattern_Ground_E01
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptE01', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern09_Check(self.ctx)


# 아홉 번째 패턴 정답 체크
class Pattern09_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000573):
            # Pattern_E01
            return Pattern09_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000573):
            # 돌이 없거나 정답이 아니면
            return Pattern09_WrongAnswer(self.ctx)


# 아홉 번째 패턴 정답
class Pattern09_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3318], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_E01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern09_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 아홉 번째 패턴 오답
class Pattern09_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern09_Reset01(self.ctx)


class Pattern09_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern09_Reset02(self.ctx)


# 아홉 번째 패턴 다시체크
class Pattern09_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3318], start_delay=100, fade=5.0) # Pattern_LightOn_E01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern09_Check(self.ctx)


# 열 번째 패턴 뽑힘
class Pattern10_Pick(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3309], visible=True) # Pattern_Ground_E02
        self.set_user_value(trigger_id=8, key='PickFourthPieceExceptE02', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern10_Check(self.ctx)


# 열 번째 패턴 정답 체크
class Pattern10_Check(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[2003], item_id=30000574):
            # Pattern_E02
            return Pattern10_CorrectAnswer(self.ctx)
        if not self.detect_liftable_object(box_ids=[2003], item_id=30000574):
            # 돌이 없거나 정답이 아니면
            return Pattern10_WrongAnswer(self.ctx)


# 열 번째 패턴 정답
class Pattern10_CorrectAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=1) # 정답
        self.set_mesh(trigger_ids=[3319], visible=True, start_delay=100, fade=5.0) # Pattern_LightOn_E02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ResetThirdPiece') == 1:
            return Pattern10_Reset01(self.ctx)
        if self.user_value(key='LockThirdPiece') == 1:
            return Quit(self.ctx)


# 열 번째 패턴 오답
class Pattern10_WrongAnswer(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=4, key='CorrectThirdPiece', value=2) # 오답

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Pattern10_Reset01(self.ctx)


class Pattern10_Reset01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CheckThirdPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='ResetThirdPiece', value=0)
        self.set_user_value(key='LockThirdPiece', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Pattern10_Reset02(self.ctx)


# 열 번째 패턴 다시체크
class Pattern10_Reset02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3319], start_delay=100, fade=5.0) # Pattern_LightOn_E02

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheckThirdPiece') == 1:
            return Pattern10_Check(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
