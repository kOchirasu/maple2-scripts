""" trigger/02010086_bf/train_open.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001]) # 전원 붙는 소리
        self.set_effect(trigger_ids=[7002]) # 전원 붙는 소리
        self.set_mesh(trigger_ids=[1061,1062,1063]) # 안보이는 상태
        self.set_mesh(trigger_ids=[2011,2012,2013]) # 안보이는 상태
        self.set_interact_object(trigger_ids=[10000896], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000896], state=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        # [b:레버]를 조작하여 드럼통을 폭파시키세요.
        self.show_guide_summary(entity_id=113, text_id=20003363)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000896], state=0):
            return 작동_01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=113)


class 작동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001], visible=True) # 전원 붙는 소리
        self.set_effect(trigger_ids=[7002], visible=True) # 전원 붙는 소리
        self.set_mesh(trigger_ids=[1071,1072,1073], interval=300, fade=10.0) # 빨간 선이
        self.set_mesh(trigger_ids=[1061,1062,1063], visible=True, interval=300, fade=10.0) # 파란 선으로
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1055], interval=30) # 드럼통 폭발
        self.set_mesh(trigger_ids=[1061,1062,1063], fade=10.0) # 파란 선도 마저 삭제
        self.set_mesh(trigger_ids=[1005], interval=50, fade=1.0) # 유리창 해제
        self.set_actor(trigger_id=1022, visible=True, initial_sequence='Opened') # 문 열림
        self.set_mesh(trigger_ids=[1021], fade=10.0) # 벽 해제
        self.set_timer(timer_id='1', seconds=1)


initial_state = 대기
