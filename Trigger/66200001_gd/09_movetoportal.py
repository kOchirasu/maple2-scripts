""" trigger/66200001_gd/09_movetoportal.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(key='MoveToTeamPortal', value=0)
        # LeavePortal_Safe (arg3=작동여부)
        self.set_portal(portal_id=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MoveToTeamPortal') == 1:
            return MoveUserbyTag(self.ctx)


class MoveUserbyTag(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_to_portal(box_id=9900, user_tag_id=1, portal_id=11) # Tag1=Blue
        self.move_to_portal(box_id=9900, user_tag_id=2, portal_id=12) # Tag2=Red
        # TheNumberOfBlueTeamWaiting
        self.set_user_value(trigger_id=11, key='BannerCheckIn', value=1)
        # TheNumberOfRedTeamWaiting
        self.set_user_value(trigger_id=13, key='BannerCheckIn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9900]):
            return MoveUserbyTag(self.ctx)
        if self.user_value(key='MoveToTeamPortal') == 2:
            return QuitDelay(self.ctx)


class QuitDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=6, enable=True) # 게임 시작 후 입장한 유저 퇴장 조치


initial_state = Wait
