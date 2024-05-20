""" trigger/02020011_bf/block.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001], visible=True, fade=5.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 사라짐(self.ctx)


class 사라짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001], fade=5.0)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[101]):
            return 딜레이2(self.ctx)


class 딜레이2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 대기(self.ctx)


initial_state = 대기
