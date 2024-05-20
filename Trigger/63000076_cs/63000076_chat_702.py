""" trigger/63000076_cs/63000076_chat_702.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[30000375], quest_states=[1]):
            return 잡담_01_702(self.ctx)


class 잡담_01_702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=103, msg='$63000076_CS__63000076_CHAT_702__0$', duration=2000) # 사람이다! 사람!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 잡담_02_702(self.ctx)


class 잡담_02_702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004372$$pp:가,이$ 사람도 초대했나?
        self.add_balloon_talk(spawn_id=101, msg='$63000076_CS__63000076_CHAT_702__1$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 잡담_03_702(self.ctx)


class 잡담_03_702(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # $npcName:11004372$$pp:는,은$ 착하니까, 그랬을 수도 있지
        self.add_balloon_talk(spawn_id=102, msg='$63000076_CS__63000076_CHAT_702__2$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
