""" trigger/03000112_bf/mesh.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], visible=True, interval=50, fade=3.0)
        self.set_interact_object(trigger_ids=[10000729], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000729], state=0):
            return 부서짐(self.ctx)


class 부서짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010], interval=50, fade=3.0)
        self.set_timer(timer_id='25', seconds=25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='25'):
            return 대기(self.ctx)


initial_state = 대기
