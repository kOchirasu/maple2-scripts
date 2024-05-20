""" trigger/02000335_bf/invisiblewall04.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=706) >= 1:
            return 벽면처리(self.ctx)


class 벽면처리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[7051,7052,7053,7054,7055,7056,7057,7058,7059,7060], fade=10.0) # 벽 해제


initial_state = 시작
