""" trigger/02000163_bf/01_trigger.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101])
        self.set_effect(trigger_ids=[201], visible=True)
        self.set_effect(trigger_ids=[202], visible=True)
        self.set_effect(trigger_ids=[203], visible=True)
        self.set_effect(trigger_ids=[204], visible=True)
        self.set_interact_object(trigger_ids=[10000079], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000079], state=0):
            self.destroy_monster(spawn_ids=[101])
            self.set_effect(trigger_ids=[201])
            self.set_effect(trigger_ids=[202])
            self.set_effect(trigger_ids=[203])
            self.set_effect(trigger_ids=[204])
            return 매킨생성(self.ctx)


class 매킨생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[102])
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 매킨대사(self.ctx)


class 매킨대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$02000163_BF__01_TRIGGER__0$', time=3)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=301, spawn_ids=[102]):
            return 매킨이동302(self.ctx)


class 매킨이동302(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[201], item_id=10000079)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 매킨이동304(self.ctx)


class 매킨이동304(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=304, spawn_ids=[102]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.set_timer(timer_id='1', seconds=60)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기(self.ctx)


initial_state = 대기
