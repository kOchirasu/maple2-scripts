""" trigger/51000006_dg/51000006_main.xml """
import trigger_api
from System.Numerics import Vector3


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=51000006, portal_id=10)
        # 101: 게임상대 - 11004827 NPC 시간여행자 블랙빈
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        # 이펙트 601: 게임상대 - 11004718 블랙빈 머리 위 스포트라이트 이펙트
        self.set_effect(trigger_ids=[601])
        # 이펙트 602: PC 머리 위 스포트라이트 이펙트
        self.set_effect(trigger_ids=[602])
        # 이펙트 603: 게임상대 - 11004718 블랙빈 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[603])
        # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[604])
        # 이펙트 610: PC 머리 위 내리는 비 이펙트
        self.set_effect(trigger_ids=[610])
        self.set_actor(trigger_id=611, initial_sequence='0') # 미니빈01끄기
        self.set_actor(trigger_id=612, initial_sequence='0') # 미니빈02끄기
        self.set_actor(trigger_id=613, initial_sequence='0') # 미니빈03끄기
        self.set_actor(trigger_id=614, initial_sequence='0') # 미니빈04끄기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 인트로(self.ctx)


class 인트로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=셋둘하나_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=1000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 인트로00(self.ctx)


class 인트로00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003,8004], return_view=False)
        self.set_cinematic_ui(type=1)
        # 대사내용01 : 안녕! 난 자유로운 블랙빈! 노는 게 제일 좋아~\n지금부터 나랑 놀자!"
        self.set_cinematic_ui(type=3, script='$51000006_DG__51000006_MAIN__0$')
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Walk_A', duration_tick=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2600):
            return 인트로01(self.ctx)


class 인트로01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005,8006], return_view=False)
        self.set_cinematic_ui(type=1)
        # 대사내용02 : 나와 다른 방향을 선택하면 네가 이기고, \n같은 방향을 선택하면 지는 거야~!
        self.set_cinematic_ui(type=3, script='$51000006_DG__51000006_MAIN__1$')
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Event_Bore_A', duration_tick=2900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인트로02(self.ctx)


class 인트로02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002,8001], return_view=False)
        self.set_cinematic_ui(type=1)
        # 대사내용03 : 네가 다섯 번 지면 놀이는 끝!\n오래 버틸수록 높은 점수를 받지!
        self.set_cinematic_ui(type=3, script='$51000006_DG__51000006_MAIN__2$')
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Event_Eat_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3100):
            return 인트로03(self.ctx)


class 인트로03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State,  setsceneskip 1 close
        self.set_scene_skip()
        # setsceneskip 1 close
        # setsceneskip 1 close
        self.select_camera_path(path_ids=[8003,8006], return_view=False)
        self.set_cinematic_ui(type=1)
        # 대사내용04 : 순위가 높으면 선물도 주지! 어때, 끌리지?\n그럼 바로 시작해 보자~ 뿡뿡!
        self.set_cinematic_ui(type=3, script='$51000006_DG__51000006_MAIN__3$')
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Attack_01_G', duration_tick=3200)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3300):
            return 게임시작_대기(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 셋둘하나_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 게임시작_대기(self.ctx)
        if not self.user_detected(box_ids=[9000]):
            return 연출종료(self.ctx)


class 게임시작_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='BlackbeanThreeTwoOne_start')
        # 로그를 남기기 위한 행 : arg5가 트리거 전체에서 유니크한 값이 들어가야 하며, arg1은 코드에 남고 있지 않음(서바이벌일 때만 서바이벌 로그 불러옴)
        self.write_log(log_name='ThreeTwoOne_log', trigger_id=9000, event='char_event', sub_event='BlackbeanThreeTwoOnegamestart')
        # lifeCount : 최대 사망 횟수
        self.arcade_three_two_one3_start_game(life_count=5, init_score=10000)
        # # 셋둘하나는 1라운드 내에서 무한루핑이므로 라운드 ui를 표시하지 않아 이 행을 넣지 않음
        self.set_event_ui_round(rounds=[1,1], v_offset=120)
        self.set_user_value(trigger_id=4001, key='Fail', value=1) # Fail Event on
        self.add_balloon_talk(msg='$51000006_DG__51000006_MAIN__4$', duration=3000) # PC : 너한텐 안 져!
        # 시작 효과음 / 레디-고! 들어간 버전 02100323
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_GetReadyGo_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라운드준비(self.ctx)


class 라운드준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이펙트 601: 게임상대 - 11004718 블랙빈 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(trigger_ids=[601])
        # 이펙트 602: PC 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(trigger_ids=[602])
        # 이펙트 603: 게임상대 - 11004718 블랙빈 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[603])
        # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[604])
        # 이펙트 610: PC 머리 위 내리는 비 이펙트
        self.set_effect(trigger_ids=[610])
        self.set_actor(trigger_id=611, initial_sequence='0') # 미니빈01끄기
        self.set_actor(trigger_id=612, initial_sequence='0') # 미니빈02끄기
        self.set_actor(trigger_id=613, initial_sequence='0') # 미니빈03끄기
        self.set_actor(trigger_id=614, initial_sequence='0') # 미니빈04끄기
        self.set_pc_rotation(rotation=Vector3(0,0,0))

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9000]):
            return 완전끝(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 라운드시작(self.ctx)


class 라운드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 26300736 가이드 텍스트 ON : [[icon:click]] 방향을 선택하세요.
        self.show_guide_summary(entity_id=1, text_id=26300736, duration=3000)
        # uiDuration : 게임 UI (화살표) 노출 시간
        self.arcade_three_two_one3_start_round(ui_duration=4, round=1)
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_ArrowPopup_01') # 화살표 Ui 팝업 효과음 02100325

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9000]):
            return 완전끝(self.ctx)
        if self.wait_tick(wait_tick=4000):
            return 라운드진행(self.ctx)


