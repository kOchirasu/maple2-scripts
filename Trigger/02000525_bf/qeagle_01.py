""" trigger/02000525_bf/qeagle_01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000569], state=1)
        self.set_actor(trigger_id=901, initial_sequence='Attack_Idle_A')
        self.set_effect(trigger_ids=[902])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000569], state=0):
            return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=901, visible=True, initial_sequence='Attack_Idle_A')
        self.set_effect(trigger_ids=[902], visible=True)
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 그리폰제거(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=901, initial_sequence='Attack_Idle_A')
        self.set_effect(trigger_ids=[902])


class 그리폰제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=600)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
