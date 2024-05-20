""" trigger/02010052_bf/invisiblewall02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210,20211,20212,20213,20214,20215,20216,20217,20218,20219,20220,20221,20222,20223,20224,20225,20226,20227,20228,20229,20230], visible=True, fade=3.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=711) >= 1:
            return 벽면처리(self.ctx)


class 벽면처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210,20211,20212,20213,20214,20215,20216,20217,20218,20219,20220,20221,20222,20223,20224,20225,20226,20227,20228,20229,20230], fade=3.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=711) < 1:
            return 시작(self.ctx)


initial_state = 시작
