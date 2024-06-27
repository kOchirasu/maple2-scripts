""" trigger/99999905/wait.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 시간표확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=10)
        self.set_event_ui_script(type=BannerType.Text, script='$99999905__WAIT__0$', duration=5000, box_ids=['0'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=101) >= 10:
            return 시작(self.ctx)
        if self.time_expired(timer_id='10'):
            return 시간표확인(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='88', seconds=1200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='88'):
            return 시간표확인(self.ctx)


initial_state = 시간표확인
