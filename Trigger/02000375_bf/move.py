""" trigger/02000375_bf/move.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], visible=True)
        self.set_breakable(trigger_ids=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023])
        self.set_interact_object(trigger_ids=[10001024], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10001024], state=0):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enable=True)
        self.set_event_ui_script(type=BannerType.Text, script='$02000375_BF__move__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=60000):
            return 레버삭제(self.ctx)


class 레버삭제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_visible_breakable_object(trigger_ids=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023])
        self.set_breakable(trigger_ids=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023])
        self.set_interact_object(trigger_ids=[10001024], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd') == 1:
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
