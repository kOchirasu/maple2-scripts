""" trigger/99999911/main.xml """
import trigger_api


# 플레이어 감지
class 최초(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return 시작조건체크(self.ctx)


class 시작조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 어나운스0(self.ctx)
        if self.count_users(box_id=701) >= 20:
            return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999911__MAIN__0$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$61000004_ME__TRIGGER_01__1$', count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            self.set_mesh(trigger_ids=[301,302,303], start_delay=12)
            self.set_achievement(trigger_id=101, type='trigger', achieve='dailyquest_start')
            return idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], delay=1)
        self.spawn_monster(spawn_ids=[102], delay=2)
        self.spawn_monster(spawn_ids=[103], delay=3)
        self.spawn_monster(spawn_ids=[104], delay=4)
        self.spawn_monster(spawn_ids=[105], delay=5)
        self.spawn_monster(spawn_ids=[106], delay=6)
        self.spawn_monster(spawn_ids=[107], delay=7)
        self.spawn_monster(spawn_ids=[108])
        self.spawn_monster(spawn_ids=[301], delay=1)
        self.spawn_monster(spawn_ids=[302], delay=2)
        self.spawn_monster(spawn_ids=[303], delay=3)
        self.spawn_monster(spawn_ids=[304])
        self.spawn_monster(spawn_ids=[305], delay=1)
        self.spawn_monster(spawn_ids=[306], delay=2)
        self.spawn_monster(spawn_ids=[307], delay=3)
        self.spawn_monster(spawn_ids=[308])
        self.spawn_monster(spawn_ids=[309], delay=1)
        self.spawn_monster(spawn_ids=[310], delay=2)
        self.spawn_monster(spawn_ids=[311], delay=3)
        self.spawn_monster(spawn_ids=[312])
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Round1_Start(self.ctx)


class Round1_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991104, key='Round_02', value=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return None # Missing State: random_start


initial_state = 최초
