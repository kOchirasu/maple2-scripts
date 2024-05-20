""" trigger/52000014_qd/collapse_2000.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2000,2001,2002,2003,2004], visible=True)
        self.set_effect(trigger_ids=[12000]) # Vibrate Short
        self.set_effect(trigger_ids=[22000]) # Vibrate Sound

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 무너짐01(self.ctx)


class 무너짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=2)
        self.set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2000__0$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 무너짐02(self.ctx)


class 무너짐02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=8)
        self.set_effect(trigger_ids=[12000], visible=True) # Vibrate Short
        self.set_effect(trigger_ids=[22000], visible=True) # Vibrate Sound
        self.set_random_mesh(trigger_ids=[2000,2001,2002,2003,2004], start_delay=5, fade=200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return None # Missing State: 무너짐03


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[12000]) # Vibrate Short
        self.set_effect(trigger_ids=[22000]) # Vibrate Sound


initial_state = 대기
