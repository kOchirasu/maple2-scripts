""" trigger/02000532_bf/talk.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703], job_code=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=216, msg='$02000532_BF__TALK__0$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return None # Missing State: State


initial_state = idle
