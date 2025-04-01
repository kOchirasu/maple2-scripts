""" trigger/02020027_bf/stun_4.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[1001]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='summon_3_4') == 1:
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11000):
            return 버프_2(self.ctx)


class 버프_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=401, script='$02020027_BF__stun_1__0$', time=3)
        self.set_dialogue(type=1, spawn_id=402, script='$02020027_BF__stun_1__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 버프_4(self.ctx)


class 버프_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=403, script='$02020027_BF__stun_1__2$', time=3)
        self.set_dialogue(type=1, spawn_id=404, script='$02020027_BF__stun_1__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 버프_5(self.ctx)


class 버프_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=405, script='$02020027_BF__stun_1__4$', time=3)
        self.set_dialogue(type=1, spawn_id=406, script='$02020027_BF__stun_1__5$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 버프_제거(self.ctx)


class 버프_제거(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[201], skill_id=62000002, level=1)

    def on_tick(self) -> trigger_api.Trigger:
        pass


initial_state = 시작
