""" trigger/52010018_qd/main_3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[1005], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 분기점(self.ctx)


class 분기점(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[100], quest_ids=[10002851], quest_states=[2]):
            self.destroy_monster(spawn_ids=[1005])
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[100], quest_ids=[10002852], quest_states=[1]):
            self.destroy_monster(spawn_ids=[1005])
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[100], quest_ids=[10002853], quest_states=[1]):
            self.destroy_monster(spawn_ids=[1005])
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[100], quest_ids=[10002853], quest_states=[2]):
            self.destroy_monster(spawn_ids=[1005])
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[100], quest_ids=[10002851], quest_states=[3]):
            return 분기점2(self.ctx)


class 분기점2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[100], quest_ids=[10002852], quest_states=[2]):
            return 종료(self.ctx)
        if self.quest_user_detected(box_ids=[100], quest_ids=[10002852], quest_states=[3]):
            return 종료(self.ctx)
        if not self.quest_user_detected(box_ids=[100], quest_ids=[10002852], quest_states=[2]):
            self.destroy_monster(spawn_ids=[1005])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
