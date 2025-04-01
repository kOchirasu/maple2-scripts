""" trigger/52000150_qd/52000150.xml """
import trigger_api
from Maple2.Server.Game.Scripting.Trigger import Align


class Wait01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2605])
        self.set_effect(trigger_ids=[2607], visible=True)
        self.spawn_monster(spawn_ids=[202], auto_target=False) # 케이틀린
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 아노스
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 호르헤

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001642], quest_states=[1]):
            # B퀘스트가 완료상태 일때
            return 퀘스트완료상태에서접속(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[3]):
            # B퀘스트가 완료상태 일때
            return 퀘스트완료상태에서접속(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[2]):
            # B퀘스트가 완료가능상태일때
            return 퀘스트완료상태에서접속(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[1]):
            # B퀘스트가 진행상태 일때
            return Skip_1(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001640], quest_states=[3]):
            # A퀘스트가 완료상태 일때
            return Wait02(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001640], quest_states=[2]):
            # A퀘스트가 진행상태 일때
            return Wait02(self.ctx)


class Wait02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 차원의숲전경씬01(self.ctx)


class 차원의숲전경씬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_1, action='nextState')
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000150, portal_id=11)
        self.select_camera_path(path_ids=[1000,1001,1004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=8000):
            return 차원의숲전경씬02_b(self.ctx)


class 차원의숲전경씬02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차원의숲전경씬02(self.ctx)


class 차원의숲전경씬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.select_camera_path(path_ids=[1002,1003], return_view=False)
        self.show_caption(type='VerticalCaption', title='$52000150_QD__52000150__8$', desc='$52000150_QD__52000150__9$', align=Align.bottomLeft, duration=5500, scale=2.5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 차원의숲전경씬03(self.ctx)


class 차원의숲전경씬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 차원의숲전경씬03_1(self.ctx)


class 차원의숲전경씬03_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차원의숲전경씬종료(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52000150, portal_id=11)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 차원의숲전경씬종료(self.ctx)


class 차원의숲전경씬종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_caitMove01') # 케이틀린 이동
        self.add_balloon_talk(spawn_id=202, msg='$52000150_QD__52000150__0$', duration=6000, delay_tick=1000) # 케이틀린 대사
        self.show_guide_summary(entity_id=25201501, text_id=25201501, duration=10000) # 가이드 메시지 : 호르헤와 아노스에게 가기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[3]):
            # B퀘스트가 완료상태 일때
            return 아노스흑화01(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[2]):
            # B퀘스트가 진행 중 일때
            return 퀘스트완료상태에서접속(self.ctx)
        if self.quest_user_detected(box_ids=[10010], quest_ids=[50001641], quest_states=[1]):
            # B퀘스트가 진행 중 일때
            return 결계흑화연출01(self.ctx)


# ########################씬3 요동치기 시작한 아노스의 결계########################
class 결계흑화연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=Skip_2, action='nextState')
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000150, portal_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 결계흑화연출02(self.ctx)


class 결계흑화연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 결계흑화연출03(self.ctx)


class 결계흑화연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2608], visible=True)
        self.select_camera_path(path_ids=[3001,3000], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Traped_A,Traped_Idle')
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003439, msg='$52000150_QD__52000150__1$', duration=4000, align=Align.right) # 호르헤 대사
        # ########################크윽…! 에너지 역류…? 결계를 거부하는 건가…!!########################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=800):
            return 결계흑화연출03_b(self.ctx)


class 결계흑화연출03_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=202, emotion_name='Bore_A')
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Traped_Idle', duration=999999.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4200):
            return 결계흑화연출04(self.ctx)


class 결계흑화연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Bore_A')
        self.select_camera_path(path_ids=[3002,3003], return_view=False)
        self.add_cinematic_talk(npc_id=11003442, msg='$52000150_QD__52000150__2$', duration=5000, align=Align.right) # 케이틀린 대사
        # ########################이건… 이건 아노스 선생님의 의지가 아냐!!########################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 결계흑화연출05(self.ctx)


class 결계흑화연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=202, sequence_name='Attack_Idle_A', duration=999999.0)
        self.set_effect(trigger_ids=[2606], visible=True)
        self.select_camera_path(path_ids=[3004,3005], return_view=False)
        self.add_cinematic_talk(npc_id=11003442, msg='$52000150_QD__52000150__3$', duration=5000, align=Align.right) # 케이틀린 대사
        # ########################선생님!! 정신 차리세요, 선생님!!!!########################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 결계흑화연출06(self.ctx)


