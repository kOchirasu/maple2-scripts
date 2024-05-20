""" trigger/02000252_bf/open_door.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8903]) # 가이드 화살표

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=909) >= 1:
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002526, text_id=20002526) # 잔해를 조사하여 [b:열쇠]를 찾으세요.
        self.set_effect(trigger_ids=[8903], visible=True) # 가이드 화살표

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000402], state=0):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002526)
        self.set_effect(trigger_ids=[8903]) # 가이드 화살표


initial_state = idle
