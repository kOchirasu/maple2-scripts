""" trigger/02000355_bf/actor11.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[611])
        self.set_actor(trigger_id=211, visible=True, initial_sequence='Damg_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[11001]):
            return 몬스터소환대기(self.ctx)


class 몬스터소환대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[611], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2011], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 더미해제(self.ctx)


class 더미해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=211, initial_sequence='Damg_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2011]):
            return 소멸(self.ctx)
        if self.monster_dead(spawn_ids=[2099]):
            return 소멸(self.ctx)
        if self.npc_detected(box_id=105, spawn_ids=[2011]):
            self.destroy_monster(spawn_ids=[2011])
            return 리젠준비(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=30000):
            return 리젠준비(self.ctx)
        if self.monster_dead(spawn_ids=[2099]):
            return 소멸(self.ctx)


class 리젠준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=211, visible=True, initial_sequence='Regen_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대기(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[2011])


initial_state = 대기
