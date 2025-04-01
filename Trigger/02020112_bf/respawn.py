""" trigger/02020112_bf/respawn.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.limit_spawn_npc_count(limit_count=200)
        self.set_user_value(key='respawn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 1:
            return 스폰시작(self.ctx)
        if self.user_value(key='respawn') == 2:
            return 종료(self.ctx)


class 스폰시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020112_BF__RESPAWN__0$', duration=5000)
        self.spawn_monster(spawn_ids=[141,142,143,144], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='respawn') == 2:
            return 종료(self.ctx)
        return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
