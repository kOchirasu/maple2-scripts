""" trigger/02000336_bf/train_open.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[16014,16015,16016]) # 안보이는 상태
        self.set_interact_object(trigger_ids=[10000805], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=706) >= 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=113, text_id=20003363)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000805], state=0):
            return 작동_01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=113)


class 작동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[16011,16012,16013], interval=300, fade=10.0) # 빨간 선이
        self.set_mesh(trigger_ids=[16014,16015,16016], visible=True, interval=300, fade=10.0) # 파란 선으로
        self.set_effect(trigger_ids=[7013], visible=True)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_skill(trigger_ids=[5802], enable=True) # 벽 날리는 스킬
        self.set_mesh(trigger_ids=[16001], interval=30) # 드럼통 폭발
        self.set_mesh(trigger_ids=[16014,16015,16016], fade=10.0) # 파란 선도 마저 삭제
        self.set_mesh(trigger_ids=[16000], interval=50, fade=1.0) # 유리창 해제
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return 작동_03(self.ctx)


class 작동_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[305,306,307,308], auto_target=False) # 기본 배치 될 몬스터 등장


initial_state = 대기
