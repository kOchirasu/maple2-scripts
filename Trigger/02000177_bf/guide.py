""" trigger/02000177_bf/guide.xml """
import trigger_api


class guide(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return Guide_Climb(self.ctx)


class Guide_Climb(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20001771, text_id=20001771, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return Guide_Climb_02(self.ctx)


class Guide_Climb_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20001771, text_id=20001771, duration=4000)


initial_state = guide
