""" trigger/02000336_bf/train_lever_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8161,8162,8163,8164]) # 안보이는 상태
        self.set_interact_object(trigger_ids=[10000898], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000898], state=0):
            return 작동_01(self.ctx)
        if self.count_users(box_id=709) >= 1:
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=113, text_id=20003363, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000898], state=0):
            return 작동_01(self.ctx)


class 작동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8161,8162,8163,8164], visible=True, interval=300, fade=10.0) # 파란 선으로
        self.set_mesh(trigger_ids=[8261,8262,8263,8264], interval=300, fade=10.0) # 빨간 선이
        self.set_effect(trigger_ids=[7012], visible=True)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=106, text_id=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_mesh(trigger_ids=[8064,8065,8066,8067,8068], fade=10.0) # 벽은 사라지고
        self.set_skill(trigger_ids=[5808], enable=True) # 벽 날리는 스킬
        self.set_mesh(trigger_ids=[8069], interval=30) # 드럼통 폭발
        self.set_mesh(trigger_ids=[8161,8162,8163,8164], fade=10.0) # 파란 선도 마저 삭제


initial_state = 대기
