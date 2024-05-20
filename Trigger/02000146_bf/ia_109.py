""" trigger/02000146_bf/ia_109.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000184], state=1)
        self.set_actor(trigger_id=209, visible=True, initial_sequence='Attack_Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000184], state=0):
            return NPC등장(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=209, initial_sequence='Attack_Idle_A')
        self.spawn_monster(spawn_ids=[409])


class NPC등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=409, script='$02000146_BF__IA_109__0$', time=3)
        self.set_timer(timer_id='1', seconds=15)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[409]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
