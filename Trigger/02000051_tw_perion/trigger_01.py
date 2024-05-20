""" trigger/02000051_tw_perion/trigger_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000382], state=1)
        self.set_mesh(trigger_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000382], state=0):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[101], visible=True)
        self.set_timer(timer_id='1', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
