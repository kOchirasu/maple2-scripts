""" trigger/02020100_bf/seed1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='Seed1interact', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed1start') == 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1302], visible=True, fade=2.0)
        self.set_interact_object(trigger_ids=[10002109], state=1, arg3=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed1start') == 2:
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[10002109], state=0):
            return 씨앗1_대기(self.ctx)


class 씨앗1_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1302])
        self.set_interact_object(trigger_ids=[10002109], state=0, arg3=True)
        self.set_user_value(trigger_id=99990001, key='Seed1interact', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Seed1start') == 2:
            return 종료(self.ctx)
        if not self.check_any_user_additional_effect(box_id=0, additional_effect_id=70002109, level=1):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10002109], state=0)


initial_state = 대기
