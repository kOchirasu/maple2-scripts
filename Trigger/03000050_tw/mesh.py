""" trigger/03000050_tw/mesh.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], visible=True, interval=200, fade=2.0)
        self.set_interact_object(trigger_ids=[10000730], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000730], state=0):
            return 부서짐(self.ctx)


class 부서짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000], interval=200, fade=2.0)
        self.set_timer(timer_id='25', seconds=25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='25'):
            return 대기(self.ctx)


initial_state = 대기
