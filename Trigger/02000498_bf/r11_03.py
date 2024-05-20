""" trigger/02000498_bf/r11_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=103, spawn_ids=[111001]):
            return 몹스폰(self.ctx)


class 몹스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111001]):
            self.destroy_monster(spawn_ids=[111004])
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[111004]):
            return 몹스폰(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
