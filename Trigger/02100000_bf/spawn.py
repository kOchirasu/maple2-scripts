""" trigger/02100000_bf/spawn.xml """
import trigger_api


class 소환(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterSpawn') == 1:
            return 끝_1(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[81003])
        self.spawn_monster(spawn_ids=[810031])
        self.spawn_monster(spawn_ids=[810032])


class 끝_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[82001]):
            return None # Missing State: 성공

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[-1])


initial_state = 소환
