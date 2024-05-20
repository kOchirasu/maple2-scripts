""" trigger/02000350_bf/timeattack_r4_08.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=140, spawn_ids=[104099]):
            return 몹스폰(self.ctx)


class 몹스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[104008], score=4100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[104099]):
            self.destroy_monster(spawn_ids=[104008])
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[104008]):
            return 몹스폰(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
