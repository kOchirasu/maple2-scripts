""" trigger/02020063_bf/battle_3.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='Battle_3_Clear', value=0)
        self.start_combine_spawn(group_id=[10000600])
        self.start_combine_spawn(group_id=[10000604])
        self.set_user_value(trigger_id=99990011, key='Battle3_TurretSpawn_1', value=0)
        self.set_user_value(trigger_id=99990012, key='Battle3_TurretSpawn_2', value=0)
        self.set_user_value(trigger_id=99990013, key='Battle3_TurretSpawn_3', value=0)
        self.set_user_value(trigger_id=99990014, key='Battle3_TurretSpawn_4', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start') == 1:
            return 보스_추가대사(self.ctx)


class 보스_추가대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.set_event_ui_script(type=BannerType.Text, script='$02020063_BF__BATTLE_3__0$', duration=5000)
            return 보스소환(self.ctx)


class 보스소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[921], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]):
            return 보스군단_클리어(self.ctx)
        if self.user_value(key='ObjectStart') == 2 and self.npc_detected(box_id=9099, spawn_ids=[921]):
            return 보스_무적페이즈(self.ctx)


class 보스_무적페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020063_BF__BATTLE_3__1$', duration=5000)
        self.set_user_value(trigger_id=99990011, key='Battle3_TurretSpawn_1', value=1)
        self.set_user_value(trigger_id=99990012, key='Battle3_TurretSpawn_2', value=1)
        self.set_user_value(trigger_id=99990013, key='Battle3_TurretSpawn_3', value=1)
        self.set_user_value(trigger_id=99990014, key='Battle3_TurretSpawn_4', value=1)
        # self.set_user_value(trigger_id=99990006, key='Battle_3_SpawnStart', value=1)
        self.start_combine_spawn(group_id=[10000600], is_start=True)
        self.start_combine_spawn(group_id=[10000604], is_start=True)
        self.set_user_value(trigger_id=99990006, key='Battle_3_SpawnStart', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]):
            return 보스군단_클리어(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 보스_추가대사1(self.ctx)


class 보스_추가대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02020063_BF__BATTLE_3__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]):
            return 보스군단_클리어(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 보스_추가대사2(self.ctx)


class 보스_추가대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_normal', duration=5000, script='$02020063_BF__BATTLE_3__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Start') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[921]):
            return 보스군단_클리어(self.ctx)


class 보스군단_클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='Battle_3_Clear', value=1)
        self.set_user_value(trigger_id=99990006, key='Battle_3_SpawnStart', value=0)
        self.start_combine_spawn(group_id=[10000600])
        self.start_combine_spawn(group_id=[10000604])
        self.set_user_value(trigger_id=99990011, key='Battle3_TurretSpawn_1', value=0)
        self.set_user_value(trigger_id=99990012, key='Battle3_TurretSpawn_2', value=0)
        self.set_user_value(trigger_id=99990013, key='Battle3_TurretSpawn_3', value=0)
        self.set_user_value(trigger_id=99990014, key='Battle3_TurretSpawn_4', value=0)


initial_state = 대기
