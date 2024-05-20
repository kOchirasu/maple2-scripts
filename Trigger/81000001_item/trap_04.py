""" trigger/81000001_item/trap_04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000129], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000129], state=0):
            self.set_mesh(trigger_ids=[701,702,703])
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='129', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='129'):
            self.set_mesh(trigger_ids=[701,702,703], visible=True)
            return 시작(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='129')


initial_state = 시작
