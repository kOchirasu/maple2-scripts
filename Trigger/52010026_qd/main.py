""" trigger/52010026_qd/main.xml """
import trigger_api
from System.Numerics import Vector3
from Maple2.Server.Game.Scripting.Trigger import Align


"""
치유의 숲 : 52010026
들어오자마자 앉아있는 상태 연출
"""
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False)
        self.set_effect(trigger_ids=[201])
        self.set_effect(trigger_ids=[221])
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])
        self.set_effect(trigger_ids=[5101])
        self.set_effect(trigger_ids=[5201])
        self.set_sound(trigger_id=7001, enable=True)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=7, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=8, path='BG\\Common\\ScreenMask\\Eff_FlickEye.nif')
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=201, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=202, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=301, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=997, path='BG/sound/Eff_BossRegen_01.xml')
        self.set_onetime_effect(id=998, path='BG/sound/Eff_DevilPortal_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2001]):
            return black(self.ctx)


class black(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52010026, portal_id=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.select_camera_path(path_ids=[4001], return_view=False) # PC 정면 샷
        self.spawn_monster(spawn_ids=[1001], auto_target=False) # 조디
        self.spawn_monster(spawn_ids=[601,602,603], auto_target=False) # 연출용 엔피씨 (상인)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작_깨어난PC(self.ctx)


class 연출시작_깨어난PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_loop(sequence_name='Sit_Ground_Idle_A', duration=29000.0)
        self.face_emotion(emotion_name='Trigger_disappoint')
        self.set_scene_skip(state=두번째연출_ready, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작_PC대사01(self.ctx)


class 연출시작_PC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(emotion_name='Trigger_disappoint')
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__0$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 연출시작_조디대사01(self.ctx)


class 연출시작_조디대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.face_emotion(spawn_id=1001, emotion_name='Trigger_Talk_A')
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__2$', duration=3000)
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__3$', duration=3000)
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 첫번째연출_PC대사02(self.ctx)


class 첫번째연출_PC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.face_emotion(emotion_name='Trigger_panic')
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__5$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 첫번째연출_조디대사02(self.ctx)


class 첫번째연출_조디대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=1001, emotion_name='Trigger_Talk03_A')
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__7$', duration=3000)
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__8$', duration=3000)
        self.face_emotion(spawn_id=1001, emotion_name='Trigger_Talk02_A')
        self.add_cinematic_talk(npc_id=11003344, illust_id='Peach_normal', msg='$52010026_QD__MAIN__9$', duration=3000, align=Align.Right)
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__10$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 첫번째연출_PC대사03(self.ctx)


class 첫번째연출_PC대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(emotion_name='Trigger_serious')
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 첫번째연출_조디대사03(self.ctx)


class 첫번째연출_조디대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=1001, emotion_name='Trigger_Talk01_A')
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__12$', duration=3000)
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__13$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 첫번째연출_PC대사04(self.ctx)


class 첫번째연출_PC대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.face_emotion(emotion_name='Trigger_serious')
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__14$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 조디_카메라01(self.ctx)


class 조디_카메라01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 첫번째연출_조디대사04(self.ctx)


class 첫번째연출_조디대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False)
        self.face_emotion(spawn_id=1001, emotion_name='Trigger_Idle02_A')
        self.set_npc_emotion_loop(spawn_id=1001, sequence_name='Trigger_Idle_A', duration=10000.0)
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__15$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 첫번째연출_조디대사05(self.ctx)


class 첫번째연출_조디대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4003], return_view=False)
        self.set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__16$', duration=3000)
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 첫번째연출_PC대사05(self.ctx)

    def on_exit(self) -> None:
        self.visible_my_pc(is_visible=True)


