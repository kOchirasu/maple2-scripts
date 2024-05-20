""" trigger/02000337_bf/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 기본 배치 될 몬스터 등장
        self.set_effect(trigger_ids=[7301])
        self.set_effect(trigger_ids=[7302])
        self.set_effect(trigger_ids=[7303])
        self.set_effect(trigger_ids=[7304])
        self.set_effect(trigger_ids=[7305])
        self.set_effect(trigger_ids=[7310], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return 폭발01(self.ctx)


class 폭발01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7301], visible=True) # 폭발 이펙트
        self.set_skill(trigger_ids=[8301], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=702) >= 1:
            return 폭발02(self.ctx)


class 폭발02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7302], visible=True) # 폭발 이펙트
        self.set_skill(trigger_ids=[8302], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=703) >= 1:
            return 폭발03(self.ctx)


class 폭발03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7303], visible=True) # 폭발 이펙트
        self.set_effect(trigger_ids=[7304], visible=True) # 폭발 이펙트
        self.set_skill(trigger_ids=[8303], enable=True) # 벽 날리는 스킬
        self.set_skill(trigger_ids=[8304], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=704) >= 1:
            return 폭발04(self.ctx)


class 폭발04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7305], visible=True) # 폭발 이펙트
        self.set_skill(trigger_ids=[8305], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=705) >= 1:
            return 폭발04(self.ctx)


initial_state = 시작
