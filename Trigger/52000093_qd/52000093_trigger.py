""" trigger/52000093_qd/52000093_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3003,3004])
        self.destroy_monster(spawn_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9100], quest_ids=[50100490], quest_states=[1]):
            return 진행중일때20002274(self.ctx)
        if self.quest_user_detected(box_ids=[9100], quest_ids=[20002274], quest_states=[1]):
            return 진행중일때20002274(self.ctx)


class 진행중일때20002274(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 몬스터들이 소환된다
        self.spawn_monster(spawn_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008], auto_target=False) # ,90537,90539

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1000,1001,1002,1003,1004,1005,1006,1007,1008]):
            return 진행중일때20002274(self.ctx)


initial_state = 대기
