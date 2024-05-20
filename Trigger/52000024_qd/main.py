""" trigger/52000024_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[20002233], quest_states=[1]):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[20002233], quest_states=[2]):
            return start(self.ctx)
        if self.quest_user_detected(box_ids=[701], quest_ids=[20002233], quest_states=[3]):
            return start_B(self.ctx)


class start_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[106], auto_target=False) # 유페리아
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 레잔


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.move_user_path(patrol_name='MS2PatrolData_2101') # 유저를 이동시킨다
        self.spawn_monster(spawn_ids=[101], auto_target=False) # 레잔
        self.spawn_monster(spawn_ids=[102], auto_target=False) # 유페리아
        self.spawn_monster(spawn_ids=[103], auto_target=False) # 이슈라
        self.select_camera_path(path_ids=[8001,8002,8003], return_view=False) # 카메라 뒤로 당김

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return Start_02(self.ctx)


class Start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return Start_03(self.ctx)


class Start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=103, patrol_name='MS2PatrolData_2001') # 이슈라를 이동시킨다
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2002') # 유페리아를 이동시킨다

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Start_04(self.ctx)


class Start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[7006], visible=True)
        self.set_dialogue(type=2, spawn_id=11001564, script='$52000024_QD__MAIN__0$', time=5) # 유페리아 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return Start_05(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[103])
        self.spawn_monster(spawn_ids=[104], auto_target=False) # 이슈라


class Start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(trigger_id=8004, enable=False) # 카메라 초기화

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return startB_01(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


"""
class Start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='동료들이 있는 쪽으로 가서 무슨 일인지 알아보자.', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[702], quest_ids=[20002233], quest_states=[2]):
            return startB_01(self.ctx)
        if self.count_users(box_id=702) >= 1:
            return startB_01(self.ctx)
"""

class startB_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=8005) # 카메라 초기화
        self.move_user(map_id=52000024, portal_id=99)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return startB_02(self.ctx)


class startB_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return startB_04(self.ctx)


"""
class startB_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001564, script='감히... 해적 따위가...', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return startB_04(self.ctx)
"""

class startB_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005,8006], return_view=False) # 카메라 뒤로 당김
        self.set_effect(trigger_ids=[7003], visible=True) # 음성 코드 00001283
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000024_QD__MAIN__1$', time=3) # 음성 코드 00001283

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return startB_07(self.ctx)


"""
class startB_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001244, script='렌듀비앙과 원정대가 도착과 동시에 \\n이곳 해적들의 기습을 받고 놈들에게 끌려갔다고 하는구나.', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return startB_06(self.ctx)
"""

"""
class startB_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2003')
        self.set_dialogue(type=2, spawn_id=11001244, script='멀리 가지는 못했을 터... 추격대원들이 해적들의 본거지를 알아보러 갔으니 곧...', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return startB_07(self.ctx)
"""

class startB_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[105], auto_target=False)
        self.set_effect(trigger_ids=[7001], visible=True) # 음성 코드 03000870
        self.set_dialogue(type=2, spawn_id=11001570, script='$52000024_QD__MAIN__2$', time=7) # 음성 코드 03000870

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return startB_08(self.ctx)


class startB_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8007,8008], return_view=False) # 카메라 뒤로 당김
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2006') # 이슈라 슌을 바라봄
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2005') # 유페리아 슌을 바라봄
        self.move_user_path(patrol_name='MS2PatrolData_2102') # 유저를 이동시킨다

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return startB_09(self.ctx)


class startB_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2008') # 이슈라 슌을 바라봄
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000024_QD__MAIN__3$', time=5) # 음성 코드 00001287
        self.set_effect(trigger_ids=[7004], visible=True) # 음성 코드 00001287

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return startB_10(self.ctx)


class startB_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001570, script='$52000024_QD__MAIN__4$', time=2) # 음성 코드 03000871
        self.set_effect(trigger_ids=[7002], visible=True) # 음성 코드 03000871

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return startB_11(self.ctx)


class startB_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=105, patrol_name='MS2PatrolData_2007') # 슌 집에감

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return startB_12(self.ctx)


class startB_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[105]) # 슌 사라짐
        self.select_camera(trigger_id=8005, enable=False) # 카메라 초기화
        self.set_achievement(trigger_id=701, type='trigger', achieve='PirateRiddenSea')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[701], quest_ids=[20002233], quest_states=[3]):
            # 퀘스트 완료 상태
            return startC_01(self.ctx)


class startC_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=104, script='$52000024_QD__MAIN__5$', time=3) # 음성 코드 00001309
        self.set_effect(trigger_ids=[7005], visible=True) # 음성 코드 00001309

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return startC_02(self.ctx)


class startC_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_dialogue(type=1, spawn_id=102, script='어서 가 봐! 레잔은 내가 챙길테니까.', time=3)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_2002')
        self.move_npc(spawn_id=104, patrol_name='MS2PatrolData_2007') # 이슈라 집에감

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return startC_03(self.ctx)


class startC_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[104]) # 이슈라 사라짐

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701) >= 1:
            return startD_01(self.ctx)


class startD_01(trigger_api.Trigger):
    pass


initial_state = idle
