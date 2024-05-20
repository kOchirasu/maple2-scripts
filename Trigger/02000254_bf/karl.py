""" trigger/02000254_bf/karl.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[450])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[904]):
            return 말풍선(self.ctx)
        if self.monster_in_combat(spawn_ids=[106]):
            return 종료(self.ctx)


class 말풍선(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='8', seconds=8)
        self.set_effect(trigger_ids=[450], visible=True)
        self.set_dialogue(type=1, spawn_id=107, script='$02000254_BF__KARL__0$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='8'):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
