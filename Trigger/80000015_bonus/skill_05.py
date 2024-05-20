""" trigger/80000015_bonus/skill_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[705])
        self.set_skill(trigger_ids=[727])
        self.set_visible_breakable_object(trigger_ids=[7501,7502,7503,7504])
        self.set_breakable(trigger_ids=[7501,7502,7503,7504])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[7501,7502,7503,7504], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[7501,7502,7503,7504], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 스킬발동(self.ctx)


class 스킬발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[7501,7502,7503,7504])
        self.set_skill(trigger_ids=[705], enable=True)
        self.set_skill(trigger_ids=[727], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
