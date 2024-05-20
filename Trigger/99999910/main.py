""" trigger/99999910/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[8002], return_view=False)
        pass


initial_state = idle
