""" trigger/52000050_qd/main_01.xml """
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
        self.set_effect(trigger_ids=[7011]) # 참새 조용함
        self.set_breakable(trigger_ids=[9001,9002,9003,9004,9005]) # 참새들 조용히 있음
        self.set_visible_breakable_object(trigger_ids=[9001,9002,9003,9004,9005]) # 참새들 조용히 있음
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010])
        self.spawn_monster(spawn_ids=[101,102,103], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003056], quest_states=[3]):
            # 준타와 틴차이 없는 스테이트
            return quest_end(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003056], quest_states=[2]):
            # 준타와 틴차이 없는 스테이트
            return quest_end(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003055], quest_states=[3]):
            return start_02_resume(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003055], quest_states=[2]):
            return start_02_j_resume(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003055], quest_states=[1]):
            return start_02_resume(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003054], quest_states=[3]):
            return start_02_Ready(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003054], quest_states=[2]):
            return start_02_Ready(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003054], quest_states=[1]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[101,102]) # 퀘스트용 소멸
        self.spawn_monster(spawn_ids=[111,112], auto_target=False) # 연출용 리젠
        self.move_npc(spawn_id=112, patrol_name='MS2PatrolData_1201') # 연출용 틴차이 이동
        self.set_dialogue(type=1, spawn_id=112, script='$52000050_QD__MAIN_01__8$', time=2)
        self.set_dialogue(type=1, spawn_id=112, script='$52000050_QD__MAIN_01__0$', time=2, arg5=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.set_achievement(trigger_id=701, type='trigger', achieve='MovetoNewHouse') # 퀘스트 목표 체크용 업적이벤트 발생
            return ready_02(self.ctx)


class ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[112]) # 퀘스트용 소멸
        self.spawn_monster(spawn_ids=[122], auto_target=False) # 퀘스트용 리젠

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003055], quest_states=[1]):
            # 10003055 가 진행중일 때
            return start_02(self.ctx)


class start_02_Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102])
        self.spawn_monster(spawn_ids=[111,122], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003055], quest_states=[1]):
            # 10003055 가 진행중일 때
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102]) # 퀘스트용 소멸
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_1101') # 연출용 틴차이 이동
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000050_QD__MAIN_01__1$', time=4)
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_1205') # 연출용 틴차이 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.move_user_path(patrol_name='MS2PatrolData_9901') # 유저를 이동시킨다
            return start_02_b(self.ctx)


class start_02_resume(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102])
        self.spawn_monster(spawn_ids=[111,122], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=111, patrol_name='MS2PatrolData_1101') # 연출용 틴차이 이동
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000050_QD__MAIN_01__2$', time=4)
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_1205') # 연출용 틴차이 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.move_user_path(patrol_name='MS2PatrolData_9901') # 유저를 이동시킨다
            return start_02_b(self.ctx)


class start_02_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=111, sequence_name='Talk_A', duration=3000.0)
        self.set_dialogue(type=2, spawn_id=11001557, script='$52000050_QD__MAIN_01__3$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_02_c(self.ctx)


class start_02_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000050_QD__MAIN_01__4$', time=3)
        self.set_npc_emotion_loop(spawn_id=122, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_02_d(self.ctx)


class start_02_d(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_1202') # 연출용 틴차이 이동
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000050_QD__MAIN_01__5$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_02_e(self.ctx)


class start_02_e(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.set_breakable(trigger_ids=[9001,9002,9003,9004,9005], enable=True) # 참새들 조용히 있음
        self.set_visible_breakable_object(trigger_ids=[9001,9002,9003,9004,9005], visible=True) # 참새들 조용히 있음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=7000):
            self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005], visible=True) # 참새들 표시
            self.set_mesh_animation(trigger_ids=[6001,6002,6003,6004,6005], visible=True)
            return start_02_f(self.ctx)


class start_02_f(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_effect(trigger_ids=[7011], visible=True)
            return start_02_g(self.ctx)


class start_02_g(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003,8004], return_view=False)
        self.set_npc_emotion_loop(spawn_id=122, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_breakable(trigger_ids=[9001,9002,9003,9004,9005]) # 참새들 조용히 있음
            self.set_visible_breakable_object(trigger_ids=[9001,9002,9003,9004,9005]) # 참새들 조용히 있음
            self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_1203') # 연출용 틴차이 이동
            return start_02_h(self.ctx)


class start_02_h(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000050_QD__MAIN_01__6$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_02_i(self.ctx)


class start_02_i(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=122, sequence_name='Talk_A', duration=3000.0)
        self.set_dialogue(type=2, spawn_id=11001708, script='$52000050_QD__MAIN_01__7$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.set_achievement(trigger_id=701, type='trigger', achieve='SingingOfBirds') # 퀘스트 목표 체크용 업적이벤트 발생
            return start_02_j(self.ctx)


class start_02_j(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002])
        self.destroy_monster(spawn_ids=[111]) # 퀘스트용 소멸
        self.spawn_monster(spawn_ids=[121], auto_target=False) # 퀘스트용 리젠
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003056], quest_states=[2]):
            return start_02_k(self.ctx)


class start_02_j_resume(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102])
        self.destroy_monster(spawn_ids=[111]) # 퀘스트용 소멸
        self.spawn_monster(spawn_ids=[121,122], auto_target=False) # 퀘스트용 리젠
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005], visible=True) # 참새들 표시
        self.set_effect(trigger_ids=[7011], visible=True) # 참새 조용함

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003056], quest_states=[2]):
            return start_02_k(self.ctx)


class start_02_k(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=121, patrol_name='MS2PatrolData_1204') # 연출용 준타 이동
        self.move_npc(spawn_id=122, patrol_name='MS2PatrolData_1204') # 연출용 틴차이 이동


class quest_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101,102]) # 퀘스트용 소멸


initial_state = ready
