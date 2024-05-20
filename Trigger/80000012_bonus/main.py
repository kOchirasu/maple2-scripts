""" trigger/80000012_bonus/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[199], auto_target=False) # 웨이브 장치 작동

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='60'):
            return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
