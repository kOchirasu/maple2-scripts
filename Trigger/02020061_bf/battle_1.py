""" trigger/02020061_bf/battle_1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=99990001, key='GaugeClear', value=0)
        self.start_combine_spawn(group_id=[478])
        self.start_combine_spawn(group_id=[479])
        self.start_combine_spawn(group_id=[480])
        self.start_combine_spawn(group_id=[481])
        self.set_onetime_effect(id=1, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart') == 1:
            return 스폰_1_SE(self.ctx)


# 시작
class 스폰_1_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[478], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 스폰_1(self.ctx)


class 스폰_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__BATTLE_1__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 200:
            return 스폰_2_SE(self.ctx)
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return None # Missing State: 스폰_1_추가대사


class 스폰_1_추가대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_nomal', duration=5000, script='$02020061_BF__BATTLE_1__1$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 스폰_1_추가대사2(self.ctx)


class 스폰_1_추가대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003536, illust='Neirin_surprise', duration=5000, script='$02020061_BF__BATTLE_1__2$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 200:
            return 스폰_2_SE(self.ctx)
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)


class 스폰_2_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_2(self.ctx)


class 스폰_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[479], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 400:
            return 스폰_3_SE(self.ctx)
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)


class 스폰_3_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_3(self.ctx)


class 스폰_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[480], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 600:
            return 스폰_4_SE(self.ctx)
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)


class 스폰_4_SE(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)
        if self.wait_tick(wait_tick=2000):
            return 스폰_4(self.ctx)


class 스폰_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')
        self.start_combine_spawn(group_id=[481], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_points() >= 800:
            return 오브젝트페이즈(self.ctx)
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)


class 오브젝트페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.shadow_expedition_close_boss_gauge()
        self.start_combine_spawn(group_id=[478])
        self.start_combine_spawn(group_id=[479])
        self.start_combine_spawn(group_id=[480])
        self.start_combine_spawn(group_id=[481])
        self.set_user_value(trigger_id=99990001, key='GaugeClear', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SpawnStart') == 2:
            return 대기(self.ctx)


initial_state = 대기
