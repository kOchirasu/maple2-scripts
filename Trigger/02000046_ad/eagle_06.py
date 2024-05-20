""" trigger/02000046_ad/eagle_06.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000298], state=1)
        self.set_actor(trigger_id=206, visible=True, initial_sequence='Dead_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000298], state=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=206, initial_sequence='Dead_A')
        self.spawn_monster(spawn_ids=[306], auto_target=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=306, patrol_name='MS2PatrolData_206')
        self.set_dialogue(type=1, spawn_id=306, script='$02000046_AD__EAGLE_06__0$', time=2)
        self.set_timer(timer_id='1', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[306])

    def on_tick(self) -> trigger_api.Trigger:
        return 시작대기중(self.ctx)


initial_state = 시작대기중
