""" trigger/52000067_qd/sub_event_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7200]) # 폭발

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=704) >= 1:
            return idle_02(self.ctx)


class idle_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[756,755]) # 시민
        self.set_dialogue(type=1, spawn_id=102, script='$52000067_QD__SUB_EVENT_02__0$', time=3)
        self.set_dialogue(type=1, spawn_id=101, script='$52000067_QD__SUB_EVENT_02__1$', time=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    pass


initial_state = idle
