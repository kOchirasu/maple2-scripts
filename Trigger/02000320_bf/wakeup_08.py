""" trigger/02000320_bf/wakeup_08.xml """
import trigger_api


class 자는중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=8001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=8002, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=8003, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=8004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=8005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=8006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 도둑듬(self.ctx)


class 도둑듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000352], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000352], state=0):
            return 깨어남1(self.ctx)


class 깨어남1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=8)
        self.set_actor(trigger_id=8001, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=8002, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=8004, initial_sequence='Bore_A')
        self.set_actor(trigger_id=8005, initial_sequence='Stun_A')
        self.set_actor(trigger_id=8006, initial_sequence='Stun_A')
        self.spawn_monster(spawn_ids=[80004])
        self.set_dialogue(type=1, spawn_id=80004, script='$02000320_BF__WAKEUP_08__0$', time=2)
        self.spawn_monster(spawn_ids=[80005])
        self.set_dialogue(type=1, spawn_id=80005, script='$02000320_BF__WAKEUP_08__1$', time=2, arg5=1)
        self.spawn_monster(spawn_ids=[80006])
        self.set_dialogue(type=1, spawn_id=80006, script='$02000320_BF__WAKEUP_08__2$', time=2, arg5=2)
        self.spawn_monster(spawn_ids=[80001])
        self.spawn_monster(spawn_ids=[80002])
        self.spawn_monster(spawn_ids=[80003])
        self.set_dialogue(type=1, spawn_id=80003, script='$02000320_BF__WAKEUP_08__3$', time=2, arg5=3)
        self.set_dialogue(type=1, spawn_id=80001, script='$02000320_BF__WAKEUP_08__4$', time=2, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 깨어남2(self.ctx)


class 깨어남2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=4)
        self.set_dialogue(type=1, spawn_id=80002, script='$02000320_BF__WAKEUP_08__5$', time=2)
        self.set_dialogue(type=1, spawn_id=80001, script='$02000320_BF__WAKEUP_08__6$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=80003, script='$02000320_BF__WAKEUP_08__7$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 깨어남3(self.ctx)


class 깨어남3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=1)
        self.set_actor(trigger_id=8001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=8002, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 깨어남4(self.ctx)


class 깨어남4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[80004,80005,80006]):
            return 다시잠듬(self.ctx)
        if not self.monster_in_combat(spawn_ids=[80004,80005,80006]):
            return 다시자러감(self.ctx)


class 다시자러감(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=80004)
        self.remove_balloon_talk(spawn_id=80005)
        self.remove_balloon_talk(spawn_id=80006)
        self.remove_balloon_talk(spawn_id=80001)
        self.remove_balloon_talk(spawn_id=80002)
        self.remove_balloon_talk(spawn_id=80003)
        self.set_timer(timer_id='14', seconds=4)
        self.set_dialogue(type=1, spawn_id=80004, script='$02000320_BF__WAKEUP_08__8$', time=2)
        self.set_dialogue(type=1, spawn_id=80005, script='$02000320_BF__WAKEUP_08__9$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=80006, script='$02000320_BF__WAKEUP_08__10$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 다시잠듬(self.ctx)


class 다시잠듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[80001,80002,80003,80004,80005,80006])
        self.set_timer(timer_id='15', seconds=7)
        self.set_actor(trigger_id=8004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=8005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=8006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 도둑듬(self.ctx)


initial_state = 자는중
