""" trigger/51000003_dg/normal_projectile_02.xml """
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
        self.destroy_monster(spawn_ids=[351,352])
        self.spawn_monster(spawn_ids=[302], delay=1000)
        self.spawn_monster(spawn_ids=[303], delay=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_02') == 1:
            return Round_02(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[353,354])
        self.spawn_monster(spawn_ids=[304], delay=500)
        self.spawn_monster(spawn_ids=[305], delay=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_03') == 1:
            return Round_03(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[355,356])
        self.spawn_monster(spawn_ids=[306], delay=1000)
        self.spawn_monster(spawn_ids=[301], delay=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_04') == 1:
            return Round_04(self.ctx)
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class Round_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[312], delay=500)
        self.spawn_monster(spawn_ids=[311], delay=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reset') == 1:
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Text, script='normal_projectile_02 종료', duration=1000)
        self.destroy_monster(spawn_ids=[301,302,303,304,305,306,307,308,309,310,311,312,351,352,353,354,355,356,357,358,359,360,361,362])


initial_state = Round_check
