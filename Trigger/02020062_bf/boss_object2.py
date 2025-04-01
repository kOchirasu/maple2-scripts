""" trigger/02020062_bf/boss_object2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101])
        self.set_user_value(trigger_id=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawn_ids=[712,722])
        self.set_interact_object(trigger_ids=[12000112], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 1:
            return 레버2_체크(self.ctx)


class 레버2_체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[722], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[712]):
            return 레버2_발동(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]):
            return 종료(self.ctx)


class 레버2_발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101], visible=True)
        self.set_interact_object(trigger_ids=[12000112], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[12000112], state=0):
            return 레버2_안내(self.ctx)


class 레버2_안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990023, key='MonsterSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=20000):
            return 레버2_재활성(self.ctx)


class 레버2_재활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000112], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[12000112], state=0):
            return 레버2_재활성_대기(self.ctx)


class 레버2_재활성_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=20000):
            return 레버2_재활성(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5101])
        self.set_user_value(trigger_id=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawn_ids=[712,722])
        self.set_interact_object(trigger_ids=[12000112], state=2)


initial_state = 대기
