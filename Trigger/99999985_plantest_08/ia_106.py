""" trigger/99999985_plantest_08/ia_106.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000005], state=1)
        self.set_actor(trigger_id=1061, visible=True, initial_sequence='SOS_B')

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[302])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000005], state=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=1061, initial_sequence='SOS_B')
        self.destroy_monster(spawn_ids=[302])
        self.spawn_monster(spawn_ids=[106])


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=106, patrol_name='MS2PatrolData106')
        self.set_dialogue(type=1, spawn_id=106, script='$02000116_BF__IA_106__0$', time=2)
        self.set_dialogue(type=1, spawn_id=106, script='$02000116_BF__IA_106__1$', time=2, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=106, spawn_ids=[106]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[106])
        self.set_timer(timer_id='106', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='106'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
