""" trigger/52100303_qd/mesh.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return 첫번째길막(self.ctx)


class 첫번째길막(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Mesh') == 2:
            self.set_mesh(trigger_ids=[4002], visible=True)
            return 이페이즈(self.ctx)


class 이페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Mesh') == 3:
            self.set_ai_extra_data(key='Thunder', value=2)
            self.set_mesh(trigger_ids=[4003], visible=True)
            return 삼페이즈(self.ctx)


class 삼페이즈(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Mesh') == 4:
            self.set_mesh(trigger_ids=[4004], visible=True)
            self.destroy_monster(spawn_ids=[111])
            return 진짜마지막(self.ctx)


class 진짜마지막(trigger_api.Trigger):
    pass


initial_state = 대기
