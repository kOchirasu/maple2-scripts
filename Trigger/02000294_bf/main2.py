""" trigger/02000294_bf/main2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[10001])
        self.destroy_monster(spawn_ids=[10002])
        self.destroy_monster(spawn_ids=[10003])
        self.destroy_monster(spawn_ids=[10004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_01') == 1:
            return 트리거01진행(self.ctx)


class 트리거01진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[10001], auto_target=False)
        self.spawn_monster(spawn_ids=[10002], auto_target=False)
        self.spawn_monster(spawn_ids=[10003], auto_target=False)
        self.spawn_monster(spawn_ids=[10004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 트리거02시작(self.ctx)


class 트리거02시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=10001, patrol_name='MS2PatrolData0')
        self.move_npc(spawn_id=10002, patrol_name='MS2PatrolData1')
        self.move_npc(spawn_id=10003, patrol_name='MS2PatrolData2')
        self.move_npc(spawn_id=10004, patrol_name='MS2PatrolData3')


initial_state = 대기
