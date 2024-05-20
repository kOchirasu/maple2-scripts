""" trigger/52020010_qd/clock_c.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5007])
        self.set_effect(trigger_ids=[5008])
        self.set_effect(trigger_ids=[5009])
        self.set_effect(trigger_ids=[5010])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2004]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001273], state=0):
            return Event_Start(self.ctx)


class Event_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5007], visible=True)
        self.spawn_monster(spawn_ids=[301]) # 엄마 유령
        self.spawn_monster(spawn_ids=[302]) # 애기 유령

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5008], visible=True)
        self.set_npc_emotion_loop(spawn_id=302, sequence_name='Bore_B', duration=18000.0)
        self.add_balloon_talk(spawn_id=302, msg='엄마 무서워...', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=301, msg='울지마렴... 조금 있으면 괜찮아 질거야...', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5009], visible=True)
        self.add_balloon_talk(spawn_id=301, msg='여보? 어디 간 거에요!', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5010], visible=True)
        self.add_balloon_talk(spawn_id=301, msg='여보!!!', duration=2800, delay_tick=1000)
        self.add_balloon_talk(spawn_id=302, msg='엄마... 아빠... 무서워...', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Event_End(self.ctx)


class Event_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5007])
        self.set_effect(trigger_ids=[5008])
        self.set_effect(trigger_ids=[5009])
        self.set_effect(trigger_ids=[5010])
        self.destroy_monster(spawn_ids=[301])
        self.destroy_monster(spawn_ids=[302])


initial_state = Idle
