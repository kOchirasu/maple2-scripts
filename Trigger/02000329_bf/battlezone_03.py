""" trigger/02000329_bf/battlezone_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6605,6606,6607,6608])
        self.set_mesh(trigger_ids=[1521,1522,1523,1524,1525,1526,1527,1528,1529,1530], visible=True, interval=1000)
        self.set_mesh(trigger_ids=[19993], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703]):
            return 애플몽키소환(self.ctx)
        if self.monster_dead(spawn_ids=[1105,1106,1107,1108]):
            return 섹터개방(self.ctx)


class 애플몽키소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=101, text_id=20000030) # 닭장을 부수세요
        # self.set_event_ui(type=1, arg2='닭장을 공격하여 닭을 구출하세요', arg3='3000')
        self.spawn_monster(spawn_ids=[703], auto_target=False)
        self.set_effect(trigger_ids=[6605,6606,6607,6608], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1105,1106,1107,1108]):
            return 섹터개방(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=101)


class 섹터개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_timer(timer_id='3', seconds=3)
        self.show_guide_summary(entity_id=102, text_id=40011) # 다음 지역으로 이동하세요
        # self.set_event_ui(type=1, arg2='$02000329_BF__BATTLEZONE_03__0$', arg3='3000')
        self.set_mesh(trigger_ids=[19993])
        self.set_mesh(trigger_ids=[1521,1522,1523,1524,1525,1526,1527,1528,1529,1530], fade=10.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=102)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
