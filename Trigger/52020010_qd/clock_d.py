""" trigger/52020010_qd/clock_d.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5011])
        self.set_effect(trigger_ids=[5012])
        self.set_effect(trigger_ids=[5013])
        self.set_effect(trigger_ids=[5014])
        self.set_effect(trigger_ids=[5015])
        self.set_interact_object(trigger_ids=[10001275], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2005], quest_ids=[60200050], quest_states=[1]):
            return Ready(self.ctx)
        if self.quest_user_detected(box_ids=[2005], quest_ids=[60200050], quest_states=[2]):
            return Ready_A(self.ctx)
        if self.quest_user_detected(box_ids=[2005], quest_ids=[60200050], quest_states=[3]):
            return Ready_A(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001275], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001274], state=0):
            return Event_Start(self.ctx)


class Event_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5011], visible=True)
        self.set_effect(trigger_ids=[5012], visible=True)
        self.spawn_monster(spawn_ids=[401]) # 아빠 유령

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=401, msg='대체 어디 있는거야?', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5013], visible=True)
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_3002')
        self.add_balloon_talk(spawn_id=401, msg='분명히 책장 어딘가에 장치가 있었는데...', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=401, msg='어째서 이럴 때 기억나지 않는거야!!!', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5014], visible=True)
        self.add_balloon_talk(spawn_id=401, msg='여기였나?', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=401, msg='아니... 생각해보니 소용 없군...', duration=2800)
        self.set_interact_object(trigger_ids=[10001275], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_06(self.ctx)


class Event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5015], visible=True)
        self.add_balloon_talk(spawn_id=401, msg='어차피 거스를 수 없는 운명인 것을...', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Event_End(self.ctx)


class Event_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5011])
        self.set_effect(trigger_ids=[5012])
        self.set_effect(trigger_ids=[5013])
        self.set_effect(trigger_ids=[5014])
        self.set_effect(trigger_ids=[5015])
        self.destroy_monster(spawn_ids=[401])


# 시간을 돌려라 퀘스트 가능 상태 이후
class Ready_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10001275], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001274], state=0):
            return Event_Start_A(self.ctx)


class Event_Start_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5011], visible=True)
        self.set_effect(trigger_ids=[5012], visible=True)
        self.spawn_monster(spawn_ids=[401]) # 아빠 유령

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Event_01_A(self.ctx)


class Event_01_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=401, msg='대체 어디 있는거야?', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_02_A(self.ctx)


class Event_02_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5013], visible=True)
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_3002')
        self.add_balloon_talk(spawn_id=401, msg='분명히 책장 어딘가에 장치가 있었는데...', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_03_A(self.ctx)


class Event_03_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=401, msg='어째서 이럴 때 기억나지 않는거야!!!', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_04_A(self.ctx)


class Event_04_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5014], visible=True)
        self.add_balloon_talk(spawn_id=401, msg='여기였나?', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_05_A(self.ctx)


class Event_05_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=401, msg='아니... 생각해보니 소용 없군...', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_06_A(self.ctx)


class Event_06_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5015], visible=True)
        self.add_balloon_talk(spawn_id=401, msg='어차피 거스를 수 없는 운명인 것을...', duration=2800)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Event_End_A(self.ctx)


class Event_End_A(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5011])
        self.set_effect(trigger_ids=[5012])
        self.set_effect(trigger_ids=[5013])
        self.set_effect(trigger_ids=[5014])
        self.set_effect(trigger_ids=[5015])
        self.destroy_monster(spawn_ids=[401])


initial_state = Idle
