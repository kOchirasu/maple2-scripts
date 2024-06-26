""" trigger/99999950/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 시작대기(self.ctx)


class 시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.set_event_ui_script(type=BannerType.GameOver, script='$99999950__MAIN__0$', duration=2000, box_ids='0')
            return 라운드1(self.ctx)


class 라운드1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101001]):
            return 라운드02_1(self.ctx)


class 라운드02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101001]):
            return 라운드대기2(self.ctx)


class 라운드대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.set_event_ui_script(type=BannerType.GameOver, script='$99999950__MAIN__1$', duration=2000, box_ids='0')
            return 라운드2(self.ctx)


class 라운드2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101002]):
            return 라운드02_2(self.ctx)


class 라운드02_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101002]):
            return 라운드대기3(self.ctx)


class 라운드대기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.set_event_ui_script(type=BannerType.GameOver, script='$99999950__MAIN__2$', duration=2000, box_ids='0')
            return 라운드3(self.ctx)


class 라운드3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101003]):
            return 라운드02_3(self.ctx)


class 라운드02_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101003])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101003]):
            return 라운드대기4(self.ctx)


class 라운드대기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.set_event_ui_script(type=BannerType.GameOver, script='$99999950__MAIN__3$', duration=2000, box_ids='0')
            return 라운드4(self.ctx)


class 라운드4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101004]):
            return 라운드02_4(self.ctx)


class 라운드02_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101004]):
            return 라운드03_4(self.ctx)


class 라운드03_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101004]):
            return 라운드대기5(self.ctx)


class 라운드대기5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            self.set_event_ui_script(type=BannerType.GameOver, script='$99999950__MAIN__4$', duration=2000, box_ids='0')
            return 라운드5(self.ctx)


class 라운드5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101005]):
            return None # Missing State: 라운드대기6


initial_state = 대기
