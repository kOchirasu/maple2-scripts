""" trigger/02000022_bf/ia_105.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=105, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        return 오브젝트반응(self.ctx)


class 오브젝트반응(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000094], state=0):
            return 개구리보이기(self.ctx)


class 개구리보이기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=105, visible=True, initial_sequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000094], state=1):
            return 시작대기중(self.ctx)

    def on_exit(self) -> None:
        self.set_actor(trigger_id=105, initial_sequence='Idle_A')


initial_state = 시작대기중
