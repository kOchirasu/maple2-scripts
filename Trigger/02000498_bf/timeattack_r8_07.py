""" trigger/02000498_bf/timeattack_r8_07.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=140, spawn_ids=[108099]):
            return 몹스폰(self.ctx)


class 몹스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dark_stream_spawn_monster(spawn_ids=[108007], score=8000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[108099]):
            self.destroy_monster(spawn_ids=[108007])
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[108007]):
            return 몹스폰(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
