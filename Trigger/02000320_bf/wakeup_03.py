""" trigger/02000320_bf/wakeup_03.xml """
import trigger_api


class 자는중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=3002, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=3003, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=3004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=3005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=3006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 도둑듬(self.ctx)


class 도둑듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000317], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000317], state=0):
            return 깨어남1(self.ctx)


class 깨어남1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=8)
        self.set_actor(trigger_id=3001, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=3002, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=3004, initial_sequence='Bore_A')
        self.set_actor(trigger_id=3005, initial_sequence='Stun_A')
        self.set_actor(trigger_id=3006, initial_sequence='Stun_A')
        self.spawn_monster(spawn_ids=[30004])
        self.set_dialogue(type=1, spawn_id=30004, script='$02000320_BF__WAKEUP_03__0$', time=2)
        self.spawn_monster(spawn_ids=[30005])
        self.set_dialogue(type=1, spawn_id=30005, script='$02000320_BF__WAKEUP_03__1$', time=2, arg5=1)
        self.spawn_monster(spawn_ids=[30006])
        self.set_dialogue(type=1, spawn_id=30006, script='$02000320_BF__WAKEUP_03__2$', time=2, arg5=2)
        self.spawn_monster(spawn_ids=[30001])
        self.spawn_monster(spawn_ids=[30002])
        self.spawn_monster(spawn_ids=[30003])
        self.set_dialogue(type=1, spawn_id=30003, script='$02000320_BF__WAKEUP_03__3$', time=2, arg5=3)
        self.set_dialogue(type=1, spawn_id=30001, script='$02000320_BF__WAKEUP_03__4$', time=2, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 깨어남2(self.ctx)


class 깨어남2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=4)
        self.set_dialogue(type=1, spawn_id=30002, script='$02000320_BF__WAKEUP_03__5$', time=2)
        self.set_dialogue(type=1, spawn_id=30001, script='$02000320_BF__WAKEUP_03__6$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=30003, script='$02000320_BF__WAKEUP_03__7$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 깨어남3(self.ctx)


class 깨어남3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=1)
        self.set_actor(trigger_id=3001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=3002, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 깨어남4(self.ctx)


class 깨어남4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[30004,30005,30006]):
            return 다시잠듬(self.ctx)
        if not self.monster_in_combat(spawn_ids=[30004,30005,30006]):
            return 다시자러감(self.ctx)


class 다시자러감(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=30004)
        self.remove_balloon_talk(spawn_id=30005)
        self.remove_balloon_talk(spawn_id=30006)
        self.remove_balloon_talk(spawn_id=30001)
        self.remove_balloon_talk(spawn_id=30002)
        self.remove_balloon_talk(spawn_id=30003)
        self.set_timer(timer_id='14', seconds=4)
        self.set_dialogue(type=1, spawn_id=30004, script='$02000320_BF__WAKEUP_03__8$', time=2)
        self.set_dialogue(type=1, spawn_id=30005, script='$02000320_BF__WAKEUP_03__9$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=30006, script='$02000320_BF__WAKEUP_03__10$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 다시잠듬(self.ctx)


class 다시잠듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[30001,30002,30003,30004,30005,30006])
        self.set_timer(timer_id='15', seconds=7)
        self.set_actor(trigger_id=3004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=3005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=3006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 도둑듬(self.ctx)


initial_state = 자는중
