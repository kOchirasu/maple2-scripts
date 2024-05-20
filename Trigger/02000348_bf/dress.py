""" trigger/02000348_bf/dress.xml """
import trigger_api


"""
플레이어 감지
60002 : 모든 영역
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001,2002], visible=True)
        self.set_interact_object(trigger_ids=[10001065], state=1)

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
        self.set_event_ui(type=1, arg2='$02000348_BF__DRESS__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001,2002], interval=200)
        self.show_guide_summary(entity_id=20003444, text_id=20003444, duration=5000)


initial_state = idle
