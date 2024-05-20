""" trigger/52000108_qd/52000108.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[2001])
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 아이샤등장
        self.set_effect(trigger_ids=[5000]) # 경로 안내
        self.set_effect(trigger_ids=[5001]) # 경로 안내
        self.set_effect(trigger_ids=[5002]) # 경로 안내
        self.set_effect(trigger_ids=[5003]) # 경로 안내
        self.set_effect(trigger_ids=[5004]) # 경로 안내
        self.set_effect(trigger_ids=[5005]) # 경로 안내
        self.set_effect(trigger_ids=[5006]) # 경로 안내
        self.set_effect(trigger_ids=[5007]) # 경로 안내
        self.set_effect(trigger_ids=[5008]) # 경로 안내
        self.set_effect(trigger_ids=[5009]) # 경로 안내
        self.set_effect(trigger_ids=[5010]) # 경로 안내
        self.set_effect(trigger_ids=[5011]) # 경로 안내
        self.set_effect(trigger_ids=[5012]) # 경로 안내
        self.set_effect(trigger_ids=[5013]) # 경로 안내
        self.set_effect(trigger_ids=[5014]) # 경로 안내
        self.set_effect(trigger_ids=[5015]) # 경로 안내
        self.set_effect(trigger_ids=[5016]) # 경로 안내
        self.set_effect(trigger_ids=[5017]) # 경로 안내
        self.set_effect(trigger_ids=[5018]) # 경로 안내
        self.set_effect(trigger_ids=[4000])
        self.set_effect(trigger_ids=[4001])
        self.set_effect(trigger_ids=[4002])
        self.set_effect(trigger_ids=[4002])
        self.set_effect(trigger_ids=[4003])
        self.set_effect(trigger_ids=[4004])
        self.set_effect(trigger_ids=[4005])
        self.set_effect(trigger_ids=[4006])
        self.set_effect(trigger_ids=[4007])
        self.set_effect(trigger_ids=[4008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002301], quest_states=[3]):
            self.move_user(map_id=52000109, portal_id=1)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002297], quest_states=[1]):
            # 퓨전코어 불끄기
            return 불끄기퀘스트01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002298], quest_states=[1]):
            return 워터슬라임퀘스트01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002300], quest_states=[1]):
            return 저항군로봇퀘스트01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002301], quest_states=[1]):
            return 저항군로봇퀘스트01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002300], quest_states=[3]):
            return 저항군로봇퀘스트01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002299], quest_states=[3]):
            return 저항군로봇퀘스트01(self.ctx)


class 불끄기퀘스트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[2000], return_view=False)
        self.move_user(map_id=52000108, portal_id=10)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 불끄기퀘스트02(self.ctx)


class 불끄기퀘스트02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npc_id=11003292, illust_id='0', msg='$52000108_QD__52000108__0$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000972, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000972.xml')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_ishaTrun')
        self.move_user_path(patrol_name='MS2PatrolData_PCTrun')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 불끄기퀘스트03(self.ctx)


class 불끄기퀘스트03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__1$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 불끄기퀘스트04(self.ctx)


class 불끄기퀘스트04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__2$', duration=4000, align=Align.Right)
        self.set_pc_emotion_loop(sequence_name='Emotion_Dance_S', duration=4000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 불끄기퀘스트05(self.ctx)


class 불끄기퀘스트05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__3$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 불끄기퀘스트06(self.ctx)


class 불끄기퀘스트06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=9000, enable=True)
        self.select_camera_path(path_ids=[2002], return_view=False)
        self.set_onetime_effect(id=40, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npc_id=11003292, illust_id='0', msg='$52000108_QD__52000108__4$', duration=6000, align=Align.Right)
        self.set_onetime_effect(id=3000973, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000973.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 불끄기퀘스트07(self.ctx)


class 불끄기퀘스트07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=50, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__5$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 불끄기퀘스트08(self.ctx)


class 불끄기퀘스트08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003292, illust_id='$52000108_QD__52000108__45$', msg='$52000108_QD__52000108__6$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000974, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000974.xml')
        self.select_camera_path(path_ids=[2003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 불끄기퀘스트09(self.ctx)


class 불끄기퀘스트09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=60, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.select_camera_path(path_ids=[2004], return_view=False)
        self.set_mesh(trigger_ids=[2001], visible=True)
        self.add_cinematic_talk(npc_id=11003292, msg='$52000108_QD__52000108__7$', duration=8000, align=Align.Right)
        self.set_onetime_effect(id=3000975, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000975.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9500):
            return 불끄기퀘스트10(self.ctx)


class 불끄기퀘스트10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2003], return_view=False)
        self.add_cinematic_talk(npc_id=11003292, illust_id='0', msg='$52000108_QD__52000108__8$', duration=5000, align=Align.Right)
        self.set_onetime_effect(id=3000976, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000976.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 불끄기퀘스트11(self.ctx)


class 불끄기퀘스트11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2008], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__9$', duration=2000, align=Align.Right)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Choice_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 불끄기퀘스트12(self.ctx)


class 불끄기퀘스트12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__10$', duration=4000, align=Align.Right)
        self.set_pc_emotion_loop(sequence_name='Snare_A', duration=5000.0)
        self.face_emotion(emotion_name='PC_OutOfMind_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 불끄기퀘스트13(self.ctx)


class 불끄기퀘스트13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트대기01_20002300(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52000108, portal_id=10)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_ishaTrun')
        self.set_mesh(trigger_ids=[2001], visible=True)
        self.reset_camera(interpolation_time=1.0)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 퀘스트대기01_20002300(self.ctx)


class 퀘스트대기01_20002300(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201081, text_id=25201081, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002298], quest_states=[1]):
            return 워터슬라임퀘스트01(self.ctx)


class 워터슬라임퀘스트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[300,301,302,303,304,305], auto_target=False)
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_caitSneak') # 케이틀린 이동
        self.show_guide_summary(entity_id=25201082, text_id=25201082, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002299], quest_states=[3]):
            return 저항군로봇퀘스트01(self.ctx)


# ########################20002300수락, 반마법세력 저항군 등장########################
class 저항군로봇퀘스트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=9000)
        self.set_sound(trigger_id=9001, enable=True)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[2013,2014], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000108, portal_id=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 저항군로봇퀘스트02(self.ctx)


class 저항군로봇퀘스트02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__11$', duration=6000, align=Align.Right)
        self.set_pc_emotion_loop(sequence_name='Object_React_D', duration=25000.0)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_ishaCom')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 저항군로봇퀘스트03(self.ctx)


class 저항군로봇퀘스트03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003292, msg='$52000108_QD__52000108__12$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000977, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000977.xml')
        self.select_camera_path(path_ids=[2015], return_view=False)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_isha_8')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 저항군로봇퀘스트04(self.ctx)


class 저항군로봇퀘스트04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__13$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 저항군로봇퀘스트05(self.ctx)


class 저항군로봇퀘스트05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__14$', duration=4000, align=Align.Right)
        self.select_camera_path(path_ids=[2016], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 저항군로봇퀘스트06(self.ctx)


class 저항군로봇퀘스트06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003292, msg='$52000108_QD__52000108__15$', duration=6000, align=Align.Right)
        self.set_onetime_effect(id=3000978, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000978.xml')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_isha_9')
        self.select_camera_path(path_ids=[2017,2018], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 저항군로봇퀘스트07(self.ctx)


class 저항군로봇퀘스트07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__16$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 저항군로봇퀘스트08(self.ctx)


class 저항군로봇퀘스트08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2028], return_view=False)
        self.add_cinematic_talk(npc_id=11003292, msg='$52000108_QD__52000108__17$', duration=6000, align=Align.Right)
        self.set_onetime_effect(id=3000979, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000979.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 저항군로봇퀘스트09(self.ctx)


class 저항군로봇퀘스트09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=9002, enable=True)
        self.set_time_scale(enable=True, start_scale=0.1, end_scale=0.1, duration=7.0, interpolator=2)
        self.set_skill(trigger_ids=[500], enable=True)
        self.select_camera_path(path_ids=[2010,2019], return_view=False)
        self.set_effect(trigger_ids=[4000], visible=True)
        self.set_effect(trigger_ids=[4001], visible=True)
        self.set_effect(trigger_ids=[4002], visible=True)
        self.move_user_path(patrol_name='MS2PatrolData_PC_TurnLeft')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 저항군로봇퀘스트10(self.ctx)


class 저항군로봇퀘스트10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(emotion_name='PC_OutOfMind_01')
        self.select_camera_path(path_ids=[2031], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__18$', duration=3000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 저항군로봇퀘스트11(self.ctx)


class 저항군로봇퀘스트11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 체키등장
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 지그문트등장
        self.spawn_monster(spawn_ids=[206], auto_target=False) # 헨리테등장
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_Checky')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_sigmund')
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_henry')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_IshaCheck')
        self.select_camera_path(path_ids=[2011,2012], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 저항군로봇퀘스트12a(self.ctx)


class 저항군로봇퀘스트12a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2029,2030], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 저항군로봇퀘스트12_b(self.ctx)


class 저항군로봇퀘스트12_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2020,2021], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 저항군로봇퀘스트12_c(self.ctx)


class 저항군로봇퀘스트12_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_caption(type='NameCaption', title='$52000108_QD__52000108__19$', align=Align.Center, offset_rate_x=-0.15, offset_rate_y=0.15, duration=3500, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4100):
            return 저항군로봇퀘스트13(self.ctx)


class 저항군로봇퀘스트13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2022,2023], return_view=False)
        self.show_caption(type='NameCaption', title='$52000108_QD__52000108__20$', align=Align.Center, offset_rate_x=-0.15, offset_rate_y=0.15, duration=3500, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4100):
            return 저항군로봇퀘스트14(self.ctx)


class 저항군로봇퀘스트14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Bore_B')
        self.select_camera_path(path_ids=[2024,2025], return_view=False)
        self.show_caption(type='NameCaption', title='$52000108_QD__52000108__22$', align=Align.Center, offset_rate_x=-0.15, offset_rate_y=0.15, duration=3500, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4100):
            return 저항군로봇퀘스트15(self.ctx)


class 저항군로봇퀘스트15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000108, portal_id=11)
        self.select_camera_path(path_ids=[2026,2027], return_view=False)
        self.show_caption(type='NameCaption', title='$52000108_QD__52000108__24$', desc='$52000108_QD__52000108__25$', align=Align.Top | Align.Center, duration=4000, scale=3.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4100):
            return 저항군로봇퀘스트15_1(self.ctx)


class 저항군로봇퀘스트15_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 저항군로봇퀘스트16(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52000108, portal_id=11)
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 체키등장
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 지그문트등장
        self.spawn_monster(spawn_ids=[206], auto_target=False) # 헨리테등장
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_Checky')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_sigmund')
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_henry')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_IshaCheck')
        self.set_skill(trigger_ids=[500], enable=True)
        self.set_effect(trigger_ids=[4000], visible=True)
        self.set_effect(trigger_ids=[4001], visible=True)
        self.set_effect(trigger_ids=[4002], visible=True)
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 저항군로봇퀘스트16(self.ctx)


class 저항군로봇퀘스트16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion()
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201083, text_id=25201083, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002301], quest_states=[3]):
            self.move_user(map_id=52000109, portal_id=1)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002301], quest_states=[2]):
            return 프로토콜해피01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002301], quest_states=[1]):
            return 체키등판퀘스트01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002300], quest_states=[1]):
            return 저항군로봇퀘스트17(self.ctx)


class 저항군로봇퀘스트17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_sigmund_back')
        self.spawn_monster(spawn_ids=[306,307,308,309,310], auto_target=False)
        self.show_guide_summary(entity_id=25201084, text_id=25201084, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002301], quest_states=[1]):
            return 체키등판퀘스트01(self.ctx)


# ########################20002301수락, 체키 등판########################
class 체키등판퀘스트01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[2032,2033], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(map_id=52000108, portal_id=11)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_sigmund_back')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 체키등판퀘스트02(self.ctx)


class 체키등판퀘스트02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_3, action='nextState')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npc_id=11003191, msg='$52000108_QD__52000108__26$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 체키등판퀘스트03(self.ctx)


class 체키등판퀘스트03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2034,2035], return_view=False)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_CheckyBoss')
        self.add_cinematic_talk(npc_id=11003191, msg='$52000108_QD__52000108__27$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 체키등판퀘스트04(self.ctx)


class 체키등판퀘스트04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2036], return_view=False)
        self.add_cinematic_talk(npc_id=11003184, msg='$52000108_QD__52000108__28$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5459):
            return 체키등판퀘스트05(self.ctx)


class 체키등판퀘스트05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2037,2038], return_view=False)
        self.add_cinematic_talk(npc_id=11003191, msg='$52000108_QD__52000108__29$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 체키등판퀘스트06(self.ctx)


class 체키등판퀘스트06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2039,2040], return_view=False)
        self.add_cinematic_talk(npc_id=11003184, msg='$52000108_QD__52000108__30$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4388):
            return 체키등판퀘스트06_1(self.ctx)


class 체키등판퀘스트06_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 체키등판퀘스트07(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_CheckyBoss')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 체키등판퀘스트07(self.ctx)


class 체키등판퀘스트07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[201])
        self.spawn_monster(spawn_ids=[311], auto_target=False)
        self.add_balloon_talk(msg='$52000108_QD__52000108__31$', duration=5000, delay_tick=1000)
        self.add_balloon_talk(spawn_id=205, msg='$52000108_QD__52000108__32$', duration=6000, delay_tick=4000)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_IshaOut')
        self.show_guide_summary(entity_id=25201085, text_id=25201085, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002301], quest_states=[2]):
            return 프로토콜해피01(self.ctx)


# ########################코어폭발씬########################
class 프로토콜해피01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[2041,2042], return_view=False)
        self.move_user(map_id=52000108, portal_id=11)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[200,201,202,311])
        self.spawn_monster(spawn_ids=[208,209,210], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 프로토콜해피02(self.ctx)


class 프로토콜해피02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_4, action='nextState')
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.add_cinematic_talk(npc_id=11003191, msg='$52000108_QD__52000108__33$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 프로토콜해피03(self.ctx)


class 프로토콜해피03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC_front')
        self.select_camera_path(path_ids=[2043], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__34$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 프로토콜해피04(self.ctx)


class 프로토콜해피04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(emotion_name='ChaosMod_Start')
        self.select_camera_path(path_ids=[2044], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__35$', duration=2500, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 프로토콜해피05(self.ctx)


class 프로토콜해피05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=208, sequence_name='Attack_Idle_A', duration=20000.0)
        self.select_camera_path(path_ids=[2045,2046], return_view=False)
        self.add_cinematic_talk(npc_id=11003292, msg='$52000108_QD__52000108__36$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000980, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000980.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 프로토콜해피06(self.ctx)


class 프로토콜해피06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion()
        self.select_camera_path(path_ids=[2047], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__37$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 프로토콜해피07(self.ctx)


class 프로토콜해피07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=209, emotion_name='Surprised')
        self.select_camera_path(path_ids=[2048], return_view=False)
        self.add_cinematic_talk(npc_id=11003183, msg='$52000108_QD__52000108__38$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 프로토콜해피08(self.ctx)


class 프로토콜해피08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2049,2050], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__39$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 프로토콜해피09(self.ctx)


class 프로토콜해피09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[2051,2053], return_view=False)
        self.add_cinematic_talk(npc_id=0, illust_id='0', msg='$52000108_QD__52000108__40$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 프로토콜해피10(self.ctx)


class 프로토콜해피10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=209, sequence_name='Bore_A')
        self.select_camera_path(path_ids=[2052], return_view=False)
        self.add_cinematic_talk(npc_id=11003183, msg='$52000108_QD__52000108__41$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 프로토콜해피10_1(self.ctx)


class 프로토콜해피10_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 프로토콜해피11(self.ctx)


class Skip_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolation_time=1.0)
        self.move_user(map_id=52000108, portal_id=11)
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 프로토콜해피11(self.ctx)


class 프로토콜해피11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[4003], visible=True)
        self.set_effect(trigger_ids=[4004], visible=True)
        self.set_effect(trigger_ids=[4005], visible=True)
        self.set_effect(trigger_ids=[4006], visible=True)
        self.set_effect(trigger_ids=[4007], visible=True)
        self.set_effect(trigger_ids=[4008], visible=True)
        self.destroy_monster(spawn_ids=[209,210,206])
        self.set_effect(trigger_ids=[5000], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5001], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5002], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5003], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5004], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5005], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5006], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5007], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5008], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5009], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5010], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5011], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5012], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5013], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5014], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5015], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5016], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5017], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5018], visible=True) # 경로 안내
        self.destroy_monster(spawn_ids=[208])
        self.spawn_monster(spawn_ids=[211])
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.add_balloon_talk(msg='$52000108_QD__52000108__42$', duration=6000, delay_tick=1000)
        self.show_guide_summary(entity_id=25201086, text_id=25201086, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[10011]):
            return 프로토콜해피12(self.ctx)


class 프로토콜해피12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=211, msg='$52000108_QD__52000108__43$', duration=6000, delay_tick=1000)
        self.set_onetime_effect(id=3000981, enable=True, path='BG/Common/Sound/Eff_Ayesha_IntroMovie_03000981.xml')
        self.show_guide_summary(entity_id=25201086, text_id=25201086, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[20002301], quest_states=[3]):
            return 프로토콜해피13(self.ctx)


class 프로토콜해피13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=211, patrol_name='MS2PatrolData_fallback')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 프로토콜해피14(self.ctx)


class 프로토콜해피14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[211])
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 프로토콜해피13(self.ctx)


initial_state = Wait
