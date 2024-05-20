""" trigger/52000100_qd/52000100.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 아노스
        self.set_effect(trigger_ids=[901])
        self.set_effect(trigger_ids=[902])
        self.set_effect(trigger_ids=[903])
        self.set_effect(trigger_ids=[904])
        self.set_effect(trigger_ids=[905])
        self.set_effect(trigger_ids=[906])
        self.set_effect(trigger_ids=[907])
        self.set_effect(trigger_ids=[908])
        self.set_effect(trigger_ids=[909])
        self.set_effect(trigger_ids=[5305]) # 경로 안내
        self.set_effect(trigger_ids=[5306]) # 경로 안내
        self.set_effect(trigger_ids=[5307]) # 경로 안내
        self.set_effect(trigger_ids=[5308]) # 경로 안내
        self.set_effect(trigger_ids=[5309]) # 경로 안내
        self.set_effect(trigger_ids=[5310]) # 경로 안내
        self.set_effect(trigger_ids=[5305]) # 경로 안내
        self.set_effect(trigger_ids=[5400]) # 경로 안내
        self.set_effect(trigger_ids=[5401]) # 경로 안내
        self.set_effect(trigger_ids=[5402]) # 경로 안내
        self.set_effect(trigger_ids=[5403]) # 경로 안내
        self.set_effect(trigger_ids=[5404]) # 경로 안내
        self.set_effect(trigger_ids=[5405]) # 경로 안내
        self.set_effect(trigger_ids=[5406]) # 경로 안내
        self.set_effect(trigger_ids=[5407]) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002290], quest_states=[3]):
            # 몬스터 처치 수업을 다 끝내면 케이틀린 등장
            return 케이틀린대련01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002292], quest_states=[2]):
            # 아시모프에게 퀘스트를 받고 교장실로 향함
            return 아시모프와대화01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002291], quest_states=[1]):
            # 대련 퀘스트를 받으면 케이틀린 등장
            return 케이틀린대련04(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002291], quest_states=[2]):
            # 대련 퀘스트를 받으면 케이틀린 등장
            return 대련종료씬시작02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002290], quest_states=[1]):
            return 몬스터소환교육04(self.ctx)
        if self.quest_user_detected(box_ids=[9003], quest_ids=[20002286], quest_states=[2]):
            # 케이틀린에게 퀘스트를 받고 강의실로 향함
            return 강의실입장01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002287], quest_states=[1]):
            # 몬스터 소환 교육
            return 참교육01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002288], quest_states=[1]):
            # 몬스터 소환 교육
            return 참교육02(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002289], quest_states=[1]):
            # 몬스터 소환 교육
            return 몬스터소환교육01(self.ctx)


class 강의실입장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5305], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5306], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5307], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5308], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5309], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5310], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002286], quest_states=[2]):
            # 케이틀린에게 퀘스트를 받고 강의실로 향함
            return 아노스등장01(self.ctx)


class 아노스등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000100, portal_id=3)
        self.set_effect(trigger_ids=[5305]) # 경로 안내
        self.set_effect(trigger_ids=[5306]) # 경로 안내
        self.set_effect(trigger_ids=[5307]) # 경로 안내
        self.set_effect(trigger_ids=[5308]) # 경로 안내
        self.set_effect(trigger_ids=[5309]) # 경로 안내
        self.set_effect(trigger_ids=[5310]) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아노스등장02(self.ctx)


class 아노스등장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_pc_emotion_loop(sequence_name='Emotion_Disappoint_Idle_A', duration=2000.0)
        self.select_camera_path(path_ids=[4000,4001], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003148, illust_id='Anos_normal', msg='$52000100_QD__52000100__0$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 아노스등장03(self.ctx)


class 아노스등장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4002], return_view=False)
        self.show_caption(type='NameCaption', title='$52000100_QD__52000100__1$', desc='$52000100_QD__52000100__2$', align=Align.Center, offset_rate_x=-0.05, offset_rate_y=0.15, duration=10000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 아노스등장03_1(self.ctx)


class 아노스등장03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아노스등장04(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아노스등장04(self.ctx)


class 아노스등장04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=25201001, text_id=25201001, duration=8000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002287], quest_states=[1]):
            return 참교육01(self.ctx)


class 참교육01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201002, text_id=25201002, duration=8000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002288], quest_states=[1]):
            return 참교육02(self.ctx)


class 참교육02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5401], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5402], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5403], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5404], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5405], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5406], visible=True) # 경로 안내
        self.set_effect(trigger_ids=[5407], visible=True) # 경로 안내
        self.show_guide_summary(entity_id=25201003, text_id=25201003, duration=8000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002288], quest_states=[2]):
            return 참교육완료(self.ctx)


class 참교육완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400]) # 경로 안내
        self.set_effect(trigger_ids=[5401]) # 경로 안내
        self.set_effect(trigger_ids=[5402]) # 경로 안내
        self.set_effect(trigger_ids=[5403]) # 경로 안내
        self.set_effect(trigger_ids=[5404]) # 경로 안내
        self.set_effect(trigger_ids=[5405]) # 경로 안내
        self.set_effect(trigger_ids=[5406]) # 경로 안내
        self.set_effect(trigger_ids=[5407]) # 경로 안내
        self.show_guide_summary(entity_id=25201003, text_id=25201003, duration=8000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002289], quest_states=[1]):
            return 몬스터소환교육01(self.ctx)


# ########################씬2 몬스터 소환 교육01~02########################
class 몬스터소환교육01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5400]) # 경로 안내
        self.set_effect(trigger_ids=[5401]) # 경로 안내
        self.set_effect(trigger_ids=[5402]) # 경로 안내
        self.set_effect(trigger_ids=[5403]) # 경로 안내
        self.set_effect(trigger_ids=[5404]) # 경로 안내
        self.set_effect(trigger_ids=[5405]) # 경로 안내
        self.set_effect(trigger_ids=[5406]) # 경로 안내
        self.set_effect(trigger_ids=[5407]) # 경로 안내
        self.spawn_monster(spawn_ids=[300,301,302,303,304,305], auto_target=False)
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_caitSneak') # 케이틀린 이동
        self.show_guide_summary(entity_id=25201004, text_id=25201004, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[300,301,302,303,304,305]):
            return 몬스터소환교육02(self.ctx)


class 몬스터소환교육02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002290], quest_states=[1]):
            return 몬스터소환교육04(self.ctx)


class 몬스터소환교육04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[400,401,402,403,404,405], auto_target=False)
        self.show_guide_summary(entity_id=25201005, text_id=25201005, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002290], quest_states=[3]):
            # 몬스터 처치 수업을 다 끝내면 케이틀린 등장
            return 케이틀린대련01(self.ctx)


# ########################씬3 케이틀린 대련########################
class 케이틀린대련01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(trigger_id=9006, enable=True) # 케이틀린 등장 브금
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[203], auto_target=False) # 케이틀린
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_caitComeOut') # 케이틀린 이동
        self.select_camera_path(path_ids=[4003,4004], return_view=False)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_turnAnos')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 케이틀린대련02(self.ctx)


class 케이틀린대련02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.face_emotion(spawn_id=200, emotion_name='UpSet')
        self.add_cinematic_talk(npc_id=11003146, illust_id='Caitlyn_normal', msg='$52000100_QD__52000100__3$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000950, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000950.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 케이틀린대련03(self.ctx)


class 케이틀린대련03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003146, illust_id='Caitlyn_normal', msg='$52000100_QD__52000100__4$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000951, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000951.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 케이틀린대련03_b(self.ctx)


class 케이틀린대련03_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003146, illust_id='Caitlyn_normal', msg='$52000100_QD__52000100__5$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000952, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000952.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 케이틀린대련03_b_1(self.ctx)


class 케이틀린대련03_b_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 케이틀린대련03_c(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 케이틀린대련03_c(self.ctx)


class 케이틀린대련03_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolation_time=0.5)
        self.show_guide_summary(entity_id=25201006, text_id=25201006, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002291], quest_states=[3]):
            # 대련 퀘스트를 받으면 케이틀린 등장
            return 대련종료씬시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002291], quest_states=[2]):
            # 대련 퀘스트를 받으면 케이틀린 등장
            return 대련종료씬시작01(self.ctx)
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002291], quest_states=[1]):
            # 대련 퀘스트를 받으면 케이틀린 등장
            return 케이틀린대련04(self.ctx)


class 케이틀린대련04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(box_ids=[9003], skill_id=70000109, level=1, is_player=False, is_skill_set=False) # 초생회
        self.set_sound(trigger_id=9006, enable=True) # 케이틀린 대련 브금
        self.destroy_monster(spawn_ids=[203])
        self.spawn_monster(spawn_ids=[500], auto_target=False) # 케이틀린
        self.show_guide_summary(entity_id=25201007, text_id=25201007, duration=5000)
        self.add_buff(box_ids=[9001], skill_id=99910231, level=1, is_player=False, is_skill_set=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 케이틀린대련05(self.ctx)


class 케이틀린대련05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=25201008, text_id=25201008, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[500]):
            return 대련종료씬시작01(self.ctx)


class 대련종료씬시작01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.destroy_monster(spawn_ids=[203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 대련종료씬시작02(self.ctx)


# ########################대련 종료씬########################
class 대련종료씬시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(box_id=9001, skill_id=99910231)
        self.set_cinematic_ui(type=1)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.spawn_monster(spawn_ids=[501], auto_target=False)
        self.move_user(map_id=52000100, portal_id=4)
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_caitRun')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 대련종료씬시작03(self.ctx)


class 대련종료씬시작03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_3, action='nextState')
        self.move_user_path(patrol_name='MS2PatrolData_PCRun')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[4005,4006], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대련종료씬시작04(self.ctx)


class 대련종료씬시작04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=501, sequence_name='Bore_A')
        self.set_effect(trigger_ids=[902], visible=True)
        self.set_time_scale(enable=True, start_scale=0.6, end_scale=0.1, duration=3.5, interpolator=2) # 2초간 느려지기 시작
        self.select_camera_path(path_ids=[4007,4008], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 대련종료씬시작05(self.ctx)


class 대련종료씬시작05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009,4010,4027], return_view=False)
        self.set_time_scale(start_scale=1.0, end_scale=0.1, duration=2.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 대련종료씬시작06(self.ctx)


class 대련종료씬시작06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Wizard_Enterance_A'])
        self.set_pc_emotion_loop(sequence_name='Wizard_Enterance_A', duration=5000.0)
        self.set_effect(trigger_ids=[901], visible=True)
        self.set_time_scale(enable=True, start_scale=1.0, end_scale=0.1, duration=5.5, interpolator=2) # 2초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 대련종료씬시작07(self.ctx)


class 대련종료씬시작07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.1, end_scale=0.1, duration=6.5, interpolator=2) # 2초간 느려지기 시작
        self.set_npc_emotion_loop(spawn_id=501, sequence_name='Attack_Idle_A', duration=17500.0)
        self.set_pc_emotion_loop(sequence_name='Wizard_Enterance_A', duration=5000.0)
        self.select_camera_path(path_ids=[4011,4012], return_view=False)
        self.set_effect(trigger_ids=[908], visible=True)
        self.set_effect(trigger_ids=[909], visible=True)
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6500):
            return 대련종료씬시작08(self.ctx)


class 대련종료씬시작08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[901])
        self.set_effect(trigger_ids=[902])
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.move_user(map_id=52000100, portal_id=5)
        self.select_camera_path(path_ids=[4013,4014], return_view=False)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_anosCare')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 대련종료씬시작09(self.ctx)


class 대련종료씬시작09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=12000.0)
        self.set_skill(trigger_ids=[7005], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 대련종료씬시작09_b(self.ctx)


class 대련종료씬시작09_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_caitRun2')
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4015], return_view=False)
        self.add_cinematic_talk(npc_id=11003147, msg='$52000100_QD__52000100__6$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000964, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000964.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대련종료씬시작10(self.ctx)


class 대련종료씬시작10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4016], return_view=False)
        self.add_cinematic_talk(npc_id=11003147, msg='$52000100_QD__52000100__7$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000965, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000965.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 대련종료씬시작11(self.ctx)


class 대련종료씬시작11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4017], return_view=False)
        self.add_cinematic_talk(npc_id=11003148, msg='$52000100_QD__52000100__8$', duration=4000, align=Align.Right)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대련종료씬시작12(self.ctx)


class 대련종료씬시작12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=200, emotion_name='Surprised')
        self.select_camera_path(path_ids=[4018], return_view=False)
        self.add_cinematic_talk(npc_id=11003148, msg='$52000100_QD__52000100__9$', duration=4000, align=Align.Right)
        self.set_effect(trigger_ids=[902], visible=True)
        self.set_effect(trigger_ids=[903], visible=True)
        self.set_effect(trigger_ids=[904], visible=True)
        self.set_effect(trigger_ids=[905], visible=True)
        self.set_effect(trigger_ids=[906], visible=True)
        self.set_effect(trigger_ids=[907], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대련종료씬시작14(self.ctx)


class 대련종료씬시작14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4019], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대련종료씬시작15(self.ctx)


class 대련종료씬시작15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4020,4021], return_view=False)
        self.add_cinematic_talk(npc_id=11003147, msg='$52000100_QD__52000100__10$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000966, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000966.xml')
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_caitlookBack')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대련종료씬시작17(self.ctx)


class 대련종료씬시작17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4022,4023], return_view=False)
        self.add_cinematic_talk(npc_id=11003147, msg='$52000100_QD__52000100__11$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000967, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000967.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 대련종료씬시작17_b(self.ctx)


class 대련종료씬시작17_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003147, msg='$52000100_QD__52000100__12$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000968, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000968.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            return 대련종료씬시작18(self.ctx)


class 대련종료씬시작18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$52000100_QD__52000100__13$', duration=6000, delay_tick=1000)
        self.add_cinematic_talk(npc_id=11003147, msg='$52000100_QD__52000100__14$', duration=4000, align=Align.Right)
        self.set_onetime_effect(id=3000969, enable=True, path='BG/Common/Sound/Eff_Caitlyn_IntroQuest_03000969.xml')
        self.select_camera_path(path_ids=[4024,4025], return_view=False)
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_caitOut')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 대련종료씬시작18_1(self.ctx)


class 대련종료씬시작18_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대련종료(self.ctx)


class Skip_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOut.xml')
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_anosCare')
        self.set_effect(trigger_ids=[901])
        self.set_effect(trigger_ids=[902])
        self.set_effect(trigger_ids=[903])
        self.set_effect(trigger_ids=[904])
        self.set_effect(trigger_ids=[905])
        self.set_effect(trigger_ids=[906])
        self.set_effect(trigger_ids=[907])
        self.set_effect(trigger_ids=[908])
        self.set_effect(trigger_ids=[909])
        self.set_effect(trigger_ids=[902], visible=True)
        self.set_effect(trigger_ids=[903], visible=True)
        self.set_effect(trigger_ids=[904], visible=True)
        self.set_effect(trigger_ids=[905], visible=True)
        self.set_effect(trigger_ids=[906], visible=True)
        self.set_effect(trigger_ids=[907], visible=True)
        self.destroy_monster(spawn_ids=[501])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 대련종료(self.ctx)


class 대련종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[501])
        self.remove_buff(box_id=9003, skill_id=70000109)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002291], quest_states=[3]):
            return 아시모프와대화01(self.ctx)


# ########################씬4 아시모프와 대화########################
class 아시모프와대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_Pc_stepAside')
        self.set_cinematic_ui(type=1)
        self.spawn_monster(spawn_ids=[202], auto_target=False)
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_asmovMove')
        self.add_balloon_talk(spawn_id=202, msg='$52000100_QD__52000100__15$', duration=5000, delay_tick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 아시모프와대화03(self.ctx)


class 아시모프와대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_4, action='nextState')
        self.select_camera_path(path_ids=[4028], return_view=False)
        self.show_caption(type='NameCaption', title='$52000100_QD__52000100__16$', desc='$52000100_QD__52000100__17$', align=Align.Center, offset_rate_x=-0.05, offset_rate_y=0.15, duration=10000, scale=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            return 아시모프와대화03_1(self.ctx)


class 아시모프와대화03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아시모프와대화04(self.ctx)


class Skip_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.reset_camera(interpolation_time=0.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아시모프와대화04(self.ctx)


class 아시모프와대화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        # 아시모프를 따라 교장실로 향하세요 가이드 추가
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9001], quest_ids=[20002292], quest_states=[2]):
            # 아시모프에게 퀘스트를 받고 교장실로 향함
            return 아시모프와대화05(self.ctx)


class 아시모프와대화05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=202, msg='$52000100_QD__52000100__18$', duration=6000, delay_tick=1000)
        self.move_npc(spawn_id=200, patrol_name='MS2PatrolData_anos_goRoom')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_asimov_goRoom')
        self.show_guide_summary(entity_id=25201009, text_id=25201009, duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아시모프와대화06(self.ctx)


class 아시모프와대화06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000102, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=9003, spawn_ids=[202]):
            return 아시모프와대화04(self.ctx)


initial_state = Wait