class 결계흑화연출06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2606], visible=True)
        self.select_camera_path(path_ids=[3006,3007], return_view=False)
        self.set_effect(trigger_ids=[2300,2301,2302,2303,2304], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2400,2401,2402,2403,2404], visible=True, start_delay=200, interval=200) # #####1번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2500,2501,2502,2503,2504], visible=True, start_delay=400, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2600,2601,2602,2603,2604], visible=True, start_delay=600, interval=200) # #####2번 지역 리젠 알림#####
        self.spawn_monster(spawn_ids=[400,401,402,403,404], auto_target=False, delay=21000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 결계흑화연출07(self.ctx)


class 결계흑화연출07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2606], visible=True)
        self.set_effect(trigger_ids=[2300,2301,2302,2303,2304], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2400,2401,2402,2403,2404], visible=True, start_delay=200, interval=200) # #####1번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2500,2501,2502,2503,2504], visible=True, start_delay=400, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2600,2601,2602,2603,2604], visible=True, start_delay=600, interval=200) # #####2번 지역 리젠 알림#####
        self.select_camera_path(path_ids=[3008,3009,3010], return_view=False)
        self.add_cinematic_talk(npc_id=11003442, msg='$52000150_QD__52000150__4$', duration=4000, align=Align.right) # 케이틀린 대사
        # ########################…아노스 선생님,선생님은 반드시 제가 지키겠어요.########################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 결계흑화연출08(self.ctx)


class 결계흑화연출08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2606], visible=True)
        self.set_effect(trigger_ids=[2300,2301,2302,2303,2304], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2400,2401,2402,2403,2404], visible=True, start_delay=200, interval=200) # #####1번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2500,2501,2502,2503,2504], visible=True, start_delay=400, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2600,2601,2602,2603,2604], visible=True, start_delay=600, interval=200) # #####2번 지역 리젠 알림#####
        self.add_cinematic_talk(npc_id=11003442, msg='$52000150_QD__52000150__5$', duration=4000, align=Align.right) # 케이틀린 대사
        # ########################…어떤 대가를 치루더라도…당신 만큼은…########################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 결계흑화연출09(self.ctx)


class 결계흑화연출09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2606], visible=True)
        self.set_effect(trigger_ids=[2300,2301,2302,2303,2304], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2400,2401,2402,2403,2404], visible=True, start_delay=200, interval=200) # #####1번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2500,2501,2502,2503,2504], visible=True, start_delay=400, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2600,2601,2602,2603,2604], visible=True, start_delay=600, interval=200) # #####2번 지역 리젠 알림#####
        self.select_camera_path(path_ids=[3011,3012], return_view=False)
        self.add_cinematic_talk(npc_id=11003442, msg='$52000150_QD__52000150__6$', duration=4000, align=Align.right) # 케이틀린 대사
        # ########################…호르헤 선생님! 잠시만 참을 수 있겠죠?! 이 몬스터들을 쓸어버리고 선생님을 진정 시킬게요!!########################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 결계흑화연출10(self.ctx)


class 결계흑화연출10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2606], visible=True)
        self.set_effect(trigger_ids=[2300,2301,2302,2303,2304], visible=True, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2400,2401,2402,2403,2404], visible=True, start_delay=200, interval=200) # #####1번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2500,2501,2502,2503,2504], visible=True, start_delay=400, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2600,2601,2602,2603,2604], visible=True, start_delay=600, interval=200) # #####2번 지역 리젠 알림#####
        self.select_camera_path(path_ids=[3013], return_view=False)
        self.add_cinematic_talk(npc_id=11003442, msg='$52000150_QD__52000150__7$', duration=4000, align=Align.right) # 케이틀린 대사
        # ########################MyPcName!! 어서 준비해!########################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 결계흑화연출10_1(self.ctx)


class 결계흑화연출10_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 결계흑화연출11(self.ctx)


class Skip_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=4)
        self.set_effect(trigger_ids=[2605])
        self.set_effect(trigger_ids=[2606])
        self.set_effect(trigger_ids=[2607])
        self.set_effect(trigger_ids=[2608])
        self.set_effect(trigger_ids=[2300,2301,2302,2303,2304], interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2400,2401,2402,2403,2404], start_delay=200, interval=200) # #####1번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2500,2501,2502,2503,2504], start_delay=400, interval=200) # #####2번 지역 리젠 알림#####
        self.set_effect(trigger_ids=[2600,2601,2602,2603,2604], start_delay=600, interval=200) # #####2번 지역 리젠 알림#####
        self.move_user(map_id=52000150, portal_id=10)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_npc_emotion_loop(spawn_id=201, sequence_name='Traped_Idle', duration=999999.0)
        self.destroy_monster(spawn_ids=[400,401,402,403,404])
        self.spawn_monster(spawn_ids=[400,401,402,403,404], auto_target=False, delay=100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 결계흑화연출11(self.ctx)


class 결계흑화연출11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()
        self.set_sound(trigger_id=9000, enable=True) # 전투 상황 브금
        self.destroy_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[700], auto_target=False)
        self.set_user_value(trigger_id=10001, key='52000150', value=1) # 전투 컨텐츠 시작을 위한 벨류 세팅
        self.show_guide_summary(entity_id=25201502, text_id=25201502, duration=10000) # 전투 가이드 : 결계 주변의 몬스터 섬멸하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아노스흑화준비(self.ctx) # 아노스흑화01"/


