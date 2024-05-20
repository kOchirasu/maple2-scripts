""" trigger/51000003_dg/hidden.xml """
import trigger_api


# 여기서 부터 시작
class Start(trigger_api.Trigger):
    pass


class Hidden_ready_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=99) # 임시 히든포탈
        self.set_event_ui(type=1, arg2='$51000003_DG__HIDDEN__0$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Hidden_ready_02(self.ctx)


class Hidden_ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$51000003_DG__HIDDEN__1$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Hidden_ready_03(self.ctx)


class Hidden_ready_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=0, arg2='6,6', arg3='0', arg4='0')
        self.select_camera(trigger_id=8002)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Hidden_ready_04(self.ctx)


class Hidden_ready_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$61000004_ME__TRIGGER_01__1$', count=5)
        self.set_achievement(trigger_id=710, type='trigger', achieve='boomboombeach_hidden_start')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Hidden_Start(self.ctx)


class Hidden_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991104, key='Round_06', value=1)
        self.set_user_value(trigger_id=991105, key='Round_06', value=1)
        self.set_user_value(trigger_id=991106, key='Round_06', value=1)
        self.set_user_value(trigger_id=991107, key='Round_06', value=1)
        self.set_user_value(trigger_id=991108, key='Round_06', value=1)
        self.set_timer(timer_id='150', seconds=150, interval=1)


initial_state = Start
