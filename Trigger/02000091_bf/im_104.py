""" trigger/02000091_bf/im_104.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000535], state=1)
        self.set_actor(trigger_id=2104, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000535], state=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[104])
        self.set_actor(trigger_id=2104, initial_sequence='Idle_A')


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_Gull_104')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=1104, spawn_ids=[104]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104])
        self.set_timer(timer_id='104', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='104'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
