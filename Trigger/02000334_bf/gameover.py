""" trigger/02000334_bf/gameover.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200,999]) # 성벽

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[200]):
            return 게임오버(self.ctx)


class 게임오버(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[999]) # 게임오버용몬스터 소멸


initial_state = 시작
