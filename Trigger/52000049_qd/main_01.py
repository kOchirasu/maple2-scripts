""" trigger/52000049_qd/main_01.xml """
import trigger_api


"""
[출연진]
101 : 준타 (퀘스트)
111,121 : 준타 (연출)
102,122 : 틴차이 (퀘스트)
112 : 틴차이 (연출)
103 : 애니마르 에너지
"""
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[8099])
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306], auto_target=False) # 연출용 라오즈리젠
        self.set_mesh(trigger_ids=[2116])
        self.set_mesh(trigger_ids=[2201,2202,2203,2204,2205,2206]) # 투명 발판

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[1]):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[2]):
            return start_23(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[3]):
            return start_23(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='MS2PatrolData_2001') # 유저를 이동시킨다
        self.select_camera_path(path_ids=[8001,8002,8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7012], visible=True)
        self.set_mesh(trigger_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115], interval=100, fade=8.0) # 모니터 켜짐
        self.set_mesh(trigger_ids=[2116], visible=True, interval=100, fade=3.0)
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 연출용 리젠 칸두라
        self.move_user_path(patrol_name='MS2PatrolData_2002') # 유저를 이동시킨다
        self.set_dialogue(type=2, spawn_id=11001761, script='$52000049_QD__MAIN_01__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7012])
        self.set_dialogue(type=1, script='$52000049_QD__MAIN_01__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001761, script='$52000049_QD__MAIN_01__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001761, script='$52000049_QD__MAIN_01__3$', time=4)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Event_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.select_camera_path(path_ids=[8004], return_view=False)
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.destroy_monster(spawn_ids=[301,302,303,304,305,306]) # 연출용 라오즈소멸
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001,7002,7003,7004,7005,7006], visible=True)
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206], auto_target=False) # 연출용 비전 리젠

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return start_08(self.ctx)


class start_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2003') # 유저를 이동시킨다
        self.select_camera_path(path_ids=[8005,8006,8007], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001761, script='$52000049_QD__MAIN_01__4$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_09(self.ctx)


class start_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000049_QD__MAIN_01__5$', time=3)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Failure_A','Emotion_Failure_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_10(self.ctx)


class start_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000049_QD__MAIN_01__6$', time=3)
        self.set_pc_emotion_loop(sequence_name='Emotion_Failure_Idle_A', duration=6000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return start_11(self.ctx)


class start_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001761, script='$52000049_QD__MAIN_01__7$', time=4)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Event_A')
        self.select_camera_path(path_ids=[8008], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_12(self.ctx)


class start_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2004') # 유저를 이동시킨다
        self.select_camera_path(path_ids=[8009], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001761, script='$52000049_QD__MAIN_01__8$', time=4)
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Attack_01_D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_13(self.ctx)


class start_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7010], visible=True)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2011') # 비전 클론 이동
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_2012') # 비전 클론 이동
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_2013') # 비전 클론 이동
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_2014') # 비전 클론 이동
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_2015') # 비전 클론 이동
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_2016') # 비전 클론 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return start_14(self.ctx)


class start_14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7011], visible=True)
        self.set_pc_emotion_sequence(sequence_names=['Emotion_Failure_A','Emotion_Failure_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return start_15(self.ctx)


class start_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequence_name='Emotion_Failure_Idle_A', duration=18000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_16(self.ctx)


class start_16(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_17(self.ctx)


class start_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[501], auto_target=False) # 연출용 리젠 준타
        self.select_camera_path(path_ids=[8010,8011,8012], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=700):
            self.set_skill(trigger_ids=[8099], enable=True)
            self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2021') # 비전 클론 이동
            self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_2022') # 비전 클론 이동
            self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_2023') # 비전 클론 이동
            self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_2024') # 비전 클론 이동
            self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_2025') # 비전 클론 이동
            self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_2026') # 비전 클론 이동
            self.set_npc_emotion_sequence(spawn_id=201, sequence_name='Bore_B')
            self.set_npc_emotion_sequence(spawn_id=202, sequence_name='Bore_B')
            self.set_npc_emotion_sequence(spawn_id=203, sequence_name='Bore_B')
            self.set_npc_emotion_sequence(spawn_id=204, sequence_name='Bore_B')
            self.set_npc_emotion_sequence(spawn_id=205, sequence_name='Bore_B')
            self.set_npc_emotion_sequence(spawn_id=206, sequence_name='Bore_B')
            return start_18(self.ctx)


class start_18(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_effect(trigger_ids=[7010])
            self.destroy_monster(spawn_ids=[201,202,203,204,205,206]) # 퀘스트용 소멸
            return start_19(self.ctx)


class start_19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=501, patrol_name='MS2PatrolData_2030') # 준타 이동
        self.set_dialogue(type=1, spawn_id=501, script='$52000049_QD__MAIN_01__9$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_dialogue(type=1, spawn_id=101, script='$52000049_QD__MAIN_01__10$', time=3)
            self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_2099') # 칸두라 이동
            return start_20(self.ctx)


class start_20(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_achievement(trigger_id=701, type='trigger', achieve='HeroJunta') # 퀘스트 목표 체크용 업적이벤트 발생
            self.set_mesh(trigger_ids=[2100,2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115], visible=True, interval=100, fade=8.0) # 모니터 꺼짐
            self.destroy_monster(spawn_ids=[101]) # 퀘스트용 소멸
            self.select_camera_path(path_ids=[8013])
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return start_21(self.ctx)


class start_21(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003053], quest_states=[2]):
            self.destroy_monster(spawn_ids=[501]) # 연출용 준타 소멸
            self.spawn_monster(spawn_ids=[502], auto_target=False) # 퀘스트용 준타 생성
            return start_22(self.ctx)


class start_22(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003054], quest_states=[1]):
            self.move_user(map_id=52000050, portal_id=1)
            return end(self.ctx)


class start_23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[502], auto_target=False) # 연출용 리젠 준타

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return start_22(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = ready
