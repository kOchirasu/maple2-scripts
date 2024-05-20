""" trigger/52000025_qd/talk_event.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702]):
            return talk_01(self.ctx)


class talk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='$52000025_QD__TALK_EVENT__0$', time=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return talk_02(self.ctx)


class talk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=201, script='$52000025_QD__TALK_EVENT__1$', time=2, arg5=1)


initial_state = idle
