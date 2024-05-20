""" trigger/02000111_bf/101_2.xml """
import trigger_api


class 시작대기중1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000165], state=1)
        self.set_mesh(trigger_ids=[302])
        self.set_effect(trigger_ids=[402])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000165], state=0):
            return 열기1(self.ctx)


class 시작대기중2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000165], state=1)
        self.set_mesh(trigger_ids=[302])
        self.set_effect(trigger_ids=[402])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000165], state=0):
            return 열기1(self.ctx)


class 열기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[302], visible=True)
        self.set_effect(trigger_ids=[402], visible=True)
        self.set_timer(timer_id='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=202, spawn_ids=[103]):
            return 아이템1(self.ctx)
        if self.npc_detected(box_id=202, spawn_ids=[104]):
            return 아이템2(self.ctx)
        if self.npc_detected(box_id=202, spawn_ids=[105]):
            return 아이템3(self.ctx)
        if self.time_expired(timer_id='1'):
            return 시작대기중2(self.ctx)


class 아이템1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[502], item_id=10000165)
        self.set_mesh(trigger_ids=[302])
        self.set_interact_object(trigger_ids=[10000165], state=1)
        self.set_effect(trigger_ids=[402], visible=True)
        self.destroy_monster(spawn_ids=[103])

    def on_tick(self) -> trigger_api.Trigger:
        return 빠지기1(self.ctx)


class 아이템2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[502], item_id=10000165)
        self.set_mesh(trigger_ids=[302])
        self.set_interact_object(trigger_ids=[10000165], state=1)
        self.set_effect(trigger_ids=[402], visible=True)
        self.destroy_monster(spawn_ids=[104])

    def on_tick(self) -> trigger_api.Trigger:
        return 빠지기2(self.ctx)


class 아이템3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[502], item_id=10000165)
        self.set_mesh(trigger_ids=[302])
        self.set_interact_object(trigger_ids=[10000165], state=1)
        self.set_effect(trigger_ids=[402], visible=True)
        self.destroy_monster(spawn_ids=[105])

    def on_tick(self) -> trigger_api.Trigger:
        return 빠지기3(self.ctx)


class 빠지기1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 시작대기중2(self.ctx)


class 빠지기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 시작대기중2(self.ctx)


class 빠지기3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return 시작대기중2(self.ctx)


initial_state = 시작대기중1
