""" trigger/02010052_bf/invisiblewall03.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[20300,20301,20302,20303,20304,20305,20306,20307,20308,20309,20310,20311,20312,20313,20314,20315,20316,20317,20318,20319,20320,20321,20322,20323,20324,20325,20326,20327,20328,20329,20330], visible=True, fade=3.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=712) >= 1:
            return 벽면처리(self.ctx)


class 벽면처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[20300,20301,20302,20303,20304,20305,20306,20307,20308,20309,20310,20311,20312,20313,20314,20315,20316,20317,20318,20319,20320,20321,20322,20323,20324,20325,20326,20327,20328,20329,20330], fade=3.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=712) < 1:
            return 시작(self.ctx)


initial_state = 시작
