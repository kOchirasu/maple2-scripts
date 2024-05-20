""" trigger/52000050_qd/main_02.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=7001, initial_sequence='Sit_Down_A') # 준타
        self.set_actor(trigger_id=7002, initial_sequence='Down_Idle_A') # 틴차이
        self.set_mesh(trigger_ids=[6020,6021,6022,6023,6024,6025,6026,6027,6028,6029,6030]) # 짹쨱이
        self.set_mesh(trigger_ids=[6011], visible=True) # 원래 벽돌 안보이게
        self.set_interact_object(trigger_ids=[10000478], state=1)
        self.set_effect(trigger_ids=[7010])
        self.set_breakable(trigger_ids=[9010,9011,9012,9013,9014]) # 참새들 조용히 있음
        self.set_visible_breakable_object(trigger_ids=[9010,9011,9012,9013,9014]) # 참새들 조용히 있음

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003059], quest_states=[1]):
            return start_c(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003058], quest_states=[2]):
            # 완료 가능
            return start_c(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003058], quest_states=[1]):
            # 진행
            return start_b(self.ctx)


class start_b(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7011], visible=True)
        self.set_mesh(trigger_ids=[6020,6021,6022,6023,6024,6025], visible=True) # 짹쨱이
        self.set_mesh_animation(trigger_ids=[6020,6021,6022,6023,6024,6025], visible=True)
        self.destroy_monster(spawn_ids=[101,102,103,111,112,121,122]) # 퀘스트용 소멸
        self.set_actor(trigger_id=7001, visible=True, initial_sequence='Sit_Down_A') # 준타
        self.set_actor(trigger_id=7002, visible=True, initial_sequence='Down_Idle_A') # 틴차이
        self.set_mesh(trigger_ids=[6010], visible=True)
        self.set_mesh(trigger_ids=[6011]) # 원래 벽돌 안보이게

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000478], state=0):
            return start_b_02(self.ctx)


class start_b_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7010], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.move_user(map_id=52000048, portal_id=1)
            return None # Missing State: start_02_end


class start_c(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6020,6021,6022,6023,6024], visible=True) # 짹쨱이
        self.set_mesh_animation(trigger_ids=[6020,6021,6022,6023,6024,6025], visible=True)
        self.destroy_monster(spawn_ids=[101,102,111,112,121,122]) # 퀘스트용 소멸
        self.set_actor(trigger_id=7001, visible=True, initial_sequence='Sit_Down_A') # 준타
        self.set_actor(trigger_id=7002, visible=True, initial_sequence='Down_Idle_A') # 틴차이
        self.set_mesh(trigger_ids=[6010], visible=True)
        self.set_mesh_animation(trigger_ids=[6010], visible=True)
        self.set_interact_object(trigger_ids=[10000478], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003059], quest_states=[1]):
            self.move_user(map_id=52000050, portal_id=2)
            return start_c_02(self.ctx)


class start_c_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6020,6021,6022,6023,6024,6025]) # 짹쨱이
        self.set_mesh(trigger_ids=[6026,6027,6028,6029,6030], visible=True) # 짹쨱이
        self.set_mesh_animation(trigger_ids=[6026,6027,6028,6029,6030], visible=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8010,8011,8001], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_9902') # 유저를 이동시킨다
        self.set_dialogue(type=1, script='$52000050_QD__MAIN_02__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_c_03(self.ctx)


class start_c_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000050_QD__MAIN_02__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_c_04(self.ctx)


class start_c_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000050_QD__MAIN_02__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_c_05(self.ctx)


class start_c_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(trigger_ids=[9010,9011,9012,9013,9014], enable=True) # 참새들 조용히 있음
        self.set_visible_breakable_object(trigger_ids=[9010,9011,9012,9013,9014], visible=True) # 참새들 조용히 있음

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.set_mesh(trigger_ids=[6026,6027,6028,6029,6030]) # 짹쨱이
            return start_c_06(self.ctx)


class start_c_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7011]) # 지저귐 삭제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera_path(path_ids=[8001])
        self.set_achievement(trigger_id=701, type='trigger', achieve='FlyingBirds') # 퀘스트 목표 체크용 업적이벤트 발생

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.set_breakable(trigger_ids=[9010,9011,9012,9013,9014]) # 참새들 조용히 있음
            self.set_visible_breakable_object(trigger_ids=[9010,9011,9012,9013,9014]) # 참새들 조용히 있음
            return start_c_07(self.ctx)


class start_c_07(trigger_api.Trigger):
    pass


initial_state = ready
