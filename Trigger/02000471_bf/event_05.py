""" trigger/02000471_bf/event_05.xml """
import trigger_api


class none(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706]):
            return idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[121,154,122,156,110]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=706, type='trigger', achieve='Hauntedmansion')
        self.spawn_monster(spawn_ids=[1110,1111,1112,1113], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1110, script='$02000471_BF__EVENT_05__0$', time=3, arg5=4)
        self.set_dialogue(type=1, spawn_id=1111, script='$02000471_BF__EVENT_05__1$', time=3, arg5=5)
        self.set_dialogue(type=1, spawn_id=1112, script='$02000471_BF__EVENT_05__2$', time=3, arg5=1)
        self.set_dialogue(type=1, spawn_id=1113, script='$02000471_BF__EVENT_05__3$', time=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return exit(self.ctx)


class exit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1110,1111,1112,1113])


initial_state = none
