""" trigger/52000096_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50001514], quest_states=[1]):
            # 50001514 퀘스트 진행 중 상태!
            return 몹소환01(self.ctx)
        if self.quest_user_detected(box_ids=[9000], quest_ids=[50100040], quest_states=[1]):
            # 50100040 퀘스트 진행 중 상태!
            return 몹소환01(self.ctx)


class 몹소환01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8001], return_view=False)
        self.spawn_monster(spawn_ids=[1001], auto_target=False) # 몬스터 스폰포인트 1
        self.spawn_monster(spawn_ids=[1002], auto_target=False) # 몬스터 스폰포인트 2
        self.spawn_monster(spawn_ids=[1003], auto_target=False) # 몬스터 스폰포인트 3
        self.spawn_monster(spawn_ids=[1004], auto_target=False) # 몬스터 스폰포인트 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 위협당함01(self.ctx)


class 위협당함01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1001, script='$52000096_QD__MAIN__0$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 위협당함02(self.ctx)


class 위협당함02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1002, script='$52000096_QD__MAIN__1$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 위협당함03(self.ctx)


class 위협당함03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1003, script='$52000096_QD__MAIN__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 위협당함04(self.ctx)


class 위협당함04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1004, script='$52000096_QD__MAIN__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 시점이동(self.ctx)


class 시점이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 경로이동(self.ctx)


class 경로이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, script='$52000096_QD__MAIN__4$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 몹말풍선01(self.ctx)


class 몹말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=3.0)
        self.set_dialogue(type=1, spawn_id=1003, script='$52000096_QD__MAIN__5$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrol_name='MS2PatrolData_PC_01')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawn_ids=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 몬스터재스폰(self.ctx)


class 몬스터재스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001]) # 몬스터 스폰포인트 1
        self.spawn_monster(spawn_ids=[1002]) # 몬스터 스폰포인트 2
        self.spawn_monster(spawn_ids=[1003]) # 몬스터 스폰포인트 3
        self.spawn_monster(spawn_ids=[1004]) # 몬스터 스폰포인트 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
