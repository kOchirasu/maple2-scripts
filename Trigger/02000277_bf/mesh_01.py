""" trigger/02000277_bf/mesh_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000633], state=1)
        self.set_mesh(trigger_ids=[10000], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000633], state=0):
            return 열기(self.ctx)


class 열기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10000])
        self.set_timer(timer_id='1', seconds=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
