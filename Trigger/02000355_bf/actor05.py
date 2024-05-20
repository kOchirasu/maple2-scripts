""" trigger/02000355_bf/actor05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[605])
        self.set_actor(trigger_id=205, visible=True, initial_sequence='Damg_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1501]):
            return 몬스터소환대기(self.ctx)


class 몬스터소환대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[605], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 더미해제(self.ctx)


class 더미해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=205, initial_sequence='Damg_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2005]):
            return 소멸(self.ctx)
        if self.monster_dead(spawn_ids=[2099]):
            return 소멸(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 리젠준비(self.ctx)
        if self.monster_dead(spawn_ids=[2099]):
            return 소멸(self.ctx)


class 리젠준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=205, visible=True, initial_sequence='Regen_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2005])


initial_state = 대기