class 라운드진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='$51000006_DG__51000006_MAIN__5$', duration=1800) # 블랙빈 대사 : 빙글빙글~!

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1.0):
            return 좌로돌아01(self.ctx)
        if self.random_condition(weight=1.0):
            return 뒤로돌아02(self.ctx)
        if self.random_condition(weight=1.0):
            return 우로돌아03(self.ctx)


class 좌로돌아01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one3_result_round(result_direction=1)
        # 블랙빈 왼쪽으로 돔 : 270도 = resultDirection 1
        self.set_npc_rotation(spawn_id=101, rotation=270.0)
        # 블랙빈 도는 효과음 2500밀리초 02100326
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 결과연출(self.ctx)


class 뒤로돌아02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one3_result_round(result_direction=2)
        # 블랙빈 뒤쪽으로 돔 : 180도 = resultDirection 2
        self.set_npc_rotation(spawn_id=101, rotation=180.0)
        # 블랙빈 도는 효과음 2500밀리초 02100326
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 결과연출(self.ctx)


class 우로돌아03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one3_result_round(result_direction=3)
        # 블랙빈 오른쪽으로 돔 : 90도 = resultDirection 3
        self.set_npc_rotation(spawn_id=101, rotation=90.0)
        # 블랙빈 도는 효과음 2500밀리초 02100326
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 결과연출(self.ctx)


class 결과연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.init_npc_rotation(spawn_ids=[101])
        self.set_pc_rotation(rotation=Vector3(0,0,0))
        # 이펙트 601: 게임상대 - 11004718 블랙빈 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(trigger_ids=[601])
        # 이펙트 602: PC 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(trigger_ids=[602])
        # 이펙트 603: 게임상대 - 11004718 블랙빈 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[603])
        # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[604])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ThreeTwoOneResult') == 1:
            # ThreeTwoOneResult 1 = 유저승리 = 다른방향
            # # 26300737 가이드 텍스트 ON : 승리
            self.show_guide_summary(entity_id=2, text_id=26300737, duration=3000)
            self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Dance_C_Ride', duration_tick=3300) # 블랙빈 돌아서서 고개숙이고 씩씩 3300
            self.set_pc_emotion_loop(sequence_name='Emotion_Dance_E', duration=3300.0) # PC 신나서 댄스
            self.set_effect(trigger_ids=[602], visible=True) # PC 머리 위 스포트라이트 이펙트
            # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
            self.set_effect(trigger_ids=[604], visible=True)
            self.add_balloon_talk(spawn_id=101, msg='$51000006_DG__51000006_MAIN__6$', duration=3300) # 블랙빈 : 내가 졌잖아?!
            self.add_balloon_talk(msg='$51000006_DG__51000006_MAIN__7$', duration=3300) # …PC : 내가 이겼지롱!
            self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Correct_01') # 성공 효과음 02100327
            return 결과정산(self.ctx)
        if self.user_value(key='ThreeTwoOneResult') == 0:
            # ThreeTwoOneResult 0 = 유저패배 = 같은방향
            # # 26300738 가이드 텍스트 ON : 패배
            self.show_guide_summary(entity_id=3, text_id=26300738, duration=3000)
            self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Event_Happy_A', duration_tick=3300)
            self.set_effect(trigger_ids=[601], visible=True) # 블랙빈 머리 위 스포트라이트 이펙트
            # 이펙트 603: 게임상대 - 11004718 블랙빈 머리 위 불꽃놀이 이펙트
            self.set_effect(trigger_ids=[603], visible=True)
            self.set_effect(trigger_ids=[610], visible=True) # 이펙트 610: PC 머리 위에 비
            self.set_actor(trigger_id=611, visible=True, initial_sequence='Run_A') # 약올리는미니빈01 ON
            self.set_actor(trigger_id=612, visible=True, initial_sequence='Run_A') # 약올리는미니빈02 ON
            self.set_actor(trigger_id=613, visible=True, initial_sequence='Run_A') # 약올리는미니빈03 ON
            self.set_actor(trigger_id=614, visible=True, initial_sequence='Run_A') # 약올리는미니빈04 ON
            self.set_pc_emotion_sequence(sequence_names=['Emotion_Fuss_A']) # PC 패배
            self.add_balloon_talk(spawn_id=101, msg='$51000006_DG__51000006_MAIN__8$', duration=3300) # …블랙빈 : 얼레리꼴레리~ 졌대요~ 메롱!
            self.add_balloon_talk(msg='$51000006_DG__51000006_MAIN__9$', duration=3300) # …PC : 으악! 분해!
            self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Wrong_01') # 패배 효과음 02100328
            return 결과정산(self.ctx)


class 결과정산(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one3_result_round2(round=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2300):
            return 라운드결과(self.ctx)


class 라운드결과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one3_clear_round(round=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라운드준비(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one3_end_game()
        self.move_user(map_id=51000006, portal_id=44)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 진짜끝(self.ctx)


class 진짜끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8010)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Result_01') # 끝나는 효과음 02100329 셋둘하나 전용

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 완전끝(self.ctx)


class 완전끝(trigger_api.Trigger):
    pass


initial_state = 입장
