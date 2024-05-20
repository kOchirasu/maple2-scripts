""" trigger/02000344_bf/dress.xml """
import trigger_api


"""
플레이어 감지
60002 : 모든 영역
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6701,6702,6703,6704,6705], visible=True) # 가림막
        self.set_mesh(trigger_ids=[6711,6712,6713,6714,6715], interval=10) # 가림막
        self.set_interact_object(trigger_ids=[10001066], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=60002) >= 1:
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20003441, text_id=20003441, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000344_BF__DRESS__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6701,6702,6703,6704,6705]) # 가림막
        self.set_mesh(trigger_ids=[6711,6712,6713,6714,6715], visible=True, interval=10) # 가림막
        self.show_guide_summary(entity_id=20003444, text_id=20003444, duration=5000)


initial_state = idle
