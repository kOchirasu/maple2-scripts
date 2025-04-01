""" trigger/02000066_bf/oscal.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='randomTalk') == 1:
            self.spawn_monster(spawn_ids=[5003], auto_target=False)
            return 전투대기(self.ctx)


class 전투대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[5003]):
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
        self.set_dialogue(type=1, spawn_id=5003, script='$02000066_BF__OSCAL__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class NPC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=5003, script='$02000066_BF__OSCAL__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class NPC대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=5003, script='$02000066_BF__OSCAL__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class NPC대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=5003, script='$02000066_BF__OSCAL__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 전투대기(self.ctx)


initial_state = 시작
