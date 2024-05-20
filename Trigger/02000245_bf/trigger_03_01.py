""" trigger/02000245_bf/trigger_03_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000301], state=1)
        self.set_mesh(trigger_ids=[705,706], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000301], state=0):
            return 개봉(self.ctx)


class 개봉(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[705,706])
        self.set_timer(timer_id='1', seconds=180)


initial_state = 대기
