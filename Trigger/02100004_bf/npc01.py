""" trigger/02100004_bf/npc01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 소환대기(self.ctx)


class 소환대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999992, key='NpcSpawned01', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawn01') == 1:
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=999992, key='NpcSpawned01', value=1)
        self.spawn_monster(spawn_ids=[2001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