class 아노스흑화준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=10001, key='52000150', value=0) # 전투 컨텐츠 시작을 위한 벨류 세팅

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='52000150monster') == 1:
            # 통신 받음 : 몬스터 다 잡으면 쏴주는 신호
            return 아노스흑화대기(self.ctx) # 아노스흑화01"/


class 아노스흑화대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[2605])
        self.set_effect(trigger_ids=[2606])
        self.set_effect(trigger_ids=[2607])
        self.set_effect(trigger_ids=[2608])
        self.move_user(map_id=52000150, portal_id=10)
        self.destroy_monster(spawn_ids=[200], arg2=False) # 아노스
        self.destroy_monster(spawn_ids=[201], arg2=False) # 호르헤
        self.destroy_monster(spawn_ids=[202])
        self.spawn_monster(spawn_ids=[200], auto_target=False) # 아노스
        self.spawn_monster(spawn_ids=[201], auto_target=False) # 호르헤
        self.spawn_monster(spawn_ids=[700], auto_target=False)
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스흑화전대사01(self.ctx)


class 아노스흑화전대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=아노스흑화09, action='exit')
        self.select_camera_path(path_ids=[3005], return_view=False)
        self.add_cinematic_talk(npc_id=11003440, msg='$52000150_QD__52000150__11$', duration=4000, align=Align.right) # 아노스 대사
        # #######################아노스#윽… 여긴…어디죠…? 케이틀린… 플레이어이름… 그리고… 호르헤.###scriptkey:0713175511006310####################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 아노스흑화전대사02(self.ctx)


class 아노스흑화전대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[3002], return_view=False)
        self.add_cinematic_talk(npc_id=11003442, illust_id='Caitlyn_serious', msg='$52000150_QD__52000150__12$', duration=3000, align=Align.right) # 케이틀린 대사
        # #######################케이틀린#…선생님…\n이제 괜찮아요. 저희가 지켜드릴게요…#scriptkey:0713175511006311#######################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스흑화전대사03(self.ctx)


class 아노스흑화전대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[6000,6001], return_view=False)
        self.add_cinematic_talk(npc_id=11003440, msg='$52000150_QD__52000150__13$', duration=3000, align=Align.right) # 아노스 대사
        # #######################아노스#윽…!\n으으…으아아!!###scriptkey:없음####################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스흑화전대사04(self.ctx)


class 아노스흑화전대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[3002], return_view=False)
        self.add_cinematic_talk(npc_id=11003442, illust_id='Caitlyn_serious', msg='$52000150_QD__52000150__14$', duration=3000, align=Align.right) # 케이틀린 대사
        # #######################케이틀린#…선생님?!#scriptkey:0713175511006314#######################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스흑화전대사05(self.ctx)


class 아노스흑화전대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(path_ids=[3001], return_view=False)
        self.add_cinematic_talk(npc_id=11003438, illust_id='Horrhe_normal', msg='$52000150_QD__52000150__15$', duration=3000, align=Align.left) # 호르헤 대사
        # #######################호르헤#$아노스?!\n대체 무슨 일이…?#scriptkey:0713175511006315#######################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스흑화전대사06(self.ctx)


class 아노스흑화전대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[6000], return_view=False)
        self.add_cinematic_talk(npc_id=11003440, msg='$52000150_QD__52000150__16$', duration=3000, align=Align.right) # 아노스 대사
        # #######################아노스#윽…!\n으으…으아아!!###scriptkey:0713175511006316####################

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스흑화01(self.ctx)


class 퀘스트완료상태에서접속(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아노스흑화09(self.ctx)


# ########################씬6 아노스 흑화########################
class 아노스흑화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_effect(trigger_ids=[2607])
        self.set_cinematic_ui(type=1)
        # self.set_scene_skip(state=아노스흑화09, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스흑화02(self.ctx)


class 아노스흑화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(path_ids=[6000,6001], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=200, sequence_name='Event_02_A,Event_02_Idle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스흑화03(self.ctx)


class 아노스흑화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[6002,6003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 아노스흑화04(self.ctx)


class 아노스흑화04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[6004,6005], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아노스흑화05(self.ctx)


class 아노스흑화05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2605], visible=True)
        self.destroy_monster(spawn_ids=[200])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 아노스흑화06(self.ctx)


class 아노스흑화06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[6006,6007,6008], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 아노스흑화07(self.ctx)


class 아노스흑화07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_time_scale(enable=True, start_scale=0.5, end_scale=0.3, duration=15.0, interpolator=1) # 2초간 느려지기 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 아노스흑화08(self.ctx)


class 아노스흑화08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FadeInOut1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 아노스흑화08_1(self.ctx)


class 아노스흑화08_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 아노스흑화09(self.ctx)


class 아노스흑화09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000151, portal_id=10)


initial_state = Wait01
