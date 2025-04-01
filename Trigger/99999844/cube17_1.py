""" trigger/99999844/cube17_1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CubeOff') == 1:
            return Off_1(self.ctx)


class Off_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return On_1(self.ctx)


class On_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Off_2(self.ctx)


class Off_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return On_2(self.ctx)


class On_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Off_3(self.ctx)


class Off_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return On_3(self.ctx)


class On_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=300):
            return Off_4(self.ctx)


class Off_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=150):
            return On_4(self.ctx)


class On_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=150):
            return Off_5(self.ctx)


class Off_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=150):
            return On_5(self.ctx)


class On_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=150):
            return Off_6(self.ctx)


class Off_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=150):
            return On_6(self.ctx)


class On_6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=150):
            return Off_7(self.ctx)


class Off_7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[5029,5030,5031,5032])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=200):
            self.set_user_value(trigger_id=920017, key='CubeOff', value=0)
            self.set_user_value(trigger_id=910017, key='Cube', value=2)
            return 대기(self.ctx)


initial_state = 대기
