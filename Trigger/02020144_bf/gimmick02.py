""" trigger/02020144_bf/gimmick02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Plant') == 1:
            return 몬스터소환(self.ctx)
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[301,302,303,304], auto_target=False) # 21430006 네펜투스

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=1000):
            return 힌트(self.ctx)


class 힌트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui_script(type=BannerType.Text, script='$02020101_BF__GIMMICK2__0$', duration=3000)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=4000):
            return 알림(self.ctx)


class 알림(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=25000):
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[301,302,303,304]):
            # self.set_user_value(trigger_id=900009, key='Seed', value=1)
            self.set_user_value(trigger_id=900004, key='Plant', value=0)
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[301,302,303,304], arg2=False)
        self.set_user_value(trigger_id=900004, key='Plant', value=0)
        # self.set_user_value(trigger_id=900009, key='Seed', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기(self.ctx)


initial_state = 대기
