""" trigger/02000254_bf/pillar_03.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000442], state=0)
        self.set_skill(trigger_ids=[703])
        self.set_effect(trigger_ids=[446])
        self.set_effect(trigger_ids=[447])
        self.set_effect(trigger_ids=[462])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=907, spawn_ids=[105]):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000442], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000442], state=0):
            return 스턴(self.ctx)
        if not self.npc_detected(box_id=907, spawn_ids=[105]):
            return 시작대기중(self.ctx)


class 스턴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[446], visible=True)
        self.set_effect(trigger_ids=[447], visible=True)
        self.set_effect(trigger_ids=[462], visible=True)
        self.set_skill(trigger_ids=[703], enable=True)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스턴2(self.ctx)


class 스턴2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[703])
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
