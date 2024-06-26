""" trigger/52010028_qd/messege.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


# 지속적으로 시스템 메시지를 띄워줌
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2003]):
            return messege(self.ctx)
        if self.user_detected(box_ids=[2004]):
            return messege(self.ctx)
        if self.user_detected(box_ids=[2005]):
            return messege(self.ctx)
        if self.user_detected(box_ids=[2006]):
            return messege(self.ctx)
        if self.user_detected(box_ids=[2007]):
            return messege(self.ctx)
        if self.user_detected(box_ids=[2008]):
            return messege(self.ctx)
        if self.user_detected(box_ids=[2009]):
            return messege(self.ctx)


class messege(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui_script(type=BannerType.GameOver, script='$52010028_QD__MESSEGE__0$', duration=3000, box_ids='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return idle(self.ctx)


initial_state = idle
