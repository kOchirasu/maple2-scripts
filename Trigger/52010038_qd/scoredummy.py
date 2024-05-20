""" trigger/52010038_qd/scoredummy.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001258], state=0):
            return 점수(self.ctx)
        if self.object_interacted(interact_ids=[10001259], state=0):
            return 점수(self.ctx)
        if self.object_interacted(interact_ids=[10001260], state=0):
            return 점수(self.ctx)
        if self.object_interacted(interact_ids=[10001261], state=0):
            return 점수(self.ctx)
        if self.object_interacted(interact_ids=[10001262], state=0):
            return 점수(self.ctx)
        if self.object_interacted(interact_ids=[10001263], state=0):
            return 점수(self.ctx)
        if self.object_interacted(interact_ids=[10001264], state=0):
            return 점수(self.ctx)
        if self.object_interacted(interact_ids=[10001265], state=0):
            return 점수(self.ctx)


class 점수(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[4030], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 대기(self.ctx)


initial_state = 대기
