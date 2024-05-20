""" trigger/02000347_bf/weather.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600])
        self.set_interact_object(trigger_ids=[10000804], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[60002]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000804], state=1)
        self.set_effect(trigger_ids=[600])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000804], state=0):
            return 비내림(self.ctx)


class 비내림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=True)
        self.set_timer(timer_id='30', seconds=30)
        self.set_event_ui(type=1, arg2='$02000347_BF__MAIN1__4$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            self.set_event_ui(type=1, arg2='$02000347_BF__MAIN1__3$', arg3='2000', arg4='0')
            return 시작(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            self.set_effect(trigger_ids=[600])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
