""" trigger/02000091_bf/im_102.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000533], state=1)
        self.set_actor(trigger_id=2102, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000533], state=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[102])
        self.set_actor(trigger_id=2102, initial_sequence='Idle_A')


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_Gull_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=1102, spawn_ids=[102]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])
        self.set_timer(timer_id='102', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='102'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
