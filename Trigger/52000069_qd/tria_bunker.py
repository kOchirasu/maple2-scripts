""" trigger/52000069_qd/tria_bunker.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])
        self.set_effect(trigger_ids=[604])
        self.set_effect(trigger_ids=[605])
        self.set_effect(trigger_ids=[606])
        self.set_effect(trigger_ids=[607])
        self.set_effect(trigger_ids=[608])
        self.set_effect(trigger_ids=[609])
        self.set_effect(trigger_ids=[610])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
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
        self.set_agent(trigger_ids=[8013], visible=True)
        self.set_agent(trigger_ids=[8014], visible=True)
        self.set_agent(trigger_ids=[8015], visible=True)
        self.set_agent(trigger_ids=[8016], visible=True)
        self.set_agent(trigger_ids=[8017], visible=True)
        self.set_agent(trigger_ids=[8018], visible=True)
        self.set_agent(trigger_ids=[8019], visible=True)
        self.set_agent(trigger_ids=[8020], visible=True)
        self.set_agent(trigger_ids=[8021], visible=True)
        self.spawn_monster(spawn_ids=[1000,1001,1002,1003], auto_target=False)
        self.spawn_monster(spawn_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110], auto_target=False)
        self.spawn_monster(spawn_ids=[1201,1202,1203], auto_target=False)
        self.spawn_monster(spawn_ids=[2001,2101,2102,2103,2104,2105,2106,2107,2108], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[199]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_scene_skip(state=연출종료)
            self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.add_cinematic_talk(npc_id=11000064, illust_id='Lennon_normal', msg='$52000069_QD__TRIA_BUNKER__0$', duration=9195, align=Align.Left)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.add_buff(box_ids=[199], skill_id=70000109, level=1, is_player=False, is_skill_set=False) # 초생회
        self.select_camera(trigger_id=301, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003A')
        self.set_dialogue(type=1, spawn_id=1003, script='$52000069_QD__TRIA_BUNKER__1$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 차연출2(self.ctx)


class 차연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=11100101, enable=True, path='BG/Common/Sound/Eff_Object_Devlin_Appear_01.xml ')
        self.set_npc_emotion_sequence(spawn_id=2001, sequence_name='AttackReady_A')
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 프레이대사01(self.ctx)


class 프레이대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=303)
        self.set_npc_emotion_sequence(spawn_id=2003, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11000119, illust_id='Fray_serious', msg='$52000069_QD__TRIA_BUNKER__2$', duration=4000, align=Align.Center)
        self.set_scene_skip(state=대사스킵용01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 돌격(self.ctx)


class 대사스킵용01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return 돌격(self.ctx)


class 돌격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.select_camera(trigger_id=304)
        self.set_agent(trigger_ids=[8004])
        self.set_agent(trigger_ids=[8005])
        self.set_agent(trigger_ids=[8006])
        self.set_agent(trigger_ids=[8007])
        self.set_agent(trigger_ids=[8008])
        self.set_agent(trigger_ids=[8009])
        self.set_agent(trigger_ids=[8010])
        self.set_agent(trigger_ids=[8011])
        self.set_agent(trigger_ids=[8012])
        self.set_agent(trigger_ids=[8013])
        self.set_agent(trigger_ids=[8014])
        self.set_agent(trigger_ids=[8015])
        self.set_agent(trigger_ids=[8016])
        self.set_agent(trigger_ids=[8017])
        self.set_agent(trigger_ids=[8018])
        self.set_agent(trigger_ids=[8019])
        self.set_agent(trigger_ids=[8020])
        self.set_agent(trigger_ids=[8021])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 지원군대기(self.ctx)


class 지원군대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(trigger_id=304, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=20000):
            return 지원군등장(self.ctx)


class 지원군등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1201,1202,1203])
        self.destroy_monster(spawn_ids=[2101,2102,2103])
        self.spawn_monster(spawn_ids=[1004,1005,1301,1302,1303,1304], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 지원군연출(self.ctx)


class 지원군연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, is_player=False, is_skill_set=False)
        self.select_camera(trigger_id=305)
        self.set_dialogue(type=1, spawn_id=1004, script='$52000069_QD__TRIA_BUNKER__3$', time=4)
        self.set_dialogue(type=1, spawn_id=1005, script='$52000069_QD__TRIA_BUNKER__4$', time=4)
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004A')
        self.move_npc(spawn_id=1005, patrol_name='MS2PatrolData_1005A')
        self.move_npc(spawn_id=1301, patrol_name='MS2PatrolData_1301A')
        self.move_npc(spawn_id=1302, patrol_name='MS2PatrolData_1302A')
        self.move_npc(spawn_id=1303, patrol_name='MS2PatrolData_1303A')
        self.move_npc(spawn_id=1304, patrol_name='MS2PatrolData_1304A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 임무종료대기(self.ctx)


class 임무종료대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_buff(box_id=199, skill_id=70000107)
        self.select_camera(trigger_id=305, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 데블린사망딜레이(self.ctx)


class 데블린사망딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return NPC교체(self.ctx)


class NPC교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52000069, portal_id=2)
        self.spawn_monster(spawn_ids=[1006,1007,1009], auto_target=False)
        self.destroy_monster(spawn_ids=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110])
        self.destroy_monster(spawn_ids=[1003,1004,1005,1301,1302,1303,1304,2001,2101,2102,2103,2104,2105,2106,2107,2108])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 에레브연출시작(self.ctx)


class 에레브연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=NPC교체2, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=306)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 에레브대사01(self.ctx)


class 에레브대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawn_id=1000, sequence_name='Talk_A')
        self.set_sound(trigger_id=90000, enable=True) # TriaAttack
        self.set_dialogue(type=2, spawn_id=11000075, script='$52000069_QD__TRIA_BUNKER__5$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 에레브대사02(self.ctx)


class 에레브대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000064, script='$52000069_QD__TRIA_BUNKER__6$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 에레브대사03(self.ctx)


class 에레브대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001975, script='$52000069_QD__TRIA_BUNKER__7$', time=4)
        self.set_onetime_effect(id=1991, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_02_00001991.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에레브대사04(self.ctx)


class 에레브대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=90000) # TriaAttack
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_surprise', msg='$52000069_QD__TRIA_BUNKER__8$', duration=4000, align=Align.Center)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드리아등장(self.ctx)


class 마드리아등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.select_camera(trigger_id=307)
        self.spawn_monster(spawn_ids=[2000], auto_target=False, delay=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 방향전환(self.ctx)


class 방향전환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[609], visible=True)
        self.move_npc(spawn_id=1006, patrol_name='MS2PatrolData_1006A')
        self.move_npc(spawn_id=1007, patrol_name='MS2PatrolData_1007A')
        # self.move_npc(spawn_id=1008, patrol_name='MS2PatrolData_1008A')
        self.move_npc(spawn_id=1009, patrol_name='MS2PatrolData_1009A')
        self.move_user_path(patrol_name='MS2PatrolData_PCA')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 광역마법(self.ctx)


class 광역마법(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.move_npc(spawn_id=2000, patrol_name='MS2PatrolData_2000A')
        self.set_effect(trigger_ids=[609], visible=True)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_effect(trigger_ids=[604], visible=True)
        self.set_effect(trigger_ids=[605], visible=True)
        self.set_effect(trigger_ids=[606], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 처맞음(self.ctx)


class 처맞음(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.set_npc_emotion_sequence(spawn_id=1006, sequence_name='Damg_A')
        self.set_npc_emotion_sequence(spawn_id=1007, sequence_name='Damg_A')
        self.set_npc_emotion_sequence(spawn_id=1009, sequence_name='Damg_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=250):
            return 쓰러짐(self.ctx)


class 쓰러짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1006, sequence_name='Down_Idle_A', duration=1000000000.0)
        self.set_npc_emotion_loop(spawn_id=1007, sequence_name='Down_Idle_A', duration=1000000000.0)
        # self.set_npc_emotion_loop(spawn_id=1008, sequence_name='Down_Idle', duration=1000000000.0)
        self.set_npc_emotion_loop(spawn_id=1009, sequence_name='Dead_Idle_A', duration=1000000000.0)
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=12000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 쓰러짐2(self.ctx)


class 쓰러짐2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1001,1002])
        self.select_camera(trigger_id=309)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마드리아워킹(self.ctx)


class 마드리아워킹(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=308)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마드리아오버숄더(self.ctx)


class 마드리아오버숄더(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000069_QD__TRIA_BUNKER__9$', time=7) # 대사
        self.set_onetime_effect(id=1992, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_03_00001992.xml')
        self.select_camera(trigger_id=310)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 마드리아공격(self.ctx)


class 마드리아공격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11000075, illust_id='Ereb_serious', msg='$52000069_QD__TRIA_BUNKER__10$', duration=3000, align=Align.Center)
        self.select_camera(trigger_id=311)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드리아공격2(self.ctx)


class 마드리아공격2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000069_QD__TRIA_BUNKER__11$', time=12) # 대사
        self.set_onetime_effect(id=1993, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_04_00001993.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12500):
            return 마드리아공격3(self.ctx)


class 마드리아공격3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000069_QD__TRIA_BUNKER__12$', time=11) # 대사
        self.set_onetime_effect(id=1994, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_05_00001994.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=11200):
            return 마드리아공격4(self.ctx)


class 마드리아공격4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000069_QD__TRIA_BUNKER__13$', time=8) # 대사
        self.set_onetime_effect(id=1995, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_06_00001995.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8100):
            return 마드리아공격5(self.ctx)


class 마드리아공격5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=1000, sequence_name='Damg_A')
        self.select_camera(trigger_id=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 에레브각성(self.ctx)


class 에레브각성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[607], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 에레브각성2(self.ctx)


class 에레브각성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1000, sequence_name='Damg_Idle_B', duration=1000000000.0)
        self.select_camera(trigger_id=312)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 마드리아놀람(self.ctx)


class 마드리아놀람(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=314)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 카메라눈속임(self.ctx)


class 카메라눈속임(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=312)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 에레브버프2(self.ctx)


class 에레브버프2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=313)
        self.set_npc_emotion_sequence(spawn_id=1000, sequence_name='Spell_A')
        self.set_onetime_effect(id=2100287, enable=True, path='BG/Common/Sound/Eff_System_Chapter8_Destruction_of_Ereb_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 화이트아웃(self.ctx)


class 화이트아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[608], visible=True)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 마드리아대사01(self.ctx)


class 마드리아대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000069_QD__TRIA_BUNKER__14$', time=7) # 대사
        self.set_onetime_effect(id=1996, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_07_00001996.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 마드리아대사02(self.ctx)


class 마드리아대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001820, script='$52000069_QD__TRIA_BUNKER__15$', time=3) # 대사
        self.set_onetime_effect(id=1997, enable=True, path='BG/Common/Sound/Eff_Madria_TriaSeige_08_00001997.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return NPC교체2(self.ctx)


class NPC교체2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.remove_buff(box_id=199, skill_id=70000109)
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[607])
        self.set_pc_emotion_sequence(sequence_names=['Idle_A'])
        self.destroy_monster(spawn_ids=[1000,1006,1007,1009,2000,1001,1002])
        self.move_user(map_id=52000069, portal_id=2)
        self.spawn_monster(spawn_ids=[1000,1006,1007,1010,1011,1001,1002,9999], auto_target=False)
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_achievement(trigger_id=91000, type='trigger', achieve='TriaSeigeClear')
        self.set_sound(trigger_id=90000, enable=True) # TriaAttack
        self.select_camera(trigger_id=313, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 대기
