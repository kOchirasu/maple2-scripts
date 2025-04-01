""" trigger/02020062_bf/battle_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='ObjectClear', value=0)
        self.set_user_value(trigger_id=99990004, key='ObjectStart', value=0)
        self.set_user_value(trigger_id=99990005, key='ObjectStart', value=0)
        self.set_user_value(trigger_id=99990006, key='ObjectStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 1:
            self.spawn_monster(spawn_ids=[811,812,821,822,831,832], auto_target=False)
            return 오브젝트소환(self.ctx)


class 오브젝트소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[711,712,713], auto_target=False)
        self.set_user_value(trigger_id=99990004, key='ObjectStart', value=1)
        self.set_user_value(trigger_id=99990005, key='ObjectStart', value=1)
        self.set_user_value(trigger_id=99990006, key='ObjectStart', value=1)
        self.set_user_value(trigger_id=99990024, key='MovePanel01', value=1) # 이동 발판 트리거 생성
        self.set_user_value(trigger_id=99990025, key='MovePanel02', value=1) # 이동 발판 트리거 생성
        self.set_user_value(trigger_id=99990026, key='MovePanel03', value=1) # 이동 발판 트리거 생성
        self.set_user_value(trigger_id=99990027, key='MovePanel04', value=1) # 이동 발판 트리거 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 2:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 추가대사_1(self.ctx)


class 추가대사_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020062_BF__BATTLE_2__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 2:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 추가대사_2(self.ctx)


class 추가대사_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02020062_BF__BATTLE_2__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 2:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 추가대사_3(self.ctx)


class 추가대사_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_normal', duration=5000, script='$02020062_BF__BATTLE_2__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 2:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 오브젝트소환_클리어(self.ctx)


class 오브젝트소환_클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='ObjectClear', value=1)
        self.set_user_value(trigger_id=99990004, key='ObjectStart', value=2)
        self.set_user_value(trigger_id=99990005, key='ObjectStart', value=2)
        self.set_user_value(trigger_id=99990006, key='ObjectStart', value=2)


initial_state = 대기
