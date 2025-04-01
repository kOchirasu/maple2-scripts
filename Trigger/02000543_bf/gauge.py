""" trigger/02000543_bf/gauge.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GaugeOpen') == 1:
            return 게이지시작(self.ctx)


class 게이지시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition_open_boss_gauge(title='$02000543_BF__GAUGE__0$', max_gauge_point=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 1000:
            return 성공(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition_close_boss_gauge()
        self.destroy_monster(spawn_ids=[-1])
        self.set_user_value(trigger_id=2001, key='WaveEnd', value=1)
        self.set_user_value(trigger_id=2003, key='WaveEnd', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
