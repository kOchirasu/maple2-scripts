""" trigger/63000076_cs/63000076_chat_706.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706]):
            return 잡담_01_706(self.ctx)


class 잡담_01_706(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=118, msg='$63000076_CS__63000076_CHAT_706__0$', duration=2500) # 신발… 아…이 신발, 신어보고 싶어요

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
