""" trigger/02000316_bf/qeagle_06.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000574], state=1)
        self.set_actor(trigger_id=911, initial_sequence='Attack_Idle_A')
        self.set_effect(trigger_ids=[912])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000574], state=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=911, visible=True, initial_sequence='Attack_Idle_A')
        self.set_effect(trigger_ids=[912], visible=True)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 그리폰제거(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=911, initial_sequence='Attack_Idle_A')
        self.set_effect(trigger_ids=[912])


class 그리폰제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
