""" trigger/02000352_bf/lever_check.xml """
import trigger_api


class 레버체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000823], state=0)
        self.set_interact_object(trigger_ids=[10000824], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000823], state=1):
            return 레버체크2(self.ctx)
        if self.object_interacted(interact_ids=[10000824], state=1):
            return 레버체크2(self.ctx)


class 레버체크2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000823], state=0):
            return 레버체크3_1개(self.ctx)
        if self.object_interacted(interact_ids=[10000824], state=0):
            return 레버체크4_1개(self.ctx)


class 레버체크3_1개(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000824], state=0):
            return 레버체크완료(self.ctx)


class 레버체크4_1개(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000823], state=0):
            return 레버체크완료(self.ctx)


class 레버체크완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_cinematic_ui(type=1)
        # self.set_cinematic_ui(type=3)
        # self.select_camera(trigger_id=8002)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 열림(self.ctx)


class 열림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_mesh(trigger_ids=[6054,6055,6056], interval=200, fade=15.0) # 빨간선 사라지게
        self.set_mesh(trigger_ids=[6154,6155,6156], visible=True, interval=200) # 파란선 나타나게
        self.set_effect(trigger_ids=[9000005], visible=True) # Sound EFfect on

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 열림_끝(self.ctx)

    def on_exit(self) -> None:
        # 레터박스, 플레이어 조작 불가능 해제
        # self.set_cinematic_ui(type=0)
        # self.set_cinematic_ui(type=2)
        # self.set_cinematic_ui(type=7)
        self.set_mesh(trigger_ids=[6003], fade=10.0) # 벽 해제


class 열림_끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entity_id=113, text_id=40011) # 다음 지역으로 이동하세요
        self.select_camera(trigger_id=8002, enable=False) # 연출 카메라
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=113)


class 종료(trigger_api.Trigger):
    pass


initial_state = 레버체크
