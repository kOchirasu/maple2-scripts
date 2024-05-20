""" trigger/02000486_bf/107_text.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9901]):
            return 알림(self.ctx)


class 알림(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=900, is_relative=True) <= 30 or self.npc_hp(spawn_id=901, is_relative=True) <= 30:
            return 텍스트(self.ctx)


class 텍스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000486_BF__107_TEXT__0$', arg3='4000')

    def on_tick(self) -> trigger_api.Trigger:
        pass


initial_state = 유저감지
