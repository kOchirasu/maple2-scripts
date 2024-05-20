""" trigger/02000320_bf/wakeup_01.xml """
import trigger_api


class 자는중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=1001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=1002, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=1003, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=1004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=1005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=1006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 도둑듬(self.ctx)


class 도둑듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000281], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000281], state=0):
            return 깨어남1(self.ctx)


class 깨어남1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=8)
        self.set_actor(trigger_id=1001, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=1002, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=1004, initial_sequence='Bore_A')
        self.set_actor(trigger_id=1005, initial_sequence='Stun_A')
        self.set_actor(trigger_id=1006, initial_sequence='Stun_A')
        self.spawn_monster(spawn_ids=[10004])
        self.set_dialogue(type=1, spawn_id=10004, script='$02000320_BF__WAKEUP_01__0$', time=2)
        self.spawn_monster(spawn_ids=[10005])
        self.set_dialogue(type=1, spawn_id=10005, script='$02000320_BF__WAKEUP_01__1$', time=2, arg5=1)
        self.spawn_monster(spawn_ids=[10006])
        self.set_dialogue(type=1, spawn_id=10006, script='$02000320_BF__WAKEUP_01__2$', time=2, arg5=2)
        self.spawn_monster(spawn_ids=[10001])
        self.spawn_monster(spawn_ids=[10002])
        self.spawn_monster(spawn_ids=[10003])
        self.set_dialogue(type=1, spawn_id=10003, script='$02000320_BF__WAKEUP_01__3$', time=2, arg5=3)
        self.set_dialogue(type=1, spawn_id=10001, script='$02000320_BF__WAKEUP_01__4$', time=2, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 깨어남2(self.ctx)


class 깨어남2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=4)
        self.set_dialogue(type=1, spawn_id=10002, script='$02000320_BF__WAKEUP_01__5$', time=2)
        self.set_dialogue(type=1, spawn_id=10001, script='$02000320_BF__WAKEUP_01__6$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=10003, script='$02000320_BF__WAKEUP_01__7$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 깨어남3(self.ctx)


class 깨어남3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=1)
        self.set_actor(trigger_id=1001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=1002, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 깨어남4(self.ctx)


class 깨어남4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[10004,10005,10006]):
            return 다시잠듬(self.ctx)
        if not self.monster_in_combat(spawn_ids=[10004,10005,10006]):
            return 다시자러감(self.ctx)


class 다시자러감(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=10004)
        self.remove_balloon_talk(spawn_id=10005)
        self.remove_balloon_talk(spawn_id=10006)
        self.remove_balloon_talk(spawn_id=10001)
        self.remove_balloon_talk(spawn_id=10002)
        self.remove_balloon_talk(spawn_id=10003)
        self.set_timer(timer_id='14', seconds=4)
        self.set_dialogue(type=1, spawn_id=10004, script='$02000320_BF__WAKEUP_01__8$', time=2)
        self.set_dialogue(type=1, spawn_id=10005, script='$02000320_BF__WAKEUP_01__9$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=10006, script='$02000320_BF__WAKEUP_01__10$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 다시잠듬(self.ctx)


class 다시잠듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[10001,10002,10003,10004,10005,10006])
        self.set_timer(timer_id='15', seconds=7)
        self.set_actor(trigger_id=1004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=1005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=1006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 도둑듬(self.ctx)


initial_state = 자는중
