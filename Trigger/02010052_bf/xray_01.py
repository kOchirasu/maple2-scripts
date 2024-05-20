""" trigger/02010052_bf/xray_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[20400,20401,20402,20403,20404,20405,20406,20407,20408,20409,20410,20411,20412,20413,20414,20415,20416,20417,20418,20419,20420,20421,20422,20423,20424,20425,20426,20427,20428,20429,20430], visible=True, fade=3.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=706) >= 1:
            return xray(self.ctx)


class xray(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[20400,20401,20402,20403,20404,20405,20406,20407,20408,20409,20410,20411,20412,20413,20414,20415,20416,20417,20418,20419,20420,20421,20422,20423,20424,20425,20426,20427,20428,20429,20430], fade=3.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=706) < 1:
            return idle(self.ctx)


initial_state = idle
