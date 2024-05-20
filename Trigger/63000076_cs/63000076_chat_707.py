""" trigger/63000076_cs/63000076_chat_707.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[707]):
            return 잡담_01_707(self.ctx)


class 잡담_01_707(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=119, msg='$63000076_CS__63000076_CHAT_707__0$', duration=2500) # 이거 이거 열어봐도 돼요?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 잡담_02_707(self.ctx)


class 잡담_02_707(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=119, msg='$63000076_CS__63000076_CHAT_707__1$', duration=2500) # 안 돼요?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
