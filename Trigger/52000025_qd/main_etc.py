""" trigger/52000025_qd/main_etc.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002942], quest_states=[1], job_code=30):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002942], quest_states=[2], job_code=30):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002942], quest_states=[3], job_code=30):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002951], quest_states=[1], job_code=40):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002951], quest_states=[2], job_code=40):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002951], quest_states=[3], job_code=40):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002961], quest_states=[1], job_code=20):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002961], quest_states=[2], job_code=20):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002961], quest_states=[3], job_code=20):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002971], quest_states=[1], job_code=50):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002971], quest_states=[2], job_code=50):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002971], quest_states=[3], job_code=50):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002981], quest_states=[1], job_code=10):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002981], quest_states=[2], job_code=10):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002981], quest_states=[3], job_code=10):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002981], quest_states=[1], job_code=1):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002981], quest_states=[2], job_code=1):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002981], quest_states=[3], job_code=1):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002991], quest_states=[1], job_code=60):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002991], quest_states=[2], job_code=60):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10002991], quest_states=[3], job_code=60):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003001], quest_states=[1], job_code=70):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003001], quest_states=[2], job_code=70):
            return start_B(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[10003001], quest_states=[3], job_code=70):
            return start_B(self.ctx)


class start_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[202,299], auto_target=False) # 이슈라 퀘스트
        self.destroy_monster(spawn_ids=[203,204,205])


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[201,203,204], auto_target=False)
        self.spawn_monster(spawn_ids=[101,102], auto_target=False) # 적 몬스터 1차

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101,102]):
            return start_02(self.ctx)

    def on_exit(self) -> None:
        self.set_dialogue(type=1, spawn_id=201, script='$52000025_QD__MAIN_ETC__0$', time=2, arg5=1)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111,112,113,114,115,116], auto_target=False) # 적 몬스터 2차
        self.set_dialogue(type=1, spawn_id=201, script='$52000025_QD__MAIN_ETC__1$', time=2, arg5=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[111,112,113,114,115,116]):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000025_QD__MAIN_ETC__2$', time=4) # 음성 코드 00001288
        self.set_effect(trigger_ids=[7001], visible=True) # 음성 코드 00001288

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2000') # 이슈라를 이동시킨다
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000025_QD__MAIN_ETC__3$', time=3) # 음성 코드 00001306
        self.set_effect(trigger_ids=[7003], visible=True) # 음성 코드 00001306

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return start_05(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=4)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[203,204,205])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Start_06(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.move_user(map_id=52000025, portal_id=99)


class Start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawn_id=201, patrol_name='MS2PatrolData_2001') # 이슈라를 이동시킨다
        self.move_user_path(patrol_name='MS2PatrolData_2002') # 유저를 이동시킨다
        self.select_camera_path(path_ids=[8001,8002], return_view=False) # 카메라 뒤로 당김

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Start_07(self.ctx)


class Start_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001575, script='$52000025_QD__MAIN_ETC__4$', time=3) # 렌듀비앙 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return Start_08(self.ctx)


class Start_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000025_QD__MAIN_ETC__5$', time=5)
        self.set_effect(trigger_ids=[7002], visible=True) # 음성 코드 00001290

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return Start_09(self.ctx)


class Start_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001575, script='$52000025_QD__MAIN_ETC__6$', time=4) # 렌듀비앙 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Start_10(self.ctx)


class Start_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001575, script='$52000025_QD__MAIN_ETC__7$', time=3) # 렌듀비앙 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Start_11(self.ctx)

    def on_exit(self) -> None:
        # self.select_camera_path(path_ids=[8001], return_view=False) # 카메라 뒤로 당김
        self.select_camera(trigger_id=8001, enable=False) # 카메라 초기화


class Start_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[201]) # 이슈라
        self.spawn_monster(spawn_ids=[299], auto_target=False) # 이슈라 퀘스트
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=701, type='trigger', achieve='SweepthePriates')


initial_state = idle
