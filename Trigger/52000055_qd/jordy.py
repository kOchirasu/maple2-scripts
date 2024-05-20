""" trigger/52000055_qd/jordy.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100120,60100121,60100122,60100123,60100124,60100125,60100126,60100127,60100128,60100129,60100130], quest_states=[1]):
            return jordy(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[60100235,60100236,60100237,60100238,60100239,60100240], quest_states=[2]):
            return jordy(self.ctx)


# 조디 스폰
class jordy(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[103], auto_target=False) # 조디


initial_state = Ready
