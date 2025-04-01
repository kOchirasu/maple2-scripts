""" trigger/02020061_bf/battle_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='ObjectClear', value=0)
        self.set_user_value(trigger_id=99990004, key='ObjectStart', value=0)
        self.set_user_value(trigger_id=99990005, key='ObjectStart', value=0)
        self.set_user_value(trigger_id=99990006, key='ObjectStart', value=0)
        self.set_user_value(trigger_id=99990007, key='ObjectStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 1:
            return 오브젝트소환(self.ctx)


class 오브젝트소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[711,712,713,714], auto_target=False)
        self.set_user_value(trigger_id=99990004, key='ObjectStart', value=1)
        self.set_user_value(trigger_id=99990005, key='ObjectStart', value=1)
        self.set_user_value(trigger_id=99990006, key='ObjectStart', value=1)
        self.set_user_value(trigger_id=99990007, key='ObjectStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 2:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 오브젝트소환_클리어(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 대사용_1(self.ctx)


class 대사용_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__BATTLE_2__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 2:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 오브젝트소환_클리어(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 대사용_2(self.ctx)


class 대사용_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02020061_BF__BATTLE_2__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 2:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 오브젝트소환_클리어(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 대사용_3(self.ctx)


class 대사용_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_normal', duration=5000, script='$02020061_BF__BATTLE_2__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectPhase') == 2:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[701]):
            return 오브젝트소환_클리어(self.ctx)


class 오브젝트소환_클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='ObjectClear', value=1)
        self.set_user_value(trigger_id=99990004, key='ObjectStart', value=0)
        self.set_user_value(trigger_id=99990005, key='ObjectStart', value=0)
        self.set_user_value(trigger_id=99990006, key='ObjectStart', value=0)
        self.set_user_value(trigger_id=99990007, key='ObjectStart', value=0)


initial_state = 대기
