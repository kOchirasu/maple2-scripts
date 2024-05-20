""" trigger/80000014_bonus/lever.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001314], state=1)
        self.set_mesh(trigger_ids=[3501,3502,3503,3504,3505,3506], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 안내(self.ctx)
        if self.object_interacted(interact_ids=[10001314], state=0):
            return 문열림(self.ctx)


class 안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$80000014_bonus__lever__0$', arg3='2000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001314], state=0):
            return 문열림(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 반응대기(self.ctx)


class 문열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3501,3502,3503,3504,3505,3506])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
