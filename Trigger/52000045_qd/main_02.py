""" trigger/52000045_qd/main_02.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=100):
            self.set_actor(trigger_id=5001, initial_sequence='Idle_A')
            self.set_actor(trigger_id=5002, initial_sequence='Idle_A')
            self.set_actor(trigger_id=5003, initial_sequence='Idle_A')
            return ready_02(self.ctx)


class ready_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=52000045, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[902], auto_target=False) # 로스트차일드
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrol_name='MS2PatrolData_2010') # 유저를 이동시킨다
        self.select_camera_path(path_ids=[8004], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=902, patrol_name='MS2PatrolData_2004')
        self.move_user_path(patrol_name='MS2PatrolData_2003') # 유저를 이동시킨다
        self.select_camera_path(path_ids=[8010], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return setup_userscript01(self.ctx)


class setup_userscript01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000045_QD__MAIN_02__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_A_03(self.ctx)


class start_A_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8010,8013], return_view=False)
        self.set_dialogue(type=1, script='$52000045_QD__MAIN_02__3$', time=3)
        self.set_dialogue(type=1, spawn_id=902, script='$52000045_QD__MAIN_02__4$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=902, script='$52000045_QD__MAIN_02__1$', time=3, arg5=1)
        self.set_npc_emotion_loop(spawn_id=902, sequence_name='Talk_A', duration=3000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7003], visible=True)
        self.spawn_monster(spawn_ids=[887,886,888], auto_target=False)
        self.set_dialogue(type=1, spawn_id=902, script='$52000045_QD__MAIN_02__5$', time=1, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return start_05(self.ctx)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8014], return_view=False)
        self.set_dialogue(type=1, script='$52000045_QD__MAIN_02__6$', time=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2200):
            return start_06(self.ctx)


class start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequence_names=['Down2_A','Down_Idle_A','Down_Idle_A','Down_Idle_A','Down_Idle_A','Down_Idle_A'])
        self.set_effect(trigger_ids=[7005], visible=True)
        self.set_effect(trigger_ids=[7004], visible=True)
        self.spawn_monster(spawn_ids=[872,873], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2050):
            return start_07(self.ctx)


class start_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8014,8015], return_view=False)
        self.spawn_monster(spawn_ids=[871,876], auto_target=False)
        self.set_pc_emotion_loop(sequence_name='Down_Idle_A', duration=80000.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=900):
            return start_08(self.ctx)


class start_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[872,875,871,876], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return start_09(self.ctx)


class start_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7005])
        self.spawn_monster(spawn_ids=[874,873,872], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return start_10(self.ctx)


class start_10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=701, type='trigger', achieve='InvestgatedScretroom') # 퀘스트 목표 체크용 업적이벤트 발생
        self.move_user(map_id=52000046, portal_id=1)


initial_state = ready
