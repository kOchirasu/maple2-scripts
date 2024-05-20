""" trigger/02010051_bf/soundeffect05.xml """
import trigger_api


class 대기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[6000]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6001]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6002]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[6003]) # DoorOpen vibrate
        self.set_effect(trigger_ids=[900])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 음성연출(self.ctx)


class 음성연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=10)
        self.set_effect(trigger_ids=[900], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 대기02(self.ctx)


class 대기02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10000]):
            # 보스전투 개시
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[900])


initial_state = 대기01
