""" trigger/63000006_cs/shake02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 다리흔들기준비(self.ctx)


class 다리흔들기준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[910])
        self.set_skill(trigger_ids=[911])
        self.set_skill(trigger_ids=[912])
        self.set_skill(trigger_ids=[913])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬발동01(self.ctx)


class 스킬발동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=42)
        self.set_skill(trigger_ids=[910], enable=True)
        self.set_skill(trigger_ids=[911], enable=True)
        self.set_skill(trigger_ids=[912], enable=True)
        self.set_skill(trigger_ids=[913], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 다리흔들기준비(self.ctx)
        if self.user_detected(box_ids=[9002]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[910])
        self.set_skill(trigger_ids=[911])
        self.set_skill(trigger_ids=[912])
        self.set_skill(trigger_ids=[913])


initial_state = 대기
