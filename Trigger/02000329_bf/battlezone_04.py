""" trigger/02000329_bf/battlezone_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6609,6610])
        self.set_mesh(trigger_ids=[1531,1532,1533,1534,1535,1536,1537,1538,1539,1540], visible=True, interval=1000)
        self.set_mesh(trigger_ids=[19994], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[704]):
            return 애플몽키소환(self.ctx)
        if self.monster_dead(spawn_ids=[1109,1110]):
            return 섹터개방(self.ctx)


class 애플몽키소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=101, text_id=20000030) # 닭장을 부수세요
        # self.set_event_ui(type=1, arg2='닭장을 공격하여 닭을 구출하세요', arg3='3000')
        self.spawn_monster(spawn_ids=[704], auto_target=False)
        self.set_effect(trigger_ids=[6609,6610], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1109,1110]):
            return 섹터개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=101)


class 섹터개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=102, text_id=40011) # 다음 지역으로 이동하세요
        # self.set_event_ui(type=1, arg2='$02000329_BF__BATTLEZONE_04__0$', arg3='3000')
        self.set_mesh(trigger_ids=[19994])
        self.set_mesh(trigger_ids=[1531,1532,1533,1534,1535,1536,1537,1538,1539,1540], fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=102)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
