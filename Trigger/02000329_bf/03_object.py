""" trigger/02000329_bf/03_object.xml """
import trigger_api


class 오브젝트_03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1103,1104]):
            return 오브젝트_03_작동(self.ctx)


class 오브젝트_03_작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[10001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return 오브젝트_03_작동_메세지(self.ctx)


class 오브젝트_03_작동_메세지(trigger_api.Trigger):
    pass


initial_state = 오브젝트_03
