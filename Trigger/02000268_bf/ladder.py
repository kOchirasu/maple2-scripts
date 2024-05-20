""" trigger/02000268_bf/ladder.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301,302,303,304,305])
        self.set_interact_object(trigger_ids=[10000456], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000456], state=0):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[301,302,303,304,305], visible=True, interval=500)
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            self.set_mesh(trigger_ids=[305,304,303,302,301], interval=500)
            return 재사용대기(self.ctx)


class 재사용대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='170', seconds=170)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='170'):
            return 대기(self.ctx)


initial_state = 대기
