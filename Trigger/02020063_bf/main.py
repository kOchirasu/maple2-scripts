""" trigger/02020063_bf/main.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import BannerType


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032], visible=True)
        self.set_effect(trigger_ids=[10001])
        self.set_effect(trigger_ids=[10002])
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096], visible=True) # <가두기 트리거 메쉬>
        self.set_portal(portal_id=1)
        self.set_portal(portal_id=2)
        self.set_portal(portal_id=3)
        self.enable_spawn_point_pc(spawn_id=0, is_enable=True) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=2)
        self.set_user_value(trigger_id=99990002, key='Battle_1_SpawnStart', value=0)
        self.set_user_value(trigger_id=99990003, key='Battle_2_Start', value=0)
        self.set_user_value(trigger_id=99990004, key='Battle_3_Start', value=0)
        self.set_user_value(trigger_id=99990005, key='Battle_2_SpawnStart', value=0)
        self.set_user_value(trigger_id=99990006, key='Battle_3_SpawnStart', value=0)
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='ks_quest_fusiondevice_A01_off')
        self.reset_timer(timer_id='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]) or self.user_detected(box_ids=[9003]):
            return 유저카운트(self.ctx)


class 유저카운트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=4002, visible=True, initial_sequence='ks_quest_fusiondevice_A01_on')
        self.set_effect(trigger_ids=[10001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='FieldGameStart') == 1:
            # <게임 시작 결정>
            return 딜레이(self.ctx)
        if self.user_value(key='FieldGameStart') == 2:
            # <방폭 결정>
            return 방폭(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9002, type='trigger', achieve='corps_battle')
        self.set_event_ui_script(type=BannerType.Text, script='$02020063_BF__MAIN__0$', duration=5000)
        self.select_camera(trigger_id=998)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 시작(self.ctx)


class 방폭(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui_script(type=BannerType.Text, script='$02020063_BF__MAIN__1$', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 내보내기(self.ctx)


class 내보내기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user()

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032])
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096])
        self.spawn_monster(spawn_ids=[801], auto_target=False) # <무적 오브젝트 생성>
        self.reset_camera(interpolation_time=1.0)
        self.set_event_ui_round(rounds=[1,3])
        self.set_event_ui_script(type=BannerType.Text, script='$02020063_BF__MAIN__2$', duration=5000)
        self.set_user_value(trigger_id=99990002, key='Battle_1_SpawnStart', value=1) # <웨이브 시작>
        # <부활 위치 세팅, 다시 살아날때는 나무에서 살아남>
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=1)
        self.enable_spawn_point_pc(spawn_id=2, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_1_Clear') == 1:
            # <웨이브 종료>
            self.set_user_value(trigger_id=99990002, key='Battle_1_SpawnStart', value=0)
            return 포탑페이즈(self.ctx)
        if self.monster_dead(spawn_ids=[801]):
            self.set_actor(trigger_id=4002, visible=True, initial_sequence='ks_quest_fusiondevice_A01_off')
            self.set_effect(trigger_ids=[10001])
            self.set_effect(trigger_ids=[10002], visible=True)
            return 실패_세팅(self.ctx)


class 포탑페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.give_reward_content(reward_id=31000001)
        self.set_user_value(trigger_id=99990003, key='Battle_2_Start', value=1) # <포탑 생성>
        self.set_user_value(trigger_id=99990005, key='Battle_2_SpawnStart', value=1)
        self.set_event_ui_round(rounds=[2,3])
        self.set_event_ui_script(type=BannerType.Text, script='$02020063_BF__MAIN__3$', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_2_Clear') == 1:
            # <모든 포탑 파괴>
            self.set_user_value(trigger_id=99990005, key='Battle_2_SpawnStart', value=0)
            return 보스페이즈(self.ctx)
        if self.monster_dead(spawn_ids=[801]):
            self.set_actor(trigger_id=4002, visible=True, initial_sequence='ks_quest_fusiondevice_A01_off')
            self.set_effect(trigger_ids=[10001])
            self.set_effect(trigger_ids=[10002], visible=True)
            return 실패_세팅(self.ctx)


class 보스페이즈(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.give_reward_content(reward_id=31000002)
        self.set_event_ui_round(rounds=[3,3])
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020063_BF__MAIN__4$')
        self.set_user_value(trigger_id=99990004, key='Battle_3_Start', value=1)
        self.set_timer(timer_id='1', seconds=180, auto_remove=True, display=True, v_offset=60) # <3라운드 게임 플레이 타임 설정>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Battle_3_Clear') == 1:
            # <보스를 처치했을 경우 성공>
            return 성공_세팅(self.ctx)
        if self.monster_dead(spawn_ids=[801]):
            self.set_actor(trigger_id=4002, visible=True, initial_sequence='ks_quest_fusiondevice_A01_off')
            self.set_effect(trigger_ids=[10001])
            self.set_effect(trigger_ids=[10002], visible=True)
            return 실패_세팅(self.ctx)
        if self.time_expired(timer_id='1'):
            # <시간 내에 클리어하지 못할 경우 실패>
            self.set_actor(trigger_id=4002, visible=True, initial_sequence='ks_quest_fusiondevice_A01_off')
            return 실패_세팅(self.ctx)


class 성공_세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020063_BF__MAIN__5$')
        self.set_user_value(trigger_id=99990002, key='Battle_1_SpawnStart', value=0)
        self.set_user_value(trigger_id=99990003, key='Battle_2_Start', value=0)
        self.set_user_value(trigger_id=99990004, key='Battle_3_Start', value=0)
        self.set_user_value(trigger_id=99990005, key='Battle_2_SpawnStart', value=0)
        self.set_user_value(trigger_id=99990006, key='Battle_3_SpawnStart', value=0)
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 성공_추가대사(self.ctx)


class 성공_추가대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_smile', duration=5000, script='$02020063_BF__MAIN__6$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 성공(self.ctx)


class 실패_세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11001813, illust='Turka_normal', duration=5000, script='$02020063_BF__MAIN__7$')
        self.set_user_value(trigger_id=99990002, key='Battle_1_SpawnStart', value=0)
        self.set_user_value(trigger_id=99990003, key='Battle_2_Start', value=0)
        self.set_user_value(trigger_id=99990004, key='Battle_3_Start', value=0)
        self.set_user_value(trigger_id=99990005, key='Battle_2_SpawnStart', value=0)
        self.set_user_value(trigger_id=99990006, key='Battle_3_SpawnStart', value=0)
        self.reset_timer(timer_id='1')
        self.reset_timer(timer_id='2')
        self.set_mesh(trigger_ids=[4001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 실패(self.ctx)


class 실패_추가대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11003533, illust='Bliche_normal', duration=5000, script='$02020063_BF__MAIN__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 실패(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.field_war_end(is_clear=True)
        self.set_achievement(type='trigger', achieve='FieldwarAchieve_2')

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[-1])
        self.field_war_end()

    def on_tick(self) -> trigger_api.Trigger:
        return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=3, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
