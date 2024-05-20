""" trigger/02000539_bf/talk.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703], job_code=0):
            return 말풍선1(self.ctx)
        if self.user_detected(box_ids=[704], job_code=0):
            return 말풍선2(self.ctx)


class 말풍선1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=201, msg='$02000539_BF__TALK__0$', duration=3500)
        self.add_balloon_talk(spawn_id=201, msg='$02000539_BF__TALK__1$', duration=3500, delay_tick=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return idle(self.ctx)


class 말풍선2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=202, msg='$02000539_BF__TALK__2$', duration=3500)
        self.add_balloon_talk(spawn_id=202, msg='$02000539_BF__TALK__3$', duration=3500, delay_tick=3500)
        self.add_balloon_talk(spawn_id=202, msg='$02000539_BF__TALK__4$', duration=3500, delay_tick=7000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return idle(self.ctx)


initial_state = idle
