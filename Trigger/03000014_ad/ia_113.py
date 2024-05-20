""" trigger/03000014_ad/ia_113.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000113], state=1)
        self.set_actor(trigger_id=113, visible=True, initial_sequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000113], state=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=113, initial_sequence='Dead_A')
        self.spawn_monster(spawn_ids=[91], auto_target=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=91, patrol_name='MS2PatrolData401')
        self.set_dialogue(type=1, spawn_id=91, script='$03000014_AD__IA_113__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=291, spawn_ids=[91]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[91])
        self.set_timer(timer_id='301', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='301'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
