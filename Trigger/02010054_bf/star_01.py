""" trigger/02010054_bf/star_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000856], state=0):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305], visible=True, interval=500, fade=3.0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.set_mesh(trigger_ids=[3301,3302,3303,3304,3305], interval=900, fade=2.0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
