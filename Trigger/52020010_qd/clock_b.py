""" trigger/52020010_qd/clock_b.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2003]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001272], state=0):
            return Event_Start(self.ctx)


class Event_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003], visible=True)
        self.spawn_monster(spawn_ids=[201]) # 아빠 유령
        self.spawn_monster(spawn_ids=[202]) # 엄마 유령
        self.spawn_monster(spawn_ids=[203]) # 애기 유령

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5004], visible=True)
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_3001')
        self.add_balloon_talk(spawn_id=203, msg='와! 쾅쾅한다!', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=202, msg='여보... 우리 어쩌면 좋아요?', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=201, msg='일이 이렇게 되어버릴 줄은...', duration=2800)
        self.add_balloon_talk(spawn_id=202, msg='우리 도망 못가는거죠?', duration=2800, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5005], visible=True)
        self.add_balloon_talk(spawn_id=203, msg='쾅쾅! 쾅쾅!', duration=2000)
        self.add_balloon_talk(spawn_id=201, msg='난 대체 무얼 위해...', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=202, msg='여보!', duration=2800)
        self.add_balloon_talk(spawn_id=201, msg='!!!', duration=2000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_06(self.ctx)


class Event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=201, msg='여보, 내 딸... 모두 미안하오...', duration=2000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_07(self.ctx)


class Event_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5006], visible=True)
        self.add_balloon_talk(spawn_id=202, msg='여보...', duration=2000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Event_End(self.ctx)


class Event_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])
        self.destroy_monster(spawn_ids=[201])
        self.destroy_monster(spawn_ids=[202])
        self.destroy_monster(spawn_ids=[203])


initial_state = Idle
