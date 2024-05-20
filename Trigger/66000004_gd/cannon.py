""" trigger/66000004_gd/cannon.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 대포등장(self.ctx)


class 대포등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[104]):
            return 소환해제(self.ctx)


class 소환해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,1002,1003,1004], arg2=False)


initial_state = 시작
