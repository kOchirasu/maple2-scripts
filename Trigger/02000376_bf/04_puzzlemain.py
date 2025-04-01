""" trigger/02000376_bf/04_puzzlemain.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='CorrectFouthPiece', value=0)
        self.set_effect(trigger_ids=[5002]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5003]) # Pattern_LightOn
        self.set_interact_object(trigger_ids=[10001023], state=0) # Lever
        self.set_user_value(key='PuzzleStart', value=0)
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109]) # Quiz
        self.set_mesh(trigger_ids=[3001,3002,3003,3004]) # BaseRock
        self.set_mesh(trigger_ids=[3020]) # LionStone

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PuzzleStart') == 1:
            return StartPuzzle(self.ctx)


class StartPuzzle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 두 번째 문양은 첫 번째 뽑힌 문양을 제외하고 6번 트리거에서 뽑음 , 중복 2개 제한 장치
        self.set_user_value(trigger_id=5, key='PickFirstPiece', value=1)
        # 네 번째 문양은 세 번째 뽑힌 문양을 제외하고 8번 트리거에서 뽑음 , 중복 2개 제한 장치
        self.set_user_value(trigger_id=7, key='PickThirdPiece', value=1)
        self.set_interact_object(trigger_ids=[10001023], state=1) # Lever
        self.set_mesh(trigger_ids=[3020], visible=True) # LionStone
        self.set_effect(trigger_ids=[5002], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001023], state=0):
            return CheckAnswer01(self.ctx)


class CheckAnswer01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3020], start_delay=200) # LionStone
        self.set_user_value(trigger_id=5, key='CheckFirstPiece', value=1)
        self.set_user_value(trigger_id=6, key='CheckSecondPiece', value=1)
        self.set_user_value(trigger_id=7, key='CheckThirdPiece', value=1)
        self.set_user_value(trigger_id=8, key='CheckFourthPiece', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return CheckAnswer02(self.ctx)


# 순차적으로 체크
class CheckAnswer02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CorrectFirstPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFouthPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFirstPiece') == 1:
            return CheckAnswer03(self.ctx)


class CheckAnswer03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CorrectFirstPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFouthPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece') == 1:
            return CheckAnswer04(self.ctx)


class CheckAnswer04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CorrectFirstPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFourthPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece') == 1:
            return CheckAnswer05(self.ctx)


class CheckAnswer05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CorrectFirstPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectSecondPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectThirdPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFourthPiece') == 2:
            return Retry01(self.ctx)
        if self.user_value(key='CorrectFourthPiece') == 1:
            return PuzzleSolved(self.ctx)


# 4개 중 하나라도 맞지 않으면 재시도
class Retry01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_event_ui_script(type=BannerType.Text, script='$02000376_BF__04_PUZZLEMAIN__0$', duration=3000, box_ids=['0'])
        self.set_user_value(key='CorrectFirstPiece', value=0)
        self.set_user_value(key='CorrectSecondPiece', value=0)
        self.set_user_value(key='CorrectThirdPiece', value=0)
        self.set_user_value(key='CorrectFouthPiece', value=0)
        self.set_user_value(trigger_id=5, key='ResetFirstPiece', value=1)
        self.set_user_value(trigger_id=6, key='ResetSecondPiece', value=1)
        self.set_user_value(trigger_id=7, key='ResetThirdPiece', value=1)
        self.set_user_value(trigger_id=8, key='ResetFourthPiece', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Retry02(self.ctx)


class Retry02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001023], state=1) # Lever
        self.set_mesh(trigger_ids=[3020], visible=True) # LionStone

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001023], state=0):
            return CheckAnswer01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10036010)


class PuzzleSolved(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True) # Pattern_LightOn
        self.set_mesh(trigger_ids=[3001,3002,3003,3004], visible=True) # BaseRock
        self.set_user_value(trigger_id=1, key='PuzzleSolved', value=1)
        self.set_user_value(trigger_id=5, key='LockFirstPiece', value=1)
        self.set_user_value(trigger_id=6, key='LockSecondPiece', value=1)
        self.set_user_value(trigger_id=7, key='LockThirdPiece', value=1)
        self.set_user_value(trigger_id=8, key='LockFourthPiece', value=1)
        # arg1="9001" arg2="trigger"
        self.set_achievement(achieve='OrientPattern_Puzzle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
