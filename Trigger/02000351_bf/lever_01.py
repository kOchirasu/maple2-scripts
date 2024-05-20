""" trigger/02000351_bf/lever_01.xml """
import trigger_api


class 닫힘상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6001,6002], visible=True) # 벽
        self.set_mesh(trigger_ids=[6020,6021,6022,6023,6024,6025,6026]) # 벽

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000818], state=1):
            return 작동(self.ctx)


class 작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=111, text_id=20000080) # 스위치를 정지하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000818], state=0):
            return 열림상태(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=111)


class 열림상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_cinematic_ui(type=1)
        # self.set_cinematic_ui(type=3)
        # self.select_camera(trigger_id=8001) # 연출 카메라
        self.set_timer(timer_id='2', seconds=2)
        self.set_mesh(trigger_ids=[6010,6011,6012,6013,6014,6015,6016], interval=200, fade=15.0) # 벽 해제
        self.set_mesh(trigger_ids=[6020,6021,6022,6023,6024,6025,6026], visible=True, interval=200, fade=15.0) # 벽 해제
        self.set_effect(trigger_ids=[9000002], visible=True) # Object_Electricity_On_01

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6001,6002], fade=10.0) # 벽 해제
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 열림_끝(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 열림_끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8001, enable=False) # 연출 카메라


initial_state = 닫힘상태
