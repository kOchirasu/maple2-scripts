""" trigger/02020063_bf/battle_2.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='Battle_2_Clear', value=0)
        self.start_combine_spawn(group_id=[10000600]) # 거대화 보급 상자
        self.start_combine_spawn(group_id=[10000601])
        self.start_combine_spawn(group_id=[10000602])
        self.set_user_value(trigger_id=99990007, key='TurretSpawn_1', value=0)
        self.set_user_value(trigger_id=99990008, key='TurretSpawn_2', value=0)
        self.set_user_value(trigger_id=99990009, key='TurretSpawn_3', value=0)
        self.set_user_value(trigger_id=99990010, key='TurretSpawn_4', value=0)
        self.set_user_value(trigger_id=99990015, key='TurretSpawn_5', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_Start') == 1:
            return 포탑소환_1(self.ctx)


class 포탑소환_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[10000600], is_start=True) # 상자 소환 1
        self.set_user_value(trigger_id=99990007, key='TurretSpawn_1', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_Start') == 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 추가대사_1(self.ctx)
        if self.monster_dead(spawn_ids=[711]):
            self.set_user_value(trigger_id=99990007, key='TurretSpawn_1', value=0)
            return 포탑소환_2(self.ctx)


class 추가대사_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020063_BF__BATTLE_2__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_Start') == 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 추가대사_2(self.ctx)
        if self.monster_dead(spawn_ids=[711]):
            self.set_user_value(trigger_id=99990007, key='TurretSpawn_1', value=0)
            return 포탑소환_2(self.ctx)


class 추가대사_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02020063_BF__BATTLE_2__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_Start') == 0:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 추가대사_3(self.ctx)
        if self.monster_dead(spawn_ids=[711]):
            self.set_user_value(trigger_id=99990007, key='TurretSpawn_1', value=0)
            return 포탑소환_2(self.ctx)


class 추가대사_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_normal', duration=5000, script='$02020063_BF__BATTLE_2__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 추가대사_4(self.ctx)
        if self.user_value(key='Battle_2_Start') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[711]):
            self.set_user_value(trigger_id=99990007, key='TurretSpawn_1', value=0)
            return 포탑소환_2(self.ctx)


class 추가대사_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020063_BF__BATTLE_2__3$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_Start') == 0:
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[711]):
            return 포탑소환_2(self.ctx)


class 포탑소환_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02020063_BF__BATTLE_2__4$')
        self.set_user_value(trigger_id=99990008, key='TurretSpawn_2', value=1)
        self.set_user_value(trigger_id=99990009, key='TurretSpawn_3', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[712,713]):
            return 포탑소환_3(self.ctx)
        if self.user_value(key='Battle_2_Start') == 0:
            return 대기(self.ctx)


class 포탑소환_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02020063_BF__BATTLE_2__5$')
        self.set_user_value(trigger_id=99990010, key='TurretSpawn_4', value=1)
        self.set_user_value(trigger_id=99990015, key='TurretSpawn_5', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[714,715]):
            return 종료대기(self.ctx)
        if self.user_value(key='Battle_2_Start') == 0:
            return 대기(self.ctx)


class 종료대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_smile', duration=5000, script='$02020063_BF__BATTLE_2__6$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 포탑소환_클리어(self.ctx)
        if self.user_value(key='Battle_2_Start') == 0:
            return 대기(self.ctx)


class 포탑소환_클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='Battle_2_Clear', value=1)
        self.set_user_value(trigger_id=99990005, key='Battle_2_SpawnStart', value=0)
        self.start_combine_spawn(group_id=[10000600])
        self.set_user_value(trigger_id=99990007, key='TurretSpawn_1', value=0)
        self.set_user_value(trigger_id=99990008, key='TurretSpawn_2', value=0)
        self.set_user_value(trigger_id=99990009, key='TurretSpawn_3', value=0)
        self.set_user_value(trigger_id=99990010, key='TurretSpawn_4', value=0)
        self.set_user_value(trigger_id=99990015, key='TurretSpawn_5', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_Start') == 0:
            return 대기(self.ctx)


initial_state = 대기
