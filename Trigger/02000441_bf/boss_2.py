""" trigger/02000441_bf/boss_2.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='monster_respawn') == 1:
            return 몬스터체력_75(self.ctx)


class 몬스터체력_75(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=209, is_relative=True) <= 75:
            return 몬스터체력_35(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[210,211,212,213])


class 몬스터체력_35(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=209, is_relative=True) <= 35:
            return 몬스터_마지막_리스폰(self.ctx)


class 몬스터_마지막_리스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[214,215,216,217])

    def on_tick(self) -> trigger_api.Trigger:
        pass


initial_state = idle
