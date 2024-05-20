""" trigger/52010007_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1001], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[100], quest_ids=[10002834], quest_states=[1]):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1002,1003,1004], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_A')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_A')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=102, spawn_ids=[1002]):
            return 둔바대사01(self.ctx)
        if self.npc_detected(box_id=102, spawn_ids=[1003]):
            return 둔바대사01(self.ctx)


class 둔바대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11001217, script='$52010007_QD__MAIN__0$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에레브대사01(self.ctx)


class 에레브대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010007_QD__MAIN__1$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return NPC이동2(self.ctx)


class NPC이동2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_B')
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_B')
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 말풍선대사01(self.ctx)


class 말풍선대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1003, script='$52010007_QD__MAIN__2$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 말풍선대사02(self.ctx)


class 말풍선대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1003, script='$52010007_QD__MAIN__3$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 말풍선대사03(self.ctx)


class 말풍선대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=1004, script='$52010007_QD__MAIN__4$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 스타츠대사01(self.ctx)


class 스타츠대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001292, script='$52010007_QD__MAIN__5$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 스타츠이동(self.ctx)


class 스타츠이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1002, patrol_name='MS2PatrolData_1002_C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 타라이동(self.ctx)


class 타라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=1004, patrol_name='MS2PatrolData_1004_C')
        self.set_dialogue(type=1, spawn_id=1004, script='$52010007_QD__MAIN__6$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 둔바이동(self.ctx)


class 둔바이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1002])
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003_C')
        self.set_dialogue(type=1, spawn_id=1003, script='$52010007_QD__MAIN__7$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 에레브대사02(self.ctx)


class 에레브대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[1003,1004])
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010007_QD__MAIN__8$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 에레브대사03(self.ctx)


class 에레브대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=2, spawn_id=11000075, script='$52010007_QD__MAIN__9$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            self.select_camera(trigger_id=301, enable=False)
            self.set_achievement(trigger_id=100, type='trigger', achieve='Find_Lamestone')
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
