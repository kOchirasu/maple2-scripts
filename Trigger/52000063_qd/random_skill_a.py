""" trigger/52000063_qd/random_skill_a.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='gameStart') == 1:
            return 감지대기(self.ctx)


class 감지대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[603], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[111]):
            return 스킬랜덤(self.ctx)


class 스킬랜덤(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=80.0):
            self.add_buff(box_ids=[199], skill_id=70000008, level=1, ignore_player=False, is_skill_set=False)
            return 종료(self.ctx)
        if self.random_condition(weight=20.0):
            self.add_buff(box_ids=[199], skill_id=70000009, level=1, ignore_player=False, is_skill_set=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
