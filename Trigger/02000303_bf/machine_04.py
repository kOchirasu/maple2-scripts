""" trigger/02000303_bf/machine_04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000578], state=0):
            self.set_mesh(trigger_ids=[3004], visible=True, fade=2.0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1800000', seconds=1800000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1800000'):
            return None # Missing State: 종료2


initial_state = 시작
