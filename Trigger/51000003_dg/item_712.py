""" trigger/51000003_dg/item_712.xml """
import trigger_api


# 포그 이펙트
class Spawn_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7712])
        self.set_effect(trigger_ids=[7722])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='item_712_spawn') == 1:
            return SpawnItem(self.ctx)


class SpawnItem(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7712], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[722]):
            # 플레이어가 닿으면 획득
            return GetItem_Random(self.ctx)
        if self.user_value(key='item_712_spawn') == 0:
            return Spawn_check(self.ctx)


class Disable(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991117, key='item_712_spawn', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Spawn_check(self.ctx)


class GetItem_Random(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='random_buff_box') # 큐브 안에 뭐가 들었을까? (트로피)
        self.set_effect(trigger_ids=[7712])
        self.set_effect(trigger_ids=[7722], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return Buff_01(self.ctx)
        if self.random_condition(weight=1.0):
            return Buff_02(self.ctx)
        if self.random_condition(weight=1.0):
            return Buff_03(self.ctx)
        if self.random_condition(weight=10.0):
            return Buff_04(self.ctx)
        if self.random_condition(weight=1.0):
            return Buff_05(self.ctx)


class Buff_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=70000080, level=1, is_skill_set=False) # 이속증가

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=991117, key='item_712_spawn', value=0)


class Buff_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=70000081, level=1, is_skill_set=False) # 이속감소

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=991117, key='item_712_spawn', value=0)


class Buff_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=70000082, level=1, is_skill_set=False) # 키 커짐

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=991117, key='item_712_spawn', value=0)


class Buff_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=70000083, level=1, is_skill_set=False) # 키 작아짐

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=991117, key='item_712_spawn', value=0)


class Buff_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[701], skill_id=70000085, level=1, is_skill_set=False) # 무적

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Spawn_check(self.ctx)

    def on_exit(self) -> None:
        self.set_user_value(trigger_id=991117, key='item_712_spawn', value=0)


initial_state = Spawn_check