class 첫번째연출_PC대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001], return_view=False)
        self.face_emotion(emotion_name='Trigger_serious')
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__18$', duration=3000)
        self.set_npc_emotion_loop(spawn_id=1001, sequence_name='Trigger_Idle_A', duration=10000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 조디_카메라02(self.ctx)


class 조디_카메라02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 첫번째연출_조디대사06(self.ctx)


class 첫번째연출_조디대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.face_emotion(spawn_id=1001, emotion_name='Idle_A')
        self.set_pc_emotion_loop(sequence_name='Idle_A', duration=1000.0)
        self.add_cinematic_talk(npc_id=11003344, msg='$52010026_QD__MAIN__19$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__20$', duration=3000)
        self.set_event_ui(type=1, arg2='$52010026_QD__MAIN__21$', arg3='8000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 두번째연출_ready(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_sound(trigger_id=7001)
        self.set_scene_skip() # Missing State: State


class 두번째연출_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=True)
        self.set_pc_emotion_loop(sequence_name='Sit_Ground_Idle_A', duration=100.0)
        self.reset_camera(interpolation_time=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[2101]):
            return 두번째연출_black(self.ctx)


class 두번째연출_black(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4501], return_view=False)
        self.spawn_monster(spawn_ids=[1000], auto_target=False, delay=30000)
        self.set_effect(trigger_ids=[5001], visible=True)
        self.set_effect(trigger_ids=[5002], visible=True)
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        self.spawn_monster(spawn_ids=[102], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=1000, sequence_name='Down_Idle_A', duration=70000.0)
        self.set_scene_skip(state=두번째연출_피치전투01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째연출_피치발견01(self.ctx)


class 두번째연출_피치발견01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=201, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003343, msg='$52010026_QD__MAIN__22$', duration=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째연출_피치발견02(self.ctx)


class 두번째연출_피치발견02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=201, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_balloon_talk(msg='$52010026_QD__MAIN__47$', duration=1000)
        self.select_camera_path(path_ids=[4501,4502], return_view=False)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째연출_피치전투01(self.ctx)


class 두번째연출_피치전투01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_balloon_talk(spawn_id=1000, msg='$52010026_QD__MAIN__24$', duration=1000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010026_QD__MAIN__25$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 두번째연출_피치전투02(self.ctx)


class 두번째연출_피치전투02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102]):
            return 두번째연출_딜레이01(self.ctx)


class 두번째연출_딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5001])
        self.set_effect(trigger_ids=[5002])
        self.add_balloon_talk(spawn_id=1000, msg='$52010026_QD__MAIN__26$', duration=2000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 두번째연출_피치전투03(self.ctx)


class 두번째연출_피치전투03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=1000, msg='$52010026_QD__MAIN__27$', duration=2000)
        self.set_onetime_effect(id=202, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(trigger_ids=[5003], visible=True)
        self.set_effect(trigger_ids=[5004], visible=True)
        self.set_effect(trigger_ids=[5005], visible=True)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.spawn_monster(spawn_ids=[105], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[103,104,105]):
            return 두번째연출_딜레이02(self.ctx)


class 두번째연출_딜레이02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=202, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(trigger_ids=[5003])
        self.set_effect(trigger_ids=[5004])
        self.set_effect(trigger_ids=[5005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 두번째연출_PC대사01(self.ctx)


class 두번째연출_PC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__28$', duration=3000)
        self.set_scene_skip(state=Skip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 두번째연출_잠시쉬기(self.ctx)


class Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=4)
        self.spawn_monster(spawn_ids=[111], auto_target=False, delay=6000)
        self.spawn_monster(spawn_ids=[112], auto_target=False, delay=6000)
        self.spawn_monster(spawn_ids=[113], auto_target=False, delay=6000)
        self.spawn_monster(spawn_ids=[114], auto_target=False, delay=6000)
        self.spawn_monster(spawn_ids=[115], auto_target=False, delay=6000)
        self.spawn_monster(spawn_ids=[121], auto_target=False, delay=5000)
        self.spawn_monster(spawn_ids=[122], auto_target=False, delay=5000)
        self.spawn_monster(spawn_ids=[123], auto_target=False, delay=5000)
        self.spawn_monster(spawn_ids=[124], auto_target=False, delay=5000)
        self.spawn_monster(spawn_ids=[125], auto_target=False, delay=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 세번째연출_대사01(self.ctx)


class 두번째연출_잠시쉬기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003343, illust_id='Peach_normal', align=Align.Left, msg='$52010026_QD__MAIN__29$', duration=2000)
        self.add_cinematic_talk(npc_id=11003343, msg='$52010026_QD__MAIN__30$', duration=2000)
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__48$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 세번째연출_포털개방(self.ctx)


class 세번째연출_포털개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4201], return_view=False)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=101, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_ambient_light(primary=Vector3(128,128,128))
        self.set_effect(trigger_ids=[201], visible=True)
        self.set_onetime_effect(id=998, enable=True, path='BG/sound/Eff_DevilPortal_01.xml')
        self.spawn_monster(spawn_ids=[111], auto_target=False, delay=6000)
        self.spawn_monster(spawn_ids=[112], auto_target=False, delay=6000)
        self.spawn_monster(spawn_ids=[113], auto_target=False, delay=6000)
        self.spawn_monster(spawn_ids=[114], auto_target=False, delay=6000)
        self.spawn_monster(spawn_ids=[115], auto_target=False, delay=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세번째연출_포털개방02(self.ctx)


class 세번째연출_포털개방02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4301], return_view=False)
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(trigger_ids=[211], visible=True)
        self.spawn_monster(spawn_ids=[121], auto_target=False, delay=5000)
        self.spawn_monster(spawn_ids=[122], auto_target=False, delay=5000)
        self.spawn_monster(spawn_ids=[123], auto_target=False, delay=5000)
        self.spawn_monster(spawn_ids=[124], auto_target=False, delay=5000)
        self.spawn_monster(spawn_ids=[125], auto_target=False, delay=5000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 세번째연출_대사01(self.ctx)


class 세번째연출_대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=102, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_balloon_talk(msg='$52010026_QD__MAIN__32$', duration=2000)
        self.set_npc_emotion_sequence(spawn_id=1000, sequence_name='ChatUP_A')
        self.add_balloon_talk(spawn_id=1000, msg='$52010026_QD__MAIN__33$', duration=2000, delay_tick=2000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010026_QD__MAIN__34$', arg3='2000', arg4='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 피치탈출(self.ctx)


class 피치탈출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1000, patrol_name='MS2PatrolData_3002')
        self.add_balloon_talk(spawn_id=1000, msg='$52010026_QD__MAIN__42$', duration=2000)
        self.add_buff(box_ids=[2101], skill_id=70000123, level=1, is_player=False, is_skill_set=False)
        self.set_effect(trigger_ids=[5101], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,112,113,114,115,121,122,123,124,125]):
            return 세번째연출_대사02(self.ctx)


