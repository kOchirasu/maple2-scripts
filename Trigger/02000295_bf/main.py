""" trigger/02000295_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[3000])
        self.set_ladder(trigger_ids=[3001])
        self.set_ladder(trigger_ids=[3002])
        self.set_ladder(trigger_ids=[3003])
        self.set_ladder(trigger_ids=[3004])
        self.destroy_monster(spawn_ids=[910,911,912,913,914,915,916,917])
        self.spawn_monster(spawn_ids=[4100], auto_target=False) # BossActor
        self.destroy_monster(spawn_ids=[4101]) # BossBattle
        self.spawn_monster(spawn_ids=[900,901,902]) # MobEnterance
        self.spawn_monster(spawn_ids=[800,801,802,803,804]) # LuminaBattle
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331]) # SlaveNpc
        self.set_agent(trigger_ids=[8000], visible=True)
        self.set_agent(trigger_ids=[8001], visible=True)
        self.set_agent(trigger_ids=[8002], visible=True)
        self.set_agent(trigger_ids=[8003], visible=True)
        self.set_agent(trigger_ids=[8004], visible=True)
        self.set_agent(trigger_ids=[8005], visible=True)
        self.set_agent(trigger_ids=[8006], visible=True)
        self.set_agent(trigger_ids=[8007], visible=True)
        self.set_agent(trigger_ids=[8008], visible=True)
        self.set_agent(trigger_ids=[8009], visible=True)
        self.set_agent(trigger_ids=[8010], visible=True)
        self.set_agent(trigger_ids=[8011], visible=True)
        self.set_agent(trigger_ids=[8012], visible=True)
        self.set_effect(trigger_ids=[5000]) # TargetGuide
        self.set_effect(trigger_ids=[5001]) # TargetGuide
        self.set_effect(trigger_ids=[5002]) # TargetGuide
        self.set_effect(trigger_ids=[5100]) # Wheel
        self.set_effect(trigger_ids=[5101]) # MetalDoorOpen
        self.set_effect(trigger_ids=[5102]) # MetalDoorClose
        self.set_effect(trigger_ids=[5103]) # BossAct
        self.set_breakable(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129]) # Jail_Mid
        self.set_breakable(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229]) # Jail_Under
        self.set_visible_breakable_object(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129]) # Jail_Mid
        self.set_visible_breakable_object(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229]) # Jail_Under
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[95001,95002,95003,95004,95005,95006], visible=True) # Stairs
        # InvisibleEnteranceBarrier
        self.set_mesh(trigger_ids=[2000], visible=True)
        # InvisibleJailBlock_alwaysON
        self.set_mesh(trigger_ids=[2001,2002], visible=True)
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045]) # Deck01_ClearOn
        self.set_mesh(trigger_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246]) # Deck02_ClearOn
        self.set_mesh(trigger_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159], visible=True) # Jail
        self.set_user_value(key='LuminaArmyJoin', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcMonologue01(self.ctx)


# 연출 시작
class NpcMonologue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[201], auto_target=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_201')
        self.set_skip(state=CameraWalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NpcMonologue02(self.ctx)


class NpcMonologue02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=1, spawn_id=201, script='$02000295_BF__MAIN__0$', time=3)
        self.set_skip(state=CameraWalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return CameraWalk01(self.ctx)


# 철창 안 노예 말풍선 연출
class CameraWalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601)
        self.set_skip(state=CameraWalk02)
        self.add_balloon_talk(spawn_id=301, msg='$02000295_BF__MAIN__1$', duration=3000, delay_tick=2000) # Right
        self.add_balloon_talk(spawn_id=310, msg='$02000295_BF__MAIN__2$', duration=3000, delay_tick=2000) # Right
        self.add_balloon_talk(spawn_id=318, msg='$02000295_BF__MAIN__3$', duration=3000, delay_tick=3000) # Right
        self.add_balloon_talk(spawn_id=316, msg='$02000295_BF__MAIN__4$', duration=3000, delay_tick=3000) # Right
        self.add_balloon_talk(spawn_id=307, msg='$02000295_BF__MAIN__5$', duration=3000, delay_tick=4000) # Right
        self.add_balloon_talk(spawn_id=312, msg='$02000295_BF__MAIN__6$', duration=3000, delay_tick=4000) # Right
        self.add_balloon_talk(spawn_id=305, msg='$02000295_BF__MAIN__7$', duration=3000, delay_tick=5000) # Right
        self.add_balloon_talk(spawn_id=314, msg='$02000295_BF__MAIN__8$', duration=3000, delay_tick=5000) # Right
        self.add_balloon_talk(spawn_id=325, msg='$02000295_BF__MAIN__9$', duration=3000, delay_tick=2000) # Left
        self.add_balloon_talk(spawn_id=323, msg='$02000295_BF__MAIN__10$', duration=3000, delay_tick=2000) # Left
        self.add_balloon_talk(spawn_id=323, msg='$02000295_BF__MAIN__11$', duration=3000, delay_tick=3000) # Left
        self.add_balloon_talk(spawn_id=327, msg='$02000295_BF__MAIN__12$', duration=3000, delay_tick=4000) # Left
        self.add_balloon_talk(spawn_id=330, msg='$02000295_BF__MAIN__13$', duration=3000, delay_tick=5000) # Left

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return CameraWalk02(self.ctx)


class CameraWalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=601, enable=False)
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return CameraWalk03(self.ctx)


class CameraWalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_ladder(trigger_ids=[3000], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[3001], visible=True, enable=True, fade=12)
        # InvisibleEnteranceBarrier
        self.set_mesh(trigger_ids=[2000])
        self.select_camera(trigger_id=600)
        self.set_skip(state=CameraWalk05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CameraWalk04(self.ctx)


class CameraWalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=1, spawn_id=202, script='$02000295_BF__MAIN__14$', time=3, arg5=1)
        self.set_skip(state=CameraWalk05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return CameraWalk05(self.ctx)


class CameraWalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_202')
        self.set_dialogue(type=1, spawn_id=202, script='$02000295_BF__MAIN__15$', time=5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=600, enable=False)
        self.play_system_sound_in_box(box_ids=[9000], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002952, text_id=20002952, duration=3000) # 투기장 안으로 이동하세요.
        self.set_effect(trigger_ids=[5000], visible=True) # TargetGuide
        self.set_effect(trigger_ids=[5001], visible=True) # TargetGuide
        self.set_effect(trigger_ids=[5002], visible=True) # TargetGuide

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9001]):
            return BattleReady01(self.ctx)


# 연출 종료
class BattleReady01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(box_ids=[9000], sound='System_ShowGuideSummary_01')
        # 투기장의 포악한 야수들이 몰려옵니다. 모두 처치하세요.
        self.show_guide_summary(entity_id=20002951, text_id=20002951, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 트리거01웨이브(self.ctx)


class 트리거01웨이브(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # TargetGuide
        self.set_effect(trigger_ids=[5001]) # TargetGuide
        self.set_effect(trigger_ids=[5002]) # TargetGuide
        self.set_mesh(trigger_ids=[95001,95002,95003,95004,95005,95006], fade=2.0) # Stairs
        self.spawn_monster(spawn_ids=[910,911])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 트리거02웨이브(self.ctx)


class 트리거02웨이브(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[912,913])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 트리거03웨이브(self.ctx)


class 트리거03웨이브(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[914,915])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 트리거04웨이브(self.ctx)


class 트리거04웨이브(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[916,917])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[910,911,912,913,914,915,916,917]):
            return BossAct01(self.ctx)


class BossAct01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BossAct02(self.ctx)


class BossAct02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=603)
        self.set_effect(trigger_ids=[5103], visible=True) # BossAct
        self.set_skip(state=BossAct03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return BossAct03(self.ctx)


class BossAct03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=603, enable=False)
        self.set_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BossBattle01(self.ctx)


# 보스 전투 돌입
class BossBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[4100]) # BossActor
        self.spawn_monster(spawn_ids=[4101]) # BossBattle

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LuminaArmyJoin') == 1:
            return BossBattle02(self.ctx)
        if self.monster_dead(spawn_ids=[4101]):
            return BossBattle02(self.ctx)


# 보스 체력 30% 루미나 해방군 전투 합류
class BossBattle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8000])
        self.set_agent(trigger_ids=[8001])
        self.set_agent(trigger_ids=[8002])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.destroy_monster(spawn_ids=[900,901,902])
        self.change_monster(from_spawn_id=800, to_spawn_id=810)
        self.change_monster(from_spawn_id=801, to_spawn_id=811)
        self.change_monster(from_spawn_id=802, to_spawn_id=812)
        self.change_monster(from_spawn_id=803, to_spawn_id=813)
        self.change_monster(from_spawn_id=804, to_spawn_id=814)
        self.change_monster(from_spawn_id=202, to_spawn_id=203)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BossBattle03(self.ctx)


class BossBattle03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=810, patrol_name='MS2PatrolData_800')
        self.move_npc(spawn_id=811, patrol_name='MS2PatrolData_801')
        self.move_npc(spawn_id=812, patrol_name='MS2PatrolData_802')
        self.move_npc(spawn_id=813, patrol_name='MS2PatrolData_803')
        self.move_npc(spawn_id=814, patrol_name='MS2PatrolData_804')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_203')
        self.set_dialogue(type=1, spawn_id=203, script='$02000295_BF__MAIN__16$', time=3, arg5=3)
        self.set_dialogue(type=1, spawn_id=203, script='$02000295_BF__MAIN__17$', time=4, arg5=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[4101]):
            return BattleEnd01(self.ctx)


class BattleEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[8003])
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_mesh(trigger_ids=[95001,95002,95003,95004,95005,95006], visible=True, fade=2.0) # Stairs
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_204')
        self.set_dialogue(type=1, spawn_id=203, script='$02000295_BF__MAIN__18$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return BattleEnd02(self.ctx)


class BattleEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return BattleEnd03(self.ctx)


class BattleEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2000295, portal_id=3, box_id=9000) # 반경 150 영역

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return ReleaseSlaves01(self.ctx)


class ReleaseSlaves01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=602)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReleaseSlaves02(self.ctx)


class ReleaseSlaves02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045], visible=True, fade=2.0) # Deck01_ClearOn
        self.set_mesh(trigger_ids=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246], visible=True, start_delay=200, interval=30, fade=2.0) # Deck02_ClearOn
        self.set_effect(trigger_ids=[5100], visible=True) # Wheel
        self.set_effect(trigger_ids=[5101], visible=True) # MetalDoorOpen

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return ReleaseSlaves03(self.ctx)


class ReleaseSlaves03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,1122,1123,1124,1125,1126,1127,1128,1129,1130,1131,1132,1133,1134,1135,1136,1137,1138,1139,1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,1156,1157,1158,1159], start_delay=100) # Jail
        self.set_breakable(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], enable=True) # Jail_Mid
        self.set_breakable(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], enable=True) # Jail_Under
        self.set_visible_breakable_object(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129], visible=True) # Jail_Mid
        self.set_visible_breakable_object(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229], visible=True) # Jail_Under
        self.change_monster(from_spawn_id=301, to_spawn_id=401)
        self.change_monster(from_spawn_id=302, to_spawn_id=402)
        self.change_monster(from_spawn_id=303, to_spawn_id=403)
        self.change_monster(from_spawn_id=304, to_spawn_id=404)
        self.change_monster(from_spawn_id=305, to_spawn_id=405)
        self.change_monster(from_spawn_id=306, to_spawn_id=406)
        self.change_monster(from_spawn_id=307, to_spawn_id=407)
        self.change_monster(from_spawn_id=308, to_spawn_id=408)
        self.change_monster(from_spawn_id=309, to_spawn_id=409)
        self.change_monster(from_spawn_id=310, to_spawn_id=410)
        self.change_monster(from_spawn_id=311, to_spawn_id=411)
        self.change_monster(from_spawn_id=312, to_spawn_id=412)
        self.change_monster(from_spawn_id=313, to_spawn_id=413)
        self.change_monster(from_spawn_id=314, to_spawn_id=414)
        self.change_monster(from_spawn_id=315, to_spawn_id=415)
        self.change_monster(from_spawn_id=316, to_spawn_id=416)
        self.change_monster(from_spawn_id=317, to_spawn_id=417)
        self.change_monster(from_spawn_id=318, to_spawn_id=418)
        self.change_monster(from_spawn_id=320, to_spawn_id=420)
        self.change_monster(from_spawn_id=321, to_spawn_id=421)
        self.change_monster(from_spawn_id=322, to_spawn_id=422)
        self.change_monster(from_spawn_id=323, to_spawn_id=423)
        self.change_monster(from_spawn_id=324, to_spawn_id=424)
        self.change_monster(from_spawn_id=325, to_spawn_id=425)
        self.change_monster(from_spawn_id=326, to_spawn_id=426)
        self.change_monster(from_spawn_id=327, to_spawn_id=427)
        self.change_monster(from_spawn_id=328, to_spawn_id=428)
        self.change_monster(from_spawn_id=329, to_spawn_id=429)
        self.change_monster(from_spawn_id=330, to_spawn_id=430)
        self.change_monster(from_spawn_id=331, to_spawn_id=431)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return ReleaseSlaves04(self.ctx)


class ReleaseSlaves04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5102], visible=True) # MetalDoorClose
        self.set_effect(trigger_ids=[5100]) # Wheel
        self.move_npc(spawn_id=401, patrol_name='MS2PatrolData_301')
        self.move_npc(spawn_id=402, patrol_name='MS2PatrolData_302')
        self.move_npc(spawn_id=403, patrol_name='MS2PatrolData_303')
        self.move_npc(spawn_id=404, patrol_name='MS2PatrolData_304')
        self.move_npc(spawn_id=405, patrol_name='MS2PatrolData_305')
        self.move_npc(spawn_id=406, patrol_name='MS2PatrolData_306')
        self.move_npc(spawn_id=407, patrol_name='MS2PatrolData_307')
        self.move_npc(spawn_id=408, patrol_name='MS2PatrolData_308')
        self.move_npc(spawn_id=409, patrol_name='MS2PatrolData_309')
        self.move_npc(spawn_id=410, patrol_name='MS2PatrolData_310')
        self.move_npc(spawn_id=411, patrol_name='MS2PatrolData_311')
        self.move_npc(spawn_id=412, patrol_name='MS2PatrolData_312')
        self.move_npc(spawn_id=413, patrol_name='MS2PatrolData_313')
        self.move_npc(spawn_id=414, patrol_name='MS2PatrolData_314')
        self.move_npc(spawn_id=415, patrol_name='MS2PatrolData_315')
        self.move_npc(spawn_id=416, patrol_name='MS2PatrolData_316')
        self.move_npc(spawn_id=417, patrol_name='MS2PatrolData_317')
        self.move_npc(spawn_id=418, patrol_name='MS2PatrolData_318')
        self.move_npc(spawn_id=420, patrol_name='MS2PatrolData_320')
        self.move_npc(spawn_id=421, patrol_name='MS2PatrolData_321')
        self.move_npc(spawn_id=422, patrol_name='MS2PatrolData_322')
        self.move_npc(spawn_id=423, patrol_name='MS2PatrolData_323')
        self.move_npc(spawn_id=424, patrol_name='MS2PatrolData_324')
        self.move_npc(spawn_id=425, patrol_name='MS2PatrolData_325')
        self.move_npc(spawn_id=426, patrol_name='MS2PatrolData_326')
        self.move_npc(spawn_id=427, patrol_name='MS2PatrolData_327')
        self.move_npc(spawn_id=428, patrol_name='MS2PatrolData_328')
        self.move_npc(spawn_id=429, patrol_name='MS2PatrolData_329')
        self.move_npc(spawn_id=430, patrol_name='MS2PatrolData_330')
        self.move_npc(spawn_id=431, patrol_name='MS2PatrolData_331')
        self.set_dialogue(type=1, spawn_id=402, script='$02000295_BF__MAIN__19$', time=2) # Right
        self.set_dialogue(type=1, spawn_id=410, script='$02000295_BF__MAIN__20$', time=3) # Right
        self.set_dialogue(type=1, spawn_id=418, script='$02000295_BF__MAIN__21$', time=3, arg5=1) # Right
        self.set_dialogue(type=1, spawn_id=416, script='$02000295_BF__MAIN__22$', time=2, arg5=2) # Right
        self.set_dialogue(type=1, spawn_id=407, script='$02000295_BF__MAIN__23$', time=3, arg5=2) # Right
        self.set_dialogue(type=1, spawn_id=412, script='$02000295_BF__MAIN__24$', time=3, arg5=3) # Right
        self.set_dialogue(type=1, spawn_id=405, script='$02000295_BF__MAIN__25$', time=3, arg5=3) # Right
        self.set_dialogue(type=1, spawn_id=414, script='$02000295_BF__MAIN__26$', time=3, arg5=3) # Right
        self.set_dialogue(type=1, spawn_id=425, script='$02000295_BF__MAIN__27$', time=2) # Left
        self.set_dialogue(type=1, spawn_id=421, script='$02000295_BF__MAIN__28$', time=3, arg5=1) # Left
        self.set_dialogue(type=1, spawn_id=424, script='$02000295_BF__MAIN__29$', time=3, arg5=2) # Left
        self.set_dialogue(type=1, spawn_id=427, script='$02000295_BF__MAIN__30$', time=3, arg5=2) # Left
        self.set_dialogue(type=1, spawn_id=430, script='$02000295_BF__MAIN__31$', time=3, arg5=3) # Left
        self.set_skip(state=ReleaseSlaves05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return ReleaseSlaves05(self.ctx)


class ReleaseSlaves05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.spawn_monster(spawn_ids=[200])
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_199')
        self.select_camera(trigger_id=602, enable=False)
        self.select_camera(trigger_id=603)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return ToBeContinued01(self.ctx)


class ToBeContinued01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000006, script='$02000295_BF__MAIN__32$', time=4)
        self.set_skip(state=Quit01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Quit01(self.ctx)


class Quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.remove_balloon_talk(spawn_id=200)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=603, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit02(self.ctx)


class Quit02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9000, type='trigger', achieve='ReleaseTheSlaves')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit03(self.ctx)


class Quit03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9000, type='trigger', achieve='ClearKatramusfirst')
        self.set_ladder(trigger_ids=[3002], visible=True, enable=True, fade=10)
        self.set_ladder(trigger_ids=[3003], visible=True, enable=True, fade=12)
        self.set_ladder(trigger_ids=[3004], visible=True, enable=True, fade=14)
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)
        self.dungeon_clear()


initial_state = 대기
