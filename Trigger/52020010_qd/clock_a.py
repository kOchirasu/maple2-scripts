""" trigger/52020010_qd/clock_a.xml """
import trigger_api


class Idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2002]):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001271], state=0):
            return Event_Start(self.ctx)


class Event_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002], visible=True)
        self.spawn_monster(spawn_ids=[101]) # 아빠 유령
        self.spawn_monster(spawn_ids=[102]) # 애기 유령
        self.spawn_monster(spawn_ids=[103]) # 엄마 유령

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=102, msg='엄마! 나 이 빵 먹어도 돼요?', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_02(self.ctx)


class Event_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=103, msg='안돼! 금방 밥먹을거야.', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_03(self.ctx)


class Event_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=102, msg='힝... 아빠 나 이거 먹으면 안돼요?', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='허허... 녀석 참. 그럼 한개만 먹는거다?', duration=2500)
        self.add_balloon_talk(spawn_id=103, msg='여보!', duration=2500, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=103, msg='그보다 요즘 한다는 일은 잘 되가요?', duration=2500, delay_tick=1500)
        self.add_balloon_talk(spawn_id=102, msg='와! 신난다!', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_06(self.ctx)


class Event_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='당연하지! 왕국 제일의 기술자인 내가 못할 일은 없어!', duration=2800, delay_tick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_07(self.ctx)


class Event_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='그런데 말이야. 일이 끝나갈 수록 기분이 영 찝찝해.', duration=2800, delay_tick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Event_08(self.ctx)


class Event_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='도대체 왕은 무슨 생각을 하고 있는건지...', duration=3000, delay_tick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Event_End(self.ctx)


class Event_End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5002])
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])


initial_state = Idle
