""" trigger/02000486_bf/103_timer.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[900]) or self.monster_in_combat(spawn_ids=[901]):
            return 타이머(self.ctx)


class 타이머(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='999', seconds=240, auto_remove=True, display=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 설명(self.ctx)


class 설명(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000486_BF__103_TIMER__0$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=239000):
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[900]) and self.monster_dead(spawn_ids=[901]):
            return 타이머종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.GameOver, script='$02000486_BF__103_TIMER__1$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


class 타이머종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_timer(timer_id='999')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            pass


initial_state = 전투시작
