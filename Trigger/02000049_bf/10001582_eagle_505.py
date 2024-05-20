""" trigger/02000049_bf/10001582_eagle_505.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000333], state=1)
        self.set_actor(trigger_id=505, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000333], state=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=505, initial_sequence='Idle_A')
        self.spawn_monster(spawn_ids=[5005], auto_target=False)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=5005, patrol_name='MS2PatrolData_505')
        self.set_timer(timer_id='1', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[5005])
        self.set_timer(timer_id='2', seconds=50)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
