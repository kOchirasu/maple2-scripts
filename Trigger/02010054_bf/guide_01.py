""" trigger/02010054_bf/guide_01.xml """
import trigger_api


class 반응대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000856], state=0):
            return 가이드01(self.ctx)


class 가이드01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20105402, text_id=20105402)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.hide_guide_summary(entity_id=20105402)
            return 감지대기(self.ctx)


class 감지대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[108]):
            return 가이드02(self.ctx)


class 가이드02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=가이드02스킵)
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 카메라이동02(self.ctx)


class 카메라이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.select_camera(trigger_id=303, enable=False)
            return 가이드02종료(self.ctx)


class 가이드02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 가이드02종료(self.ctx)


class 가이드02종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=20105403, text_id=20105403)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000860,10000861], state=0):
            self.hide_guide_summary(entity_id=20105403)
            return 가이드03(self.ctx)


class 가이드03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000858], state=0):
            return 가이드03종료(self.ctx)


class 가이드03종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20105405, text_id=20105405)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.hide_guide_summary(entity_id=20105405)
            return 반응대기02(self.ctx)


class 반응대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[109]):
            return 반응대기02종료(self.ctx)


class 반응대기02종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20105403, text_id=20105403)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            self.hide_guide_summary(entity_id=20105403)
            return 가이드04(self.ctx)


class 가이드04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000857], state=0):
            return 가이드04종료(self.ctx)


class 가이드04종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20105402, text_id=20105402)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.hide_guide_summary(entity_id=20105402)
            return 감지대기02(self.ctx)


class 감지대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[110]):
            self.set_event_ui(type=1, arg2='$02010054_BF__GUIDE_01__0$', arg3='5000', arg4='0')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 반응대기
