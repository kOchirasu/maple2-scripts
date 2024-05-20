""" trigger/52000045_qd/main_01.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=110):
            self.set_effect(trigger_ids=[7001], visible=True)
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 비전
        self.add_buff(box_ids=[701], skill_id=70000105, level=1) # 투명 버프를 걸어준다
        self.set_dialogue(type=2, spawn_id=11001560, script='$52000045_QD__MAIN_01__0$', time=5)
        self.spawn_monster(spawn_ids=[201,202,203,204,205,206], auto_target=False)
        self.spawn_monster(spawn_ids=[301,302,303,304,305,306], auto_target=False)
        self.spawn_monster(spawn_ids=[401,402,403,404,405], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=202, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=203, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=204, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=205, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=206, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=301, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=302, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=303, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=304, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=305, patrol_name='MS2PatrolData_2001')
        self.move_npc(spawn_id=306, patrol_name='MS2PatrolData_2001')
        self.select_camera_path(path_ids=[8001,8002,8003], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001560, script='$52000045_QD__MAIN_01__1$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            self.spawn_monster(spawn_ids=[101], auto_target=False) # 비전
            self.remove_buff(box_id=701, skill_id=70000105)
            self.select_camera_path(path_ids=[8004])
            self.destroy_monster(spawn_ids=[101]) # 비전 사라짐
            self.destroy_monster(spawn_ids=[401,402,403,404,405])
            self.set_actor(trigger_id=5001, initial_sequence='Idle_A')
            self.set_actor(trigger_id=5002, initial_sequence='Idle_A')
            self.set_actor(trigger_id=5003, initial_sequence='Idle_A')
            self.set_cinematic_ui(type=4)
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_effect(trigger_ids=[7001])
            self.add_buff(box_ids=[701], skill_id=70000094, level=1) # 어질어질한 이펙트
            self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=4000.0)
            self.set_cinematic_ui(type=1)
            self.set_cinematic_ui(type=3)
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4500):
            self.set_pc_emotion_sequence(sequence_names=['Emotion_Failure_Idle_A'])
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_effect(trigger_ids=[7002], visible=True)
            self.move_user_path(patrol_name='MS2PatrolData_2002') # 유저를 이동시킨다
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_08(self.ctx)


class start_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005], return_view=False)
        self.spawn_monster(spawn_ids=[901], auto_target=False) # 스커
        self.move_user_path(patrol_name='MS2PatrolData_2004') # 유저를 이동시킨다
        self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_2003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return start_09(self.ctx)


class start_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=901, script='$52000045_QD__MAIN_01__2$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_A_10(self.ctx)


class start_A_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=901, script='$52000045_QD__MAIN_01__11$', time=3)
        self.set_dialogue(type=1, script='$52000045_QD__MAIN_01__12$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_10(self.ctx)


class start_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000045_QD__MAIN_01__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.set_effect(trigger_ids=[7003], visible=True)
            self.move_npc(spawn_id=901, patrol_name='MS2PatrolData_2005')
            return start_11(self.ctx)


class start_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[801,802,803,804,805,806], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return start_12(self.ctx)


class start_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return start_13(self.ctx)


class start_13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7004], visible=True)
        self.select_camera_path(path_ids=[8004])
        self.spawn_monster(spawn_ids=[809], auto_target=False)
        self.set_npc_emotion_loop(spawn_id=901, sequence_name='Down_Idle_A', duration=300000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.show_guide_summary(entity_id=25200473, text_id=25200473)
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            return start_14(self.ctx)


class start_14(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[801,802,803,804,805,806,809]):
            self.hide_guide_summary(entity_id=25200473)
            return start_15(self.ctx)


class start_15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_16(self.ctx)


class start_16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[7701,7702], auto_target=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.select_camera_path(path_ids=[8004], return_view=False)
            return start_17(self.ctx)


class start_17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=7702, sequence_name='Talk_A', duration=3000.0)
        self.set_dialogue(type=2, spawn_id=11001545, script='$52000045_QD__MAIN_01__4$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_18(self.ctx)


class start_18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawn_id=7701, sequence_name='Talk_A', duration=3000.0)
        self.set_dialogue(type=2, spawn_id=11001546, script='$52000045_QD__MAIN_01__5$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.move_user_path(patrol_name='MS2PatrolData_2006') # 유저를 이동시킨다
            self.move_npc(spawn_id=7701, patrol_name='MS2PatrolData_7003')
            self.move_npc(spawn_id=7702, patrol_name='MS2PatrolData_7004')
            return start_19(self.ctx)


class start_19(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.select_camera_path(path_ids=[8005], return_view=False)
            return start_20(self.ctx)


class start_20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=7701, script='$52000045_QD__MAIN_01__6$', time=3)
        self.set_dialogue(type=1, spawn_id=7702, script='$52000045_QD__MAIN_01__7$', time=3, arg5=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_21(self.ctx)


class start_21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000045_QD__MAIN_01__8$', time=2)
        self.set_dialogue(type=1, script='$52000045_QD__MAIN_01__9$', time=3, arg5=2)
        self.set_dialogue(type=1, script='$52000045_QD__MAIN_01__10$', time=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return start_22(self.ctx)


class start_22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_2007') # 유저를 이동시킨다

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            self.set_achievement(trigger_id=701, type='trigger', achieve='MeetAgainStriker') # 퀘스트 목표 체크용 업적이벤트 발생
            self.move_user(map_id=2000138, portal_id=103)
            return start_22(self.ctx)


initial_state = ready
