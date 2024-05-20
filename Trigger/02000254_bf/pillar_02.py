""" trigger/02000254_bf/pillar_02.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000441], state=0)
        self.set_skill(trigger_ids=[702])
        self.set_effect(trigger_ids=[444])
        self.set_effect(trigger_ids=[445])
        self.set_effect(trigger_ids=[461])

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=906, spawn_ids=[104]):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000441], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000441], state=0):
            return 스턴(self.ctx)
        if not self.npc_detected(box_id=906, spawn_ids=[104]):
            return 시작대기중(self.ctx)


class 스턴(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[444], visible=True)
        self.set_effect(trigger_ids=[445], visible=True)
        self.set_effect(trigger_ids=[461], visible=True)
        self.set_skill(trigger_ids=[702], enable=True)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스턴2(self.ctx)


class 스턴2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[702])
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
