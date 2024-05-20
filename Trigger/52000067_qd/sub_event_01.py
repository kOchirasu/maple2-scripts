""" trigger/52000067_qd/sub_event_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[751]) # 골두스

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=751, script='$52000067_QD__SUB_EVENT_01__0$', time=3)
        self.set_dialogue(type=1, spawn_id=751, script='$52000067_QD__SUB_EVENT_01__1$', time=3, arg5=3)
        self.set_dialogue(type=1, spawn_id=751, script='$52000067_QD__SUB_EVENT_01__2$', time=3, arg5=6)
        self.set_dialogue(type=1, spawn_id=751, script='$52000067_QD__SUB_EVENT_01__3$', time=3, arg5=9)
        self.set_dialogue(type=1, spawn_id=751, script='$52000067_QD__SUB_EVENT_01__4$', time=3, arg5=12)
        self.set_dialogue(type=1, spawn_id=751, script='$52000067_QD__SUB_EVENT_01__5$', time=3, arg5=15)
        self.set_dialogue(type=1, spawn_id=751, script='$52000067_QD__SUB_EVENT_01__6$', time=3, arg5=18)
        self.set_dialogue(type=1, spawn_id=752, script='$52000067_QD__SUB_EVENT_01__7$', time=3, arg5=19)
        self.set_dialogue(type=1, spawn_id=753, script='$52000067_QD__SUB_EVENT_01__8$', time=3, arg5=19)
        self.set_dialogue(type=1, spawn_id=754, script='$52000067_QD__SUB_EVENT_01__9$', time=3, arg5=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[757,758,761,762]) # 시민
        self.set_dialogue(type=1, spawn_id=757, script='$52000067_QD__SUB_EVENT_01__10$', time=3, arg5=2)
        self.set_dialogue(type=1, spawn_id=758, script='$52000067_QD__SUB_EVENT_01__11$', time=3, arg5=3)
        self.set_dialogue(type=1, spawn_id=762, script='$52000067_QD__SUB_EVENT_01__12$', time=3, arg5=2)
        self.set_dialogue(type=1, spawn_id=761, script='$52000067_QD__SUB_EVENT_01__13$', time=3, arg5=2)


initial_state = idle
