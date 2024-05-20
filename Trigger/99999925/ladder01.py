""" trigger/99999925/ladder01.xml """
import trigger_api


class ladderIdle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001077], state=0):
            return ladderWolk(self.ctx)


class ladderWolk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[701], start_delay=1)
        self.set_ai_extra_data(key='LadderCnt', value=1, is_modify=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ladderEnd(self.ctx)


class ladderEnd(trigger_api.Trigger):
    pass


initial_state = ladderIdle
