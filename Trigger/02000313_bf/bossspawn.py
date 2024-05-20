""" trigger/02000313_bf/bossspawn.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)
        self.set_portal(portal_id=12)
        self.set_portal(portal_id=13)
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])
        self.set_ladder(trigger_ids=[4001])
        self.set_ladder(trigger_ids=[4002])
        self.set_ladder(trigger_ids=[4003])
        self.set_ladder(trigger_ids=[4004])
        self.set_ladder(trigger_ids=[4005])
        self.set_ladder(trigger_ids=[4006])
        self.set_ladder(trigger_ids=[4007])
        self.set_ladder(trigger_ids=[4008])
        self.set_ladder(trigger_ids=[4101])
        self.set_ladder(trigger_ids=[4102])
        self.set_ladder(trigger_ids=[4103])
        self.set_ladder(trigger_ids=[4104])
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015])
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158])
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235])
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325])
        self.spawn_monster(spawn_ids=[1099], auto_target=False)
        self.spawn_monster(spawn_ids=[1101,1102,1103,1104,1105,1106,1107,1108], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[15]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015], visible=True)
        self.spawn_monster(spawn_ids=[1001], auto_target=False)
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.select_camera(trigger_id=30000)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=차전투시작1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 차전투시작1(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=30000, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 차전투시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20031300, text_id=20031300, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 차전투시작2_1(self.ctx)


class 차전투시작2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20031301, text_id=20031301, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 차NPC이동1(self.ctx)


class 차NPC이동1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=10101, spawn_ids=[1001]):
            self.destroy_monster(spawn_ids=[1001])
            self.spawn_monster(spawn_ids=[1002], auto_target=False)
            return 차전투대기2(self.ctx)


class 차전투대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20031302, text_id=20031302, duration=4000)
        self.spawn_monster(spawn_ids=[2002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10102]):
            return 차전투딜레이2(self.ctx)
        if self.monster_in_combat(spawn_ids=[2002]):
            return 차전투딜레이2(self.ctx)


class 차전투딜레이2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차전투시작2(self.ctx)


class 차전투시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1002])
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.set_ladder(trigger_ids=[4001], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4002], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4003], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4004], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4005], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4006], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4007], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4008], visible=True, enable=True)
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132,3133,3134,3135,3136,3137,3138,3139,3140,3141,3142,3143,3144,3145,3146,3147,3148,3149,3150,3151,3152,3153,3154,3155,3156,3157,3158], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2002]):
            return 차NPC이동2(self.ctx)


class 차NPC이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=10104, spawn_ids=[1003]):
            self.destroy_monster(spawn_ids=[1003])
            self.spawn_monster(spawn_ids=[1004], auto_target=False)
            return 차전투대기3(self.ctx)


class 차전투대기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2003], auto_target=False)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20031302, text_id=20031302, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10103]):
            return 차전투딜레이3(self.ctx)
        if self.monster_in_combat(spawn_ids=[2003]):
            return 차전투딜레이3(self.ctx)


class 차전투딜레이3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차전투시작3(self.ctx)


class 차전투시작3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1004])
        self.spawn_monster(spawn_ids=[1005], auto_target=False)
        self.set_ladder(trigger_ids=[4101], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4102], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4103], visible=True, enable=True)
        self.set_ladder(trigger_ids=[4104], visible=True, enable=True)
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2003]):
            return 보스등장연출(self.ctx)


class 보스등장연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=30001)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 보스등장연출2(self.ctx)


class 보스등장연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1099])
        self.destroy_monster(spawn_ids=[1005])
        self.spawn_monster(spawn_ids=[2099], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 보스등장연출3(self.ctx)


class 보스등장연출3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1101, sequence_name='Dead_A', duration=9000.0)
        self.set_npc_emotion_loop(spawn_id=1102, sequence_name='Dead_A', duration=9000.0)
        self.set_npc_emotion_loop(spawn_id=1103, sequence_name='Dead_A', duration=9000.0)
        self.set_npc_emotion_loop(spawn_id=1104, sequence_name='Dead_A', duration=9000.0)
        self.set_npc_emotion_loop(spawn_id=1105, sequence_name='Dead_A', duration=9000.0)
        self.set_npc_emotion_loop(spawn_id=1106, sequence_name='Dead_A', duration=9000.0)
        self.set_npc_emotion_loop(spawn_id=1107, sequence_name='Dead_A', duration=9000.0)
        self.set_npc_emotion_loop(spawn_id=1108, sequence_name='Dead_A', duration=9000.0)
        self.set_mesh(trigger_ids=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319,3320,3321,3322,3323,3324,3325], visible=True)
        self.set_skip(state=보스전투시작)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스전투시작(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(trigger_id=30001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[1101,1102,1103,1104,1105,1106,1107,1108])
        self.set_npc_emotion_loop(spawn_id=1005, sequence_name='Dead_Idle_A', duration=10000000000000000.0)
        self.set_effect(trigger_ids=[5002])


class 보스전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20031303, text_id=20031303, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 보스전투시작2(self.ctx)


class 보스전투시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20031304, text_id=20031304, duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2099]):
            return 퀘스트체크(self.ctx)


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 종료(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트코드확인(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=12, visible=True, enable=True, minimap_visible=True)
        self.set_portal(portal_id=13, visible=True, enable=True, minimap_visible=True)


class 퀘스트코드확인(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_effect(trigger_ids=[5001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9997], quest_ids=[10003105], quest_states=[2]):
            return 퀘스트연출_시작(self.ctx)
        if self.quest_user_detected(box_ids=[9998], quest_ids=[10003105], quest_states=[2]):
            return 퀘스트연출_시작(self.ctx)
        if self.quest_user_detected(box_ids=[9999], quest_ids=[10003105], quest_states=[2]):
            return 퀘스트연출_시작(self.ctx)


class 퀘스트연출_시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=9, script='$02000313_BF__BOSSSPAWN__43$')
        self.spawn_monster(spawn_ids=[205]) # 바야르
        self.spawn_monster(spawn_ids=[202]) # 무파사
        self.spawn_monster(spawn_ids=[203]) # 구르는천둥
        self.spawn_monster(spawn_ids=[204]) # 시끄러운 주먹
        self.move_user(map_id=2000313, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 퀘스트연출_상황보여주기_01(self.ctx)


class 퀘스트연출_상황보여주기_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=퀘스트연출끝_이동, action='exit')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=30000)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=0, msg='$02000313_BF__BOSSSPAWN__44$', duration=3000)
        self.add_cinematic_talk(npc_id=11003392, msg='$02000313_BF__BOSSSPAWN__45$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=205, sequence_name='Stun_A', duration=160000000.0)
        self.set_npc_emotion_loop(spawn_id=203, sequence_name='Attack_Idle_A', duration=160000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트연출_상황보여주기_02(self.ctx)


class 퀘스트연출_상황보여주기_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Bore_A')
        self.face_emotion(spawn_id=203, emotion_name='Trigger_Sad')
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__46$', duration=3000)
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__47$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트연출_상황보여주기_03(self.ctx)


class 퀘스트연출_상황보여주기_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.set_npc_emotion_loop(spawn_id=203, sequence_name='Attack_Idle_A', duration=1000000000.0)
        self.set_npc_emotion_sequence(spawn_id=204, sequence_name='Talk_A,Bore_B')
        self.set_effect(trigger_ids=[5001])
        self.add_cinematic_talk(npc_id=11003454, msg='$02000313_BF__BOSSSPAWN__48$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퀘스트연출_상황보여주기_04_1(self.ctx)


class 퀘스트연출_상황보여주기_04_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=203, emotion_name='Trigger_Danger')
        self.add_cinematic_talk(npc_id=11003387, msg='$02000313_BF__BOSSSPAWN__49$', duration=3000)
        self.add_cinematic_talk(npc_id=11003387, msg='$02000313_BF__BOSSSPAWN__50$', duration=3000)
        self.add_cinematic_talk(npc_id=11003454, msg='$02000313_BF__BOSSSPAWN__51$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 퀘스트연출_상황보여주기_04_2(self.ctx)


class 퀘스트연출_상황보여주기_04_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.set_pc_emotion_sequence(sequence_names=['Talk_A'])
        self.add_cinematic_talk(npc_id=0, msg='$02000313_BF__BOSSSPAWN__52$', duration=3000)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__53$', duration=3000)
        self.spawn_monster(spawn_ids=[201]) # 붉은늑대심장
        self.add_balloon_talk(msg='$02000313_BF__BOSSSPAWN__54$', duration=2000, delay_tick=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트연출_상황보여주기_04(self.ctx)


class 퀘스트연출_상황보여주기_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=201, emotion_name='Talk')
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Idle_A', duration=1000000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 퀘스트연출_상황보여주기_05(self.ctx)


class 퀘스트연출_상황보여주기_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_9991')
        self.add_cinematic_talk(npc_id=11003387, msg='$02000313_BF__BOSSSPAWN__55$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퀘스트연출_상황보여주기_06(self.ctx)


class 퀘스트연출_상황보여주기_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Idle_A', duration=1000000000.0)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__56$', duration=3000)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__57$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트연출_상황보여주기_07(self.ctx)


class 퀘스트연출_상황보여주기_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.add_cinematic_talk(npc_id=11003387, msg='$02000313_BF__BOSSSPAWN__58$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퀘스트연출_상황보여주기_08(self.ctx)


class 퀘스트연출_상황보여주기_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4018], return_view=False)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Idle_A', duration=1000000000.0)
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Bore_A')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_9994')
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__15$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퀘스트연출_상황보여주기_09(self.ctx)


class 퀘스트연출_상황보여주기_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Attack_Idle_A', duration=1000000000.0)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__59$', duration=3000)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__60$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트연출_상황보여주기_10(self.ctx)


class 퀘스트연출_상황보여주기_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_9995')
        self.add_cinematic_talk(npc_id=11003387, msg='$02000313_BF__BOSSSPAWN__61$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$02000313_BF__BOSSSPAWN__62$', duration=3000)
        self.set_npc_emotion_sequence(spawn_id=204, sequence_name='Talk_A')
        self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Attack_01_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트연출_상황보여주기_10_1(self.ctx)


class 퀘스트연출_상황보여주기_10_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013], return_view=False)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__63$', duration=3000)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__64$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Attack_Idle_A', duration=1000000000.0)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__65$', duration=3000)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__66$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$02000313_BF__BOSSSPAWN__67$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 퀘스트연출_상황보여주기_11(self.ctx)


class 퀘스트연출_상황보여주기_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='ChatUp_A')
        self.face_emotion(spawn_id=201, emotion_name='Trigger_Proud')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_9996')
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__68$', duration=4000)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__69$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 퀘스트연출_상황보여주기_11_1(self.ctx)


class 퀘스트연출_상황보여주기_11_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.add_cinematic_talk(npc_id=11003387, msg='$02000313_BF__BOSSSPAWN__70$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=203, sequence_name='Sit_Down_A', duration=10000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퀘스트연출_상황보여주기_11_2(self.ctx)


class 퀘스트연출_상황보여주기_11_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4018], return_view=False)
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__71$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퀘스트연출_상황보여주기_11_3(self.ctx)


class 퀘스트연출_상황보여주기_11_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Bore_A')
        self.face_emotion(spawn_id=201, emotion_name='Trigger_Sad')
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__72$', duration=3000)
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__73$', duration=3000)
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__74$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 퀘스트연출_상황보여주기_11_4_1(self.ctx)


class 퀘스트연출_상황보여주기_11_4_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=201, emotion_name='Trigger_Proud')
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__75$', duration=6060)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6060):
            return 퀘스트연출_상황보여주기_11_4(self.ctx)


class 퀘스트연출_상황보여주기_11_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4019], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Attack_01_A')
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__76$', duration=4000)
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__77$', duration=4000)
        self.set_skip(state=퀘스트연출_마지막전투_04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 퀘스트연출_상황보여주기_12(self.ctx)


class 퀘스트연출_상황보여주기_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4014], return_view=False)
        self.add_cinematic_talk(npc_id=11003387, msg='$02000313_BF__BOSSSPAWN__78$', duration=3000)
        self.face_emotion(spawn_id=203, emotion_name='Trigger_Embarrassed')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 퀘스트연출_상황보여주기_13(self.ctx)


class 퀘스트연출_상황보여주기_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4018], return_view=False)
        self.visible_my_pc(is_visible=False)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_A')
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Attack_01_C')
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__79$', duration=3000)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__80$', duration=3000)
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__81$', duration=3000)
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.destroy_monster(spawn_ids=[203]) # 구르는천둥
        self.destroy_monster(spawn_ids=[204]) # 시끄러운 주먹

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 퀘스트연출_마지막전투_01(self.ctx)


class 퀘스트연출_마지막전투_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4020], return_view=False)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Attack_04_G')
        self.add_cinematic_talk(npc_id=11003392, msg='$02000313_BF__BOSSSPAWN__82$', duration=1500)
        self.set_effect(trigger_ids=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 퀘스트연출_마지막전투_02(self.ctx)


class 퀘스트연출_마지막전투_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4017], return_view=False)
        self.visible_my_pc(is_visible=False)
        self.add_cinematic_talk(npc_id=11003393, msg='$02000313_BF__BOSSSPAWN__83$', duration=3000)
        self.add_cinematic_talk(npc_id=11003407, msg='$02000313_BF__BOSSSPAWN__84$', duration=3000)
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Attack_02_H')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 퀘스트연출_마지막전투_03(self.ctx)


class 퀘스트연출_마지막전투_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_9993')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_9992')
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Attack_04_G')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트연출_마지막전투_03_1(self.ctx)


class 퀘스트연출_마지막전투_03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4017], return_view=False)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Dead_A')
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Attack_01_B')
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_effect(trigger_ids=[5005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 퀘스트연출_마지막전투_04(self.ctx)


class 퀘스트연출_마지막전투_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawn_ids=[201])
        self.destroy_monster(spawn_ids=[202])
        self.destroy_monster(spawn_ids=[205])
        self.spawn_monster(spawn_ids=[206])
        self.spawn_monster(spawn_ids=[207])
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_npc_emotion_loop(spawn_id=206, sequence_name='Dead_A', duration=1000000.0)
        self.set_npc_emotion_loop(spawn_id=207, sequence_name='Dead_B', duration=1000000.0)
        self.face_emotion(spawn_id=206, emotion_name='Trigger_Dead')
        self.face_emotion(spawn_id=207, emotion_name='Trigger_Dead')
        self.set_effect(trigger_ids=[5006], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 퀘스트연출_마지막전투_05(self.ctx)


class 퀘스트연출_마지막전투_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_onetime_effect(id=3, enable=True, path='BG\\weather\\Eff_monochrome_03.xml')
        self.select_camera_path(path_ids=[4021,4022], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트연출_마지막전투_06(self.ctx)


class 퀘스트연출_마지막전투_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_onetime_effect(id=3, path='BG\\weather\\Eff_monochrome_03.xml')
        self.set_cinematic_ui(type=9, script='$02000313_BF__BOSSSPAWN__85$')
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 퀘스트연출_마지막전투_07(self.ctx)


class 퀘스트연출_마지막전투_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=9, script='$02000313_BF__BOSSSPAWN__86$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 퀘스트연출_마지막전투_08(self.ctx)


class 퀘스트연출_마지막전투_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트연출끝_이동(self.ctx)


class 퀘스트연출끝_이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=52010032, portal_id=3)


initial_state = 시작대기중
