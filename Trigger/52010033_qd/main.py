""" trigger/52010033_qd/main.xml """
import trigger_api


# 페리온 병원 : 52010033
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[10003075,10003076,10003077,10003078,10003079], quest_states=[1]):
            return NpcSpawn(self.ctx)


class NpcSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105]) # 상처입은 추격대원
        self.spawn_monster(spawn_ids=[106]) # 상처입은 추격대원
        self.spawn_monster(spawn_ids=[107]) # 상처입은 추격대원
        self.spawn_monster(spawn_ids=[108]) # 상처입은 추격대원


initial_state = idle
