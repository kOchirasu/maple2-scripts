""" trigger/02100009_bf/text.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 알림(self.ctx)


class 알림(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=100000001, is_relative=True) <= 5 or self.npc_hp(spawn_id=100000002, is_relative=True) <= 5:
            return 알림_2(self.ctx)
        if self.monster_dead(spawn_ids=[100000001]) and self.monster_dead(spawn_ids=[100000002]):
            return 완료알림(self.ctx)

    def on_exit(self) -> None:
        self.reset_timer(timer_id='10000')


class 알림_2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 알림_3(self.ctx)

    def on_exit(self) -> None:
        self.set_event_ui(type=1, arg2='$02100009_BF__resurrection_2__0$', arg3='4000')


class 알림_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 알림(self.ctx)
        if self.monster_dead(spawn_ids=[100000001]) and self.monster_dead(spawn_ids=[100000002]):
            return 완료알림(self.ctx)


class 완료알림(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            pass


initial_state = 유저감지
