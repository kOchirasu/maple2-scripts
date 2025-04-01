""" trigger/99999844/cube7.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Cube') == 1:
            return 큐브7(self.ctx)


class 큐브7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4010], visible=True)
        self.set_mesh(trigger_ids=[5010], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.set_user_value(trigger_id=920007, key='CubeOff', value=1)
            return 메쉬제거(self.ctx)


class 메쉬제거(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Cube') == 2:
            self.set_user_value(trigger_id=910007, key='Cube', value=1)
            return 큐브제거(self.ctx)


class 큐브제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4010])
        self.set_mesh(trigger_ids=[5010])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 큐브7(self.ctx)
        if self.user_detected(box_ids=[9004]):
            self.set_user_value(trigger_id=910007, key='Cube', value=0)
            return 종료(self.ctx)
        if self.user_detected(box_ids=[9005]):
            self.set_user_value(trigger_id=910007, key='Cube', value=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4011,4012,4013,4014,4015,4016,4017,4018,4019,4020,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032,4033,4034,4035,4036,4037,4038,4039,4040], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 대기(self.ctx)


initial_state = 대기
