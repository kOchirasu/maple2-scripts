""" trigger/02010086_bf/train_open_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000897], state=0)
        self.set_effect(trigger_ids=[7003]) # 전원 붙는 소리
        self.set_effect(trigger_ids=[7004]) # 전원 붙는 소리
        self.set_mesh(trigger_ids=[1161,1162,1163]) # 파랑 안보이는 상태

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000897], state=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        # [b:레버]를 조작하여 드럼통을 폭파시키세요.
        self.show_guide_summary(entity_id=113, text_id=20003363)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000897], state=0):
            return 작동_01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=113)


class 작동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7003], visible=True) # 전원 붙는 소리
        self.set_effect(trigger_ids=[7004], visible=True) # 전원 붙는 소리
        self.set_mesh(trigger_ids=[1171,1172,1173], interval=300, fade=10.0) # 빨간 선이
        self.set_mesh(trigger_ids=[1161,1162,1163], visible=True, interval=300, fade=10.0) # 파란 선으로
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2111], interval=30) # 드럼통 폭발
        self.set_mesh(trigger_ids=[1161,1162,1163], fade=10.0) # 파란 선도 마저 삭제
        self.set_mesh(trigger_ids=[2101], interval=50, fade=1.0) # 유리창 해제
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 벽제거(self.ctx)


class 벽제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True) # 보상으로 연결되는 포탈 제어 (켬)


initial_state = 대기
