""" trigger/02000336_bf/train_lever_02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8211,8212,8213,8214]) # 안보이는 상태
        self.set_interact_object(trigger_ids=[10000897], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000897], state=0):
            return 작동_01(self.ctx)


class 작동_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8211,8212,8213,8214], visible=True, interval=300, fade=10.0) # 빨간 선이
        self.set_mesh(trigger_ids=[8201,8202,8203,8204], interval=300, fade=10.0) # 파란 선으로
        self.set_effect(trigger_ids=[7011], visible=True)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 작동_02(self.ctx)


class 작동_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[8021,8022,8023,8024], fade=10.0) # 벽은 사라지고
        self.set_skill(trigger_ids=[5807], enable=True) # 벽 날리는 스킬
        self.set_mesh(trigger_ids=[8205], interval=30) # 드럼통 폭발
        self.set_mesh(trigger_ids=[8211,8212,8213,8214], fade=10.0) # 파란 선도 마저 삭제


initial_state = 시작
