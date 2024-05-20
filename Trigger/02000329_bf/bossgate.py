""" trigger/02000329_bf/bossgate.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[710]):
            return 사다리가이드(self.ctx)


class 사다리가이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=106, text_id=20000060) # 다음 지역으로 이동하세요
        # self.set_event_ui(type=1, arg2='$02000329_BF__BOSSGATE__0$', arg3='3000')
        self.set_timer(timer_id='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 대기(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=106)


initial_state = 대기
