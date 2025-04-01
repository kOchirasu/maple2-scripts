""" trigger/52010038_qd/gauge.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GaugeOpen') == 1:
            return 게이지시작(self.ctx)


class 게이지시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[700], enable=True)
        self.set_user_value(trigger_id=999002, key='GaugeStart', value=1)
        self.set_user_value(trigger_id=991001, key='GaugeStart', value=1)
        self.set_user_value(trigger_id=991002, key='GaugeStart', value=1)
        self.set_user_value(trigger_id=991003, key='GaugeStart', value=1)
        self.set_user_value(trigger_id=991004, key='GaugeStart', value=1)
        self.shadow_expedition_open_boss_gauge(title='$52010038_QD__gauge__2$', max_gauge_point=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 1000:
            return 성공(self.ctx)
        if self.user_value(key='CoreIsDead') == 1:
            return 실패(self.ctx)
        if self.user_value(key='EngineIsDead') == 1:
            return 실패(self.ctx)

    def on_exit(self) -> None:
        self.shadow_expedition_close_boss_gauge()
        self.set_user_value(trigger_id=991001, key='GaugeClosed', value=1)
        self.set_user_value(trigger_id=991002, key='GaugeClosed', value=1)
        self.set_user_value(trigger_id=991003, key='GaugeClosed', value=1)
        self.set_user_value(trigger_id=991004, key='GaugeClosed', value=1)
        self.set_user_value(trigger_id=999002, key='GaugeClosed', value=1)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_normal', duration=6000, script='$52010038_QD__gauge__3$', voice='ko/Npc/00002107')
        self.set_achievement(trigger_id=199, type='trigger', achieve='skyfortress_takeoff')
        self.set_event_ui_script(type=BannerType.Success, script='$52010038_QD__GAUGE__0$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 정리(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.GameOver, script='$52010038_QD__GAUGE__1$', duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.move_user(map_id=2000092, portal_id=20)
            return 정리(self.ctx)


class 정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_user_value(trigger_id=992001, key='WaveEnd', value=1)
        self.set_user_value(trigger_id=992002, key='WaveEnd', value=1)
        self.set_user_value(trigger_id=993001, key='WoundEnd', value=1)
        self.set_user_value(trigger_id=999004, key='AllertEnd', value=1)
        self.move_user(map_id=52010039, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
