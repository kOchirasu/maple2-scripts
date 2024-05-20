""" trigger/52020029_qd/main30000330.xml """
import trigger_api


# 진리의 문 입장
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[30000330], quest_states=[2]):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작1(self.ctx)


class 연출시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52020029, portal_id=6002)
        self.destroy_monster(spawn_ids=[105])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[103], auto_target=False)
        self.destroy_monster(spawn_ids=[104])
        self.spawn_monster(spawn_ids=[104], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=104, sequence_name='Quest_Programming', duration=15000000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출시작2(self.ctx)


class 연출시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4005], return_view=False)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=9000.0)
        self.face_emotion(emotion_name='defaultBattle')
        self.add_cinematic_talk(npc_id=11003755, msg='어떤가요? 사용할 수 있겠어요?', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='절 너무 물로보면 곤란합니다.', duration=3000)
        self.add_cinematic_talk(npc_id=11003755, msg='그럼 순서대로 검색해볼까요?', duration=3000)
        self.set_scene_skip(state=이동, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 정보검색첫번째(self.ctx)


class 정보검색첫번째(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npc_id=11003755, msg='티어스 코어에 대해서 검색해 주세요.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정보검색첫번째2(self.ctx)


class 정보검색첫번째2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4006], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=11003717, msg='데이터 서칭 완료입니다.', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='고대 문자라 읽기 어려운데... 내용은 이렇습니다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 정보검색첫번째2_1(self.ctx)


class 정보검색첫번째2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4013,4010], return_view=False)
        self.add_cinematic_talk(npc_id=11003717, msg='티어스 코어는 티마이온의 에너지 원으로, 강력한 마력의 힘이 담겨 있다.', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='티어스 코어는 몇 가지의 재료로 조합할 수 있으며, 이 재료는 크리티아스의 사방에 흩어져 있다.', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='주 재료가 되는 파멸의 날개는 크리티아스 왕가에 내려져 오는 가보로, 하나는 헤카톤 국왕이, 하나는 왕비가 가지고 있다.', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='왕비가 가지고 있던 파멸의 날개는 딸 이오네에게 넘겨졌다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=12000):
            return 정보검색첫번째3(self.ctx)


class 정보검색첫번째3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npc_id=11003717, msg='파멸의 날개 이외의 재료는 천공의 심장, 신의 눈, 영혼의 구슬, 지혜의 고리이다. ', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='천공의 심장은 마력의 숲의 천공의 탑에 보관되어 있으며, 실제적인 티어스 코어의 베이스가 되는 물질이다.', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='신의 눈은 티아만 시간의...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 정보검색첫번째3_1(self.ctx)


class 정보검색첫번째3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawn_id=104, emotion_name='dance_S')
        self.select_camera_path(path_ids=[4011], return_view=False)
        self.add_cinematic_talk(npc_id=11003717, msg='엇!?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 정보검색첫번째4(self.ctx)


class 정보검색첫번째4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Emotion_Troubled_A')
        self.add_cinematic_talk(npc_id=11003717, msg='으음...', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정보검색첫번째4_2(self.ctx)


class 정보검색첫번째4_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_3005')
        self.add_cinematic_talk(npc_id=11003755, msg='무슨일이지요?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 정보검색첫번째4_3(self.ctx)


class 정보검색첫번째4_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.add_cinematic_talk(npc_id=11003717, msg='갑자기... 티어스 코어에 대한 정보를 볼수가 없게 되었습니다.', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='누군가가... 데이터 접근을 막고 있습니다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 정보검색첫번째4_4(self.ctx)


class 정보검색첫번째4_4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11003755, msg='흐음. 누가 접근을 막고 있는건지는 알 수 있을까나?', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='노력은 해보겠지만, 시간이 필요합니다.', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='그 외의 정보라면 먼저 검색해 볼 수 있을 것 같습니다.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=9000):
            return 정보검색첫번째5(self.ctx)


class 정보검색첫번째5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.set_pc_emotion_loop(sequence_name='Talk_A', duration=20000.0)
        self.add_cinematic_talk(npc_id=0, msg='그렇다면, 제가 먼저 천공의 심장을 찾으러 가겠어요.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 정보검색첫번째5_1(self.ctx)


class 정보검색첫번째5_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=9000.0)
        self.add_cinematic_talk(npc_id=11003755, msg='...아무래도 그게 좋겠군요.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 정보검색첫번째5_2(self.ctx)


class 정보검색첫번째5_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='당신은 같이 안 가나요?', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 정보검색첫번째5_3(self.ctx)


class 정보검색첫번째5_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_npc_emotion_loop(spawn_id=103, sequence_name='Talk_A', duration=3000.0)
        self.add_cinematic_talk(npc_id=11003755, msg='예. 저는 더 찾고 싶은 정보가 있습니다.\\n나중에 뵙죠.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 정보검색첫번째6(self.ctx)


class 정보검색첫번째6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4008], return_view=False)
        self.add_cinematic_talk(npc_id=0, msg='알겠어요. 더 알게 되는 것이 있으면 알려주세요.', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 정보검색첫번째7_1(self.ctx)


class 정보검색첫번째7_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 정보검색첫번째7(self.ctx)


class 정보검색첫번째7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[4007], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정보검색첫번째8(self.ctx)


class 정보검색첫번째8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(is_visible=False)
        self.set_onetime_effect(id=5, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(path_ids=[4004], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003755, msg='방해꾼이 사라졌군요.', duration=3000)
        self.add_cinematic_talk(npc_id=11003717, msg='헤헤. 그럼 이제 뭘 찾으면 될까요?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 정보검색첫번째8_1(self.ctx)


class 정보검색첫번째8_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=104, sequence_name='Emotion_Troubled_A')
        self.add_cinematic_talk(npc_id=11003717, msg='희귀한 보석? 헤카톤 왕의 비밀?', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정보검색첫번째9(self.ctx)


class 정보검색첫번째9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4009], return_view=False)
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Bore_A')
        self.add_cinematic_talk(npc_id=11003755, msg='훗. 찾고 있는 것은 따로 있지.', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 정보검색첫번째9_1(self.ctx)


class 정보검색첫번째9_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawn_id=103, sequence_name='Bore_B')
        self.face_emotion(spawn_id=103, emotion_name='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 정보검색첫번째10(self.ctx)


class 정보검색첫번째10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4012], return_view=False)
        self.face_emotion(spawn_id=103, emotion_name='Trigger_Bore_03')
        self.add_cinematic_talk(npc_id=11003755, msg='비밀 병기 프로젝트 아포칼립스...!', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 이동(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 이동_1(self.ctx)


class 이동_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[103])
        self.destroy_monster(spawn_ids=[104])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 이동_2(self.ctx)


class 이동_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.visible_my_pc(is_visible=True)
        self.move_user(map_id=2020016, portal_id=3)


initial_state = idle
