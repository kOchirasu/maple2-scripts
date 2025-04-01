""" trigger/02010051_bf/eventtimer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            return 시간체크(self.ctx)


class 시간체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='timercheck') == 1:
            return 업적이벤트(self.ctx)
        if self.wait_tick(wait_tick=240000):
            return 종료(self.ctx)


class 업적이벤트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9003, type='trigger', achieve='CaboTimeEvent')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 업적이벤트(self.ctx)
        if self.monster_dead(spawn_ids=[99]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
