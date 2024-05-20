""" trigger/80000009_bonus/trigger_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[801,802,803,804,805,806,807,808,809,810])
        self.set_interact_object(trigger_ids=[10000212], state=1)
        self.set_mesh(trigger_ids=[201,202,203,204,205])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000212], state=0):
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=401, spawn_ids=[105]):
            return 몬스터소멸(self.ctx)


class 몬스터소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105])
        self.set_timer(timer_id='5', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 아이템(self.ctx)


class 아이템(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_item(spawn_ids=[505])
        self.set_effect(trigger_ids=[810], visible=True)
        self.set_mesh(trigger_ids=[205], visible=True)
        self.set_interact_object(trigger_ids=[10000212], state=2)


initial_state = 대기
