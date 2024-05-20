""" trigger/63000076_cs/63000076_chat_708.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[708]):
            return 잡담_01_708(self.ctx)


class 잡담_01_708(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 너도 $npcName:11004372$가 불러서 왔어?
        self.add_balloon_talk(spawn_id=108, msg='$63000076_CS__63000076_CHAT_708__0$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 잡담_02_708(self.ctx)


class 잡담_02_708(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=115, msg='$63000076_CS__63000076_CHAT_708__1$', duration=2500) # 아니, 너 따라 왔어

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 잡담_03_708(self.ctx)


class 잡담_03_708(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=108, msg='$63000076_CS__63000076_CHAT_708__2$', duration=2500) # 아하…

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
