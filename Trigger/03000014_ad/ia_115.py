""" trigger/03000014_ad/ia_115.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000115], state=1)
        self.set_actor(trigger_id=115, visible=True, initial_sequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000115], state=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=115, initial_sequence='Dead_A')
        self.spawn_monster(spawn_ids=[93], auto_target=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=93, patrol_name='MS2PatrolData403')
        self.set_dialogue(type=1, spawn_id=93, script='$03000014_AD__IA_115__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=293, spawn_ids=[93]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[93])
        self.set_timer(timer_id='303', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='303'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
