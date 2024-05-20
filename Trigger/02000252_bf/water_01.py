""" trigger/02000252_bf/water_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108], interval=100)
        self.set_interact_object(trigger_ids=[10000409], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000409], state=0):
            return 물(self.ctx)


class 물(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108], visible=True, interval=250)


initial_state = 대기
