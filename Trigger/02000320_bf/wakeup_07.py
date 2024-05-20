""" trigger/02000320_bf/wakeup_07.xml """
import trigger_api


class 자는중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=7001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=7002, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=7003, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=7004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=7005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=7006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 도둑듬(self.ctx)


class 도둑듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000351], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000351], state=0):
            return 깨어남1(self.ctx)


class 깨어남1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=8)
        self.set_actor(trigger_id=7001, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=7002, visible=True, initial_sequence='Bore_A')
        self.set_actor(trigger_id=7004, initial_sequence='Bore_A')
        self.set_actor(trigger_id=7005, initial_sequence='Stun_A')
        self.set_actor(trigger_id=7006, initial_sequence='Stun_A')
        self.spawn_monster(spawn_ids=[70004])
        self.set_dialogue(type=1, spawn_id=70004, script='$02000320_BF__WAKEUP_07__0$', time=2)
        self.spawn_monster(spawn_ids=[70005])
        self.set_dialogue(type=1, spawn_id=70005, script='$02000320_BF__WAKEUP_07__1$', time=2, arg5=1)
        self.spawn_monster(spawn_ids=[70006])
        self.set_dialogue(type=1, spawn_id=70006, script='$02000320_BF__WAKEUP_07__2$', time=2, arg5=2)
        self.spawn_monster(spawn_ids=[70001])
        self.spawn_monster(spawn_ids=[70002])
        self.spawn_monster(spawn_ids=[70003])
        self.set_dialogue(type=1, spawn_id=70003, script='$02000320_BF__WAKEUP_07__3$', time=2, arg5=3)
        self.set_dialogue(type=1, spawn_id=70001, script='$02000320_BF__WAKEUP_07__4$', time=2, arg5=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 깨어남2(self.ctx)


class 깨어남2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=4)
        self.set_dialogue(type=1, spawn_id=70002, script='$02000320_BF__WAKEUP_07__5$', time=2)
        self.set_dialogue(type=1, spawn_id=70001, script='$02000320_BF__WAKEUP_07__6$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=70003, script='$02000320_BF__WAKEUP_07__7$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 깨어남3(self.ctx)


class 깨어남3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=1)
        self.set_actor(trigger_id=7001, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=7002, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 깨어남4(self.ctx)


class 깨어남4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[70004,70005,70006]):
            return 다시잠듬(self.ctx)
        if not self.monster_in_combat(spawn_ids=[70004,70005,70006]):
            return 다시자러감(self.ctx)


class 다시자러감(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk(spawn_id=70004)
        self.remove_balloon_talk(spawn_id=70005)
        self.remove_balloon_talk(spawn_id=70006)
        self.remove_balloon_talk(spawn_id=70001)
        self.remove_balloon_talk(spawn_id=70002)
        self.remove_balloon_talk(spawn_id=70003)
        self.set_timer(timer_id='14', seconds=4)
        self.set_dialogue(type=1, spawn_id=70004, script='$02000320_BF__WAKEUP_07__8$', time=2)
        self.set_dialogue(type=1, spawn_id=70005, script='$02000320_BF__WAKEUP_07__9$', time=2, arg5=1)
        self.set_dialogue(type=1, spawn_id=70006, script='$02000320_BF__WAKEUP_07__10$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 다시잠듬(self.ctx)


class 다시잠듬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[70001,70002,70003,70004,70005,70006])
        self.set_timer(timer_id='15', seconds=7)
        self.set_actor(trigger_id=7004, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=7005, visible=True, initial_sequence='Stun_A')
        self.set_actor(trigger_id=7006, visible=True, initial_sequence='Stun_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 도둑듬(self.ctx)


initial_state = 자는중
