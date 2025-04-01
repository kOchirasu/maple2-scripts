""" trigger/82000002_survival/17_noticeextraevent.xml """
import trigger_api


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='NoticeExtraEvent', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NoticeExtraEvent') == 1:
            # AI에서 신호 받아야 함
            return NoticeExtraEvent01(self.ctx)


class NoticeExtraEvent01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : 누군가 [b:모쿰]을 목격했습니다!
        self.show_guide_summary(entity_id=28200000, text_id=28200000, duration=3000)
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NoticeExtraEvent02(self.ctx)


class NoticeExtraEvent02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Mokum_Completion_01')
        self.side_npc_talk_bottom(npc_id=21001019, illust='MushroomRichPorter_normal', duration=5000, script='$82000002_survival__17_NoticeExtraEvent__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return NoticeExtraEvent03(self.ctx)


class NoticeExtraEvent03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 가이드 : [b:다섯 마리]의 모쿰이 섬 어딘가에 있습니다!
        self.show_guide_summary(entity_id=28200001, text_id=28200001, duration=5000)
        self.play_system_sound_in_box(sound='System_Mokum_Popup_UI_01')


initial_state = Setting
