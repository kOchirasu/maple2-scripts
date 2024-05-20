""" trigger/02100000_bf/timer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=19, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[106]):
            return 타이머시작(self.ctx)


class 타이머시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10000', seconds=360, start_delay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 유저감지_2(self.ctx)


class 유저감지_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[104]):
            return 몬스터등장_보스(self.ctx)


class 몬스터등장_보스(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[82001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 종료선택(self.ctx)


class 종료선택(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[82001]):
            return 성공(self.ctx)
        if self.time_expired(timer_id='10000'):
            return 실패(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='10000')


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.set_achievement(trigger_id=9900, type='trigger', achieve='Find02100000')
        self.set_event_ui(type=7, arg2='$02100000_BF__TIMER__1$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=5, arg2='$02100000_BF__TIMER__0$', arg3='2000', arg4='0')
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=19, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=5, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
