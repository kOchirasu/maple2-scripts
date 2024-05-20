""" trigger/80000014_bonus/skill_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[701])
        self.set_visible_breakable_object(trigger_ids=[7101,7102,7103])
        self.set_breakable(trigger_ids=[7101,7102,7103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[7101,7102,7103], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[7101,7102,7103], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 스킬발동(self.ctx)


class 스킬발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[701], enable=True)
        self.set_breakable(trigger_ids=[7101,7102,7103])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