class 세번째연출_대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[201])
        self.set_effect(trigger_ids=[221])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=998, path='BG/sound/Eff_DevilPortal_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 세번째연출_대사02_1(self.ctx)


class 세번째연출_대사02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=skip_a, action='nextState')
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__35$', duration=2000)
        self.add_cinematic_talk(npc_id=11003343, msg='$52010026_QD__MAIN__36$', duration=2000)
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__49$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 다섯번째연출_ready(self.ctx)


class 다섯번째연출_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4402], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다섯번째연출_엘리트몬스터(self.ctx)


class skip_a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State
        self.spawn_monster(spawn_ids=[131])
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 다섯번째연출_엘리트몬스터대사(self.ctx)


class 다섯번째연출_엘리트몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=1000, sequence_name='Trigger_Hurt_A', duration=28000.0)
        self.select_camera_path(path_ids=[4401], return_view=False)
        self.set_onetime_effect(id=7, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(map_id=52010026, portal_id=6002)
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=997, enable=True, path='BG/sound/Eff_BossRegen_01.xml')
        self.spawn_monster(spawn_ids=[131])
        self.show_caption(scale=2.3, type='NameCaption', title='$52010026_QD__MAIN__50$', desc='$52010026_QD__MAIN__51$', align=Align.Center | Align.Left, offset_rate_x=-0.15, duration=4000)
        self.set_onetime_effect(id=103, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 다섯번째연출_엘리트몬스터대사(self.ctx)


class 다섯번째연출_엘리트몬스터대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010026_QD__MAIN__38$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 다섯번째연출_전투(self.ctx)


class 다섯번째연출_전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=997, path='BG/sound/Eff_BossRegen_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[131]):
            return 다섯번째연출_마지막(self.ctx)


class 다섯번째연출_마지막(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Warp, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 다섯번째연출_대화02(self.ctx)


class 다섯번째연출_대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.face_emotion(emotion_name='Trigger_disappoint')
        self.set_pc_emotion_loop(sequence_name='Down_B', duration=18000.0)
        self.set_onetime_effect(id=6, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(trigger_ids=[5201], visible=True)
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__43$', duration=3000)
        self.add_cinematic_talk(npc_id=0, msg='$52010026_QD__MAIN__44$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 다섯번째연출_암전(self.ctx)


class 다섯번째연출_암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 다섯번째연출_의문의목소리암전(self.ctx)


class 다섯번째연출_의문의목소리암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003145, msg='$52010026_QD__MAIN__45$', duration=3000)
        self.add_cinematic_talk(npc_id=11003145, msg='$52010026_QD__MAIN__46$', duration=3000)
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return Warp(self.ctx)


class Warp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=63000042, portal_id=10)


initial_state = idle
