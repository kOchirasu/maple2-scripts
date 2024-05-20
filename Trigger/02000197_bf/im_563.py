""" trigger/02000197_bf/im_563.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000563], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)

    def on_exit(self) -> None:
        self.spawn_monster(spawn_ids=[102])


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000563], state=0):
            return NPC이동(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[102])
        self.spawn_monster(spawn_ids=[1102])


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1102, patrol_name='MS2PatrolData_563')
        self.set_dialogue(type=1, spawn_id=1102, script='$02000197_BF__IM_563__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=563, spawn_ids=[1102]):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1102])
        self.set_timer(timer_id='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
