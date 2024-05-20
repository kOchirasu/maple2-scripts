""" trigger/02000352_bf/lever_01.xml """
import trigger_api


class 닫힘상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6111], visible=True) # 벽
        self.set_mesh(trigger_ids=[6101]) # 벽

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000822], state=1):
            return 작동(self.ctx)


class 작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=111, text_id=20000080) # 스위치를 정지하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000822], state=0):
            return 열림상태(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=111)


class 열림상태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_cinematic_ui(type=1)
        # self.set_cinematic_ui(type=3)
        # self.select_camera(trigger_id=8001)
        # self.set_skip(state=열림)
        self.set_timer(timer_id='1', seconds=1)
        self.set_effect(trigger_ids=[9000002], visible=True) # Sound EFfect on
        self.set_mesh(trigger_ids=[6111], interval=200, fade=15.0) # 벽 해제
        self.set_mesh(trigger_ids=[6101], visible=True, interval=200, fade=15.0) # 벽 해제

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6002], fade=10.0) # 벽 해제
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 열림_끝(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        # self.set_cinematic_ui(type=0)
        # self.set_cinematic_ui(type=2)
        # self.set_cinematic_ui(type=7)
        pass


class 열림_끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=113, text_id=40011) # 스위치를 정지하세요
        self.select_camera(trigger_id=8001, enable=False) # 연출 카메라
        # self.set_event_ui(type=1, arg2='관문이 개방되었습니다. \\n다음 지역으로 이동할 수 있습니다.', arg3='3000')


initial_state = 닫힘상태
