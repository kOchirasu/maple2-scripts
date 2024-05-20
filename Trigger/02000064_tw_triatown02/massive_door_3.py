""" trigger/02000064_tw_triatown02/massive_door_3.xml """
import trigger_api


class 오픈대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[11,12,13], visible=True)
        self.set_actor(trigger_id=1, visible=True, initial_sequence='Eff_MassiveEvent_Bridge_Opened')
        self.set_actor(trigger_id=2, visible=True, initial_sequence='Eff_MassiveEvent_Bridge_Opened')
        self.set_actor(trigger_id=3, visible=True, initial_sequence='Eff_MassiveEvent_Door_Closed')


class 오픈중1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 오픈중2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='1')


class 오픈중2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 클로즈대기중(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='2')
        self.set_actor(trigger_id=3, visible=True, initial_sequence='Eff_MassiveEvent_Door_Opened')


class 클로즈대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=114)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 클로즈5초전(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='3')


class 클로즈5초전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.notice(script='$02000064_TW_Triatown02__MASSIVE_DOOR_3__0$', arg3=True)
        self.set_timer(timer_id='4', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 클로즈중1(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='4')
        self.set_actor(trigger_id=3, visible=True, initial_sequence='Eff_MassiveEvent_Door_Closed')


class 클로즈중1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 클로즈중2(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='5')


class 클로즈중2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.notice(script='$02000064_TW_Triatown02__MASSIVE_DOOR_3__1$', arg3=True)
        self.set_timer(timer_id='6', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 오픈대기중(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='6')


initial_state = 오픈대기중
