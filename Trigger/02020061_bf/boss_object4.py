""" trigger/02020061_bf/boss_object4.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5301])
        self.set_user_value(trigger_id=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawn_ids=[714,724])
        self.set_interact_object(trigger_ids=[12000097], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 1:
            return 레버4_체크(self.ctx)


class 레버4_체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[724], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[714]):
            return 레버4_발동(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]) and self.monster_dead(spawn_ids=[924]) and self.monster_dead(spawn_ids=[925]) and self.monster_dead(spawn_ids=[926]):
            return 종료(self.ctx)


class 레버4_발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5301], visible=True)
        self.set_interact_object(trigger_ids=[12000097], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]) and self.monster_dead(spawn_ids=[924]) and self.monster_dead(spawn_ids=[925]) and self.monster_dead(spawn_ids=[926]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[12000097], state=0):
            return 레버4_안내(self.ctx)


class 레버4_안내(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990023, key='MonsterSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]) and self.monster_dead(spawn_ids=[924]) and self.monster_dead(spawn_ids=[925]) and self.monster_dead(spawn_ids=[926]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 레버4_재활성(self.ctx)


class 레버4_재활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000097], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]) and self.monster_dead(spawn_ids=[924]) and self.monster_dead(spawn_ids=[925]) and self.monster_dead(spawn_ids=[926]):
            return 종료(self.ctx)
        if self.object_interacted(interact_ids=[12000097], state=0):
            return 레버4_재활성_대기(self.ctx)


class 레버4_재활성_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BossObjectStart') == 2:
            return 종료(self.ctx)
        if self.monster_dead(spawn_ids=[921]) and self.monster_dead(spawn_ids=[922]) and self.monster_dead(spawn_ids=[923]) and self.monster_dead(spawn_ids=[924]) and self.monster_dead(spawn_ids=[925]) and self.monster_dead(spawn_ids=[926]):
            return 종료(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 레버4_재활성(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5301])
        self.set_user_value(trigger_id=99990023, key='MonsterSpawn', value=0)
        self.destroy_monster(spawn_ids=[714,724])
        self.set_interact_object(trigger_ids=[12000097], state=2)


initial_state = 대기
