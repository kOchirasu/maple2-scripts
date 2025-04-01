""" trigger/52020016_qd/monster_spawn_4_1.xml """
import trigger_api


class 체력조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn_phase_4') == 1:
            return 전투페이즈(self.ctx)


class 전투페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[4000402], auto_target=False)
        self.set_dialogue(type=1, spawn_id=4000402, script='저를 살려내란 말이에요!!', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=4000402, is_relative=True) <= 20:
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[4000402], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            pass


initial_state = 체력조건
