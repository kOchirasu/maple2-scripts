""" trigger/80000006_bonus/meso.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            self.create_item(spawn_ids=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
            self.create_item(spawn_ids=[9001,9002,9003,9004,9005])
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    pass


initial_state = 입장
