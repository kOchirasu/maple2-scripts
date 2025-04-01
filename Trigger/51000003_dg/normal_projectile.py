""" trigger/51000003_dg/normal_projectile.xml """
import trigger_api


"""
플레이어 감지
직사형 일반발사체
"""
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[301,302,303,304,305,306,307,308,309,310,311,312,351,352,353,354,355,356,357,358,359,360,361,362])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01') == 1:
            return Round_01(self.ctx)
        if self.user_value(key='Round_02') == 1:
            return Round_02(self.ctx)
        if self.user_value(key='Round_03') == 1:
            return Round_03(self.ctx)
        if self.user_value(key='Round_04') == 1:
            return Round_04(self.ctx)
        if self.user_value(key='Round_05') == 1:
            return None # Missing State: Round_05
        if self.user_value(key='Round_06') == 1:
            return None # Missing State: Round_06


class Round_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[354], delay=700)
        self.spawn_monster(spawn_ids=[355], delay=1400)
        self.spawn_monster(spawn_ids=[362], delay=2100)
        self.spawn_monster(spawn_ids=[361])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_02') == 1:
            return Round_02(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[352], delay=2000)
        self.spawn_monster(spawn_ids=[360], delay=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_03') == 1:
            return Round_03(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[359])
        self.spawn_monster(spawn_ids=[351], delay=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_04') == 1:
            return Round_04(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[353], delay=1000)
        self.spawn_monster(spawn_ids=[358], delay=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Text, script='normal_projectile 종료', duration=1000)
        self.destroy_monster(spawn_ids=[301,302,303,304,305,306,307,308,309,310,311,312,351,352,353,354,355,356,357,358,359,360,361,362])


initial_state = Round_check
