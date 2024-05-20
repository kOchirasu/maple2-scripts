""" trigger/63000076_cs/63000076_chat_705.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705]):
            return 잡담_01_705(self.ctx)


class 잡담_01_705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=116, msg='$63000076_CS__63000076_CHAT_705__0$', duration=2500) # 이거 누르면 소리 나요

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 잡담_02_705(self.ctx)


class 잡담_02_705(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=117, msg='$63000076_CS__63000076_CHAT_705__1$', duration=2500) # 소리 들어보고 싶어요

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
