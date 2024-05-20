""" trigger/02000283_bf/ladder.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[511])
        self.set_ladder(trigger_ids=[512])
        self.set_ladder(trigger_ids=[513])
        self.set_ladder(trigger_ids=[514])
        self.set_interact_object(trigger_ids=[10000429], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[2001]):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000429], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000429], state=0):
            return 사다리생성(self.ctx)


class 사다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[511], visible=True, enable=True)
        self.set_ladder(trigger_ids=[512], visible=True, enable=True)
        self.set_ladder(trigger_ids=[513], visible=True, enable=True)
        self.set_ladder(trigger_ids=[514], visible=True, enable=True)
        self.set_timer(timer_id='10', seconds=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
