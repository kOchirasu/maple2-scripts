""" trigger/80000008_bonus/trigger_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[801,802,803,804,805])
        self.set_effect(trigger_ids=[806,807,808,809,810])
        self.set_mesh(trigger_ids=[201,202,203,204,205])
        self.set_interact_object(trigger_ids=[10000212], state=1)

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
        self.set_timer(timer_id='6', seconds=1, start_delay=1)
        self.set_effect(trigger_ids=[801,802,803,804,805], visible=True)
        self.set_effect(trigger_ids=[806,807,808,809,810], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 꽝(self.ctx)


class 꽝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.destroy_monster(spawn_ids=[102])
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])
        self.destroy_monster(spawn_ids=[105])
        self.set_mesh(trigger_ids=[201,202,203,204,205], visible=True)
        self.set_interact_object(trigger_ids=[10000208], state=2)
        self.set_interact_object(trigger_ids=[10000209], state=2)
        self.set_interact_object(trigger_ids=[10000210], state=2)
        self.set_interact_object(trigger_ids=[10000211], state=2)
        self.set_interact_object(trigger_ids=[10000212], state=2)


initial_state = 대기
