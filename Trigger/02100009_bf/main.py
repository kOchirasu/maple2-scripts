""" trigger/02100009_bf/main.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 타이머설정(self.ctx)


class 타이머설정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=3, minimap_visible=True)
        self.set_portal(portal_id=4, visible=True, enable=True, minimap_visible=True)
        self.set_timer(timer_id='10000', seconds=300, start_delay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[100000001]) and self.monster_dead(spawn_ids=[100000002]):
            return 성공(self.ctx)
        if self.time_expired(timer_id='10000'):
            return 실패(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='10000')


class 성공(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 성공_2(self.ctx)

    def on_exit(self) -> None:
        self.set_event_ui(type=1, arg2='$02100009_BF__text__0$', arg3='4000')


class 성공_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            self.dungeon_clear()
            return 성공_3(self.ctx)

    def on_exit(self) -> None:
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)


class 성공_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[101], skill_id=50000230, level=1, is_player=False, is_skill_set=False)
        self.destroy_monster(spawn_ids=[-1])
        self.set_achievement(trigger_id=9900, type='trigger', achieve='Find02100009')
        self.set_event_ui(type=7, arg2='$02100009_BF__MAIN__1$', arg3='2000', arg4='0')
        self.set_achievement(trigger_id=9900, type='trigger', achieve='02100009_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[101], skill_id=50000230, level=1, is_player=False, is_skill_set=False)
        self.set_event_ui(type=5, arg2='$02100009_BF__MAIN__0$', arg3='2000', arg4='0')
        self.destroy_monster(spawn_ids=[-1])
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 유저감지
