""" trigger/02000329_bf/battlezone_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6602,6601])
        self.set_mesh(trigger_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], visible=True, interval=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return 애플몽키소환(self.ctx)
        if self.monster_dead(spawn_ids=[1101,1102]):
            return 섹터개방(self.ctx)


class 애플몽키소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=101, text_id=20000030) # 닭장을 부수세요
        # self.set_event_ui(type=1, arg2='$02000329_BF__BATTLEZONE_01__0$', arg3='3000')
        self.set_effect(trigger_ids=[6602,6601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1101,1102]):
            return 섹터개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=101)


class 섹터개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=102, text_id=40011) # 다음 지역으로 이동하세요
        # self.set_event_ui(type=1, arg2='$02000329_BF__BATTLEZONE_01__1$', arg3='3000')
        self.set_mesh(trigger_ids=[19991])
        self.set_mesh(trigger_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=102)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
