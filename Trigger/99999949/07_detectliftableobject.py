""" trigger/99999949/07_detectliftableobject.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5007]) # 내려놓을 위치 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9061]):
            return Guide(self.ctx)


class Guide(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='7번 영역에 들어가면 DetectLiftableObject 트리거가 발동됩니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9060]):
            return Ready01(self.ctx)


class Ready01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='DetectLiftableObject 2초 후에 시작됩니다.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return Ready02(self.ctx)


class Ready02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__0$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return QuizRandom01(self.ctx)


class QuizRandom01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5007], visible=True) # 내려놓을 위치 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=50.0):
            return AnswerIsWood01(self.ctx) # Wooditem : 30000377
        if self.random_condition(weight=50.0):
            return AnswerIsRock01(self.ctx) # Rockitem : 30000440


class AnswerIsWood01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__1$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9062], item_id=0):
            # 아이템을 내려놓았는지 체크
            return CheckAnswerWood01(self.ctx)


class CheckAnswerWood01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5007]) # 내려놓을 위치 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9062], item_id=30000377):
            # 내려놓은 아이템이 나무 상자이면 정답
            return RightAnswerWood01(self.ctx)
        if not self.detect_liftable_object(box_ids=[9062], item_id=30000377):
            # 내려놓은 아이템이 나무 상자가 아니면 실패
            return WrongAnswerWood01(self.ctx)


class RightAnswerWood01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__2$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return ClearDetectBox01(self.ctx)


class WrongAnswerWood01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__3$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return ClearDetectBox01(self.ctx)


class AnswerIsRock01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__4$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9062], item_id=0):
            # 아이템을 내려놓았는지 체크
            return CheckAnswerRock01(self.ctx)


class CheckAnswerRock01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5007]) # 내려놓을 위치 가이드

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(box_ids=[9062], item_id=30000440):
            # 내려놓은 아이템이 바위덩이이면 정답
            return RightAnswerRock01(self.ctx)
        if not self.detect_liftable_object(box_ids=[9062], item_id=30000440):
            # 내려놓은 아이템이 바위덩이가 아니면 실패
            return WrongAnswerRock01(self.ctx)


class RightAnswerRock01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__5$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return ClearDetectBox01(self.ctx)


class WrongAnswerRock01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999949__07_DETECTLIFTABLEOBJECT__6$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return ClearDetectBox01(self.ctx)


class ClearDetectBox01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.detect_liftable_object(box_ids=[9062], item_id=0):
            # 체크박스에 아무 오브젝트가 없는지 체크
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.debug_string(value='3초 후에 트리거가 리셋됩니다. 7번 영역 밖으로 나가세요.')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Wait(self.ctx)


initial_state = Wait
