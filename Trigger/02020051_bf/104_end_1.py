""" trigger/02020051_bf/104_end_1.xml """
import trigger_api


class 사망조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End') == 1:
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=103, key='Main', value=2)
        self.set_user_value(trigger_id=107, key='Text', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 준비_2(self.ctx)


class 준비_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', script='$02020051_BF__104_END_1__0$', duration=5684, voice='ko/Npc/00002201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 몬스터사망_1(self.ctx)


class 몬스터사망_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_is_dead_by_string_id(string_id='Gigantika_01') or self.user_value(key='End') == 3:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=102, key='Timmer', value=3)
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 종료_2(self.ctx)


class 종료_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=103, key='Main', value=2)
        self.set_user_value(trigger_id=102, key='Timmer', value=2)
        self.set_user_value(trigger_id=102, key='Timmer', value=3)
        self.set_user_value(trigger_id=101, key='Potion', value=2)
        self.set_user_value(trigger_id=105, key='Summon_monster', value=2)
        self.set_user_value(trigger_id=106, key='Summon_monster_2', value=2)
        self.set_user_value(trigger_id=107, key='Text', value=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End') == 2:
            return 사망조건(self.ctx)


initial_state = 사망조건
