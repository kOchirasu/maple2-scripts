""" trigger/02000066_bf/anos.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[103]):
            return NPC생성(self.ctx)


class NPC생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[98], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 말풍선랜덤(self.ctx)


class 말풍선랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25.0):
            return NPC대사01(self.ctx)
        if self.random_condition(weight=25.0):
            return NPC대사02(self.ctx)
        if self.random_condition(weight=25.0):
            return NPC대사03(self.ctx)
        if self.random_condition(weight=25.0):
            return NPC대사04(self.ctx)


class NPC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=98, script='$02000066_BF__ANOS__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class NPC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=98, script='$02000066_BF__ANOS__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class NPC대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=98, script='$02000066_BF__ANOS__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class NPC대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=98, script='$02000066_BF__ANOS__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


initial_state = 시작
